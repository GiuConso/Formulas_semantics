"""Check vocabulary serializations and their links to the annotated JSONL corpus."""

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path
from xml.etree import ElementTree as ET

RDF = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
SKOS = 'http://www.w3.org/2004/02/skos/core#'
OA = 'http://www.w3.org/ns/oa#'
DCT = 'http://purl.org/dc/terms/'
XML_LANG = '{http://www.w3.org/XML/1998/namespace}lang'


def read_xml(path):
    root = ET.parse(path).getroot()
    assert root.tag == '{' + RDF + '}RDF'
    triples = []
    for resource in root:
        assert resource.tag == '{' + RDF + '}Description'
        subject = resource.attrib['{' + RDF + '}about']
        for prop in resource:
            namespace, name = prop.tag[1:].split('}', 1)
            uri = prop.get('{' + RDF + '}resource')
            triples.append((subject, namespace + name, uri if uri is not None else prop.text or '',
                            prop.get(XML_LANG, ''), prop.get('{' + RDF + '}datatype', ''), uri is not None))
    assert len(triples) == len(set(triples)), 'Repeated RDF triple'
    return set(triples)


def read_turtle_subset(path):
    """Read the single-triple-per-line Turtle subset emitted in this package."""
    prefixes = {}
    triples = []
    decoder = json.JSONDecoder()

    def expand(token):
        if token.startswith('<') and token.endswith('>'):
            uri = token[1:-1]
            assert not re.search(r'[\x00-\x20<>"{}|^`\\]', uri)
            return uri
        prefix, local = token.split(':', 1)
        assert re.fullmatch(r'[A-Za-z_][A-Za-z0-9_.-]*', local)
        return prefixes[prefix] + local

    for line in path.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if line.startswith('@prefix '):
            match = re.fullmatch(r'@prefix ([A-Za-z][A-Za-z0-9]*): <([^<>]+)> \.', line)
            assert match, line
            prefixes[match[1]] = match[2]
            continue
        assert line.endswith(' .'), line
        subject, predicate, obj = line[:-2].split(' ', 2)
        lang = datatype = ''
        is_uri = not obj.startswith('"')
        if is_uri:
            value = expand(obj)
        else:
            value, end = decoder.raw_decode(obj)
            suffix = obj[end:]
            if suffix.startswith('@'):
                lang = suffix[1:]
                assert re.fullmatch(r'[A-Za-z]+(?:-[A-Za-z0-9]+)*', lang)
            elif suffix.startswith('^^'):
                datatype = expand(suffix[2:])
            else:
                assert suffix == ''
        triples.append((expand(subject), expand(predicate), value, lang, datatype, is_uri))
    assert len(triples) == len(set(triples)), 'Repeated Turtle triple'
    return set(triples)


def objects(graph, subject, predicate):
    return [t for t in graph if t[0] == subject and t[1] == predicate]


def only_object(graph, subject, predicate):
    found = objects(graph, subject, predicate)
    assert len(found) == 1, (subject, predicate, len(found))
    return found[0][2]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=Path, default=Path(__file__).resolve().parent.parent / 'BCSL_Evora.jsonl')
    args = parser.parse_args()
    folder = Path(__file__).resolve().parent
    metadata = json.loads((folder / 'source_metadata.json').read_text())
    graphs = {}
    for name in ['clause_repertoire', 'clause_examples']:
        xml = read_xml(folder / (name + '.rdf'))
        turtle = read_turtle_subset(folder / (name + '.ttl'))
        assert xml == turtle, f'Different graphs: {name}'
        assert len(xml) == metadata['graph_triple_counts'][name]
        graphs[name] = xml
    graph = graphs['clause_repertoire']
    examples_graph = graphs['clause_examples']
    concepts = {s for s, p, o, lang, dtype, is_uri in graph if p == RDF + 'type' and o == SKOS + 'Concept'}
    assert len(concepts) == metadata['concept_count'] == 14
    notations = set()
    for concept in concepts:
        preferred = objects(graph, concept, SKOS + 'prefLabel')
        assert sorted(t[3] for t in preferred) == ['en', 'la']
        assert len(objects(graph, concept, SKOS + 'definition')) == 1
        assert len(objects(graph, concept, SKOS + 'inScheme')) == 1
        notation = only_object(graph, concept, SKOS + 'notation')
        assert notation not in notations
        notations.add(notation)
        mappings = [t for t in graph if t[0] == concept and t[1] in {SKOS + v for v in ['exactMatch', 'closeMatch', 'relatedMatch', 'broadMatch', 'narrowMatch']}]
        assert len(mappings) <= 1
    with (folder / 'clause_repertoire.csv').open(newline='', encoding='utf-8') as handle:
        catalog = list(csv.DictReader(handle))
    with (folder / 'clause_examples.csv').open(newline='', encoding='utf-8') as handle:
        examples = list(csv.DictReader(handle))
    assert {row['concept_uri'] for row in catalog} == concepts
    field_to_predicate = {'definition_en': 'definition', 'inclusion_en': 'scopeNote', 'exclusion_en': 'scopeNote', 'mapping_rationale_en': 'editorialNote', 'example_text': 'example'}
    for row in catalog:
        for field, predicate in field_to_predicate.items():
            assert any(t[2] == row[field] for t in objects(graph, row['concept_uri'], SKOS + predicate)), field
        if row['vid_mapping']:
            assert (row['concept_uri'], SKOS + row['vid_mapping'].split(':')[1], row['vid_uri'], '', '', True) in graph
    assert len(examples) == metadata['clause_annotation_count'] == 135
    assert len({row['example_id'] for row in examples}) == len(examples)
    records = [json.loads(line) for line in args.dataset.read_text(encoding='utf-8').splitlines() if line.strip()]
    assert len(records) == metadata['document_count'] == 16
    canonical = json.dumps(records, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
    assert hashlib.sha256(canonical.encode('utf-8')).hexdigest() == metadata['dataset_content_sha256']
    for row in examples:
        record = records[int(row['jsonl_record_1based']) - 1]
        start, end = int(row['start']), int(row['end'])
        assert 0 <= start < end <= len(record['text'])
        assert record['text'][start:end] == row['text']
        assert any(s['label'] == row['annie_label'] and s['start'] == start and s['end'] == end for s in record['spans'])
        assert hashlib.sha256(record['text'].encode('utf-8')).hexdigest() == row['document_text_sha256']
        assert only_object(examples_graph, row['example_uri'], RDF + 'value') == row['text']
        assert only_object(examples_graph, row['example_uri'], OA + 'hasBody') == row['concept_uri']
        target = only_object(examples_graph, row['example_uri'], OA + 'hasTarget')
        assert only_object(examples_graph, target, OA + 'hasSource') == row['document_uri']
        selector = only_object(examples_graph, target, OA + 'hasSelector')
        assert int(only_object(examples_graph, selector, OA + 'start')) == start
        assert int(only_object(examples_graph, selector, OA + 'end')) == end
    print('Verified: 14 concepts; 135 source annotations; CSV/RDF content and offsets; equivalent Turtle and RDF/XML graphs.')
    print('SKOS checks: preferred-label cardinality, unique notations, scheme membership, and non-conflicting declared mappings.')


if __name__ == '__main__':
    main()
