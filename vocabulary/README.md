# BCSL clause repertoire

Version 0.1.2, 3 November 2026.

This repertoire documents the fourteen operational clause categories used in *Formulas and Semantics in Digital Diplomatics*, by Giuseppe Consolo, Tamás Kovács and Georg Vogeler. It links a corpus-specific SKOS concept scheme to the *Vocabulaire international de la diplomatique* (VID).

The underlying corpus consists of sixteen BCSL notarial charters, dated 1393–1486. Definitions describe the diplomatic or legal function of each category. Occurrence in a particular transaction type or institutional configuration remains an observation about this corpus.

## Files

| File | Content |
|---|---|
| `clause_repertoire.csv` | Fourteen categories, definitions, recognition criteria, VID mappings and one representative example per category. |
| `clause_repertoire.ttl` | The category repertoire in RDF/SKOS Turtle. |
| `clause_repertoire.rdf` | The same repertoire graph in RDF/XML. |
| `clause_examples.csv` | All 135 source annotations belonging to the fourteen categories, with document identifiers, exact excerpts and character offsets. |
| `clause_examples.ttl` | The example annotations as a separate RDF graph, using the Web Annotation vocabulary. |
| `clause_examples.rdf` | The same example graph in RDF/XML. |
| `repertoire_source.json` | The definitions, recognition criteria and mapping decisions from which the repertoire was assembled. |
| `source_metadata.json` | Source version, corpus order, text hashes and annotation-count information. |
| `validate_repertoire.py` | Local consistency checks against the JSONL corpus. |

## VID alignment

Mappings were checked against the VID definitions, including the differences between entries 221a–d. The checked RDF/XML file is pinned to [VID commit cb6ffbb9cfa4cd820a5b0d0fd001a6f49a9c0599](https://github.com/GVogeler/VID/blob/cb6ffbb9cfa4cd820a5b0d0fd001a6f49a9c0599/skos/VID.rdf.xml), the latest commit affecting that file when checked.

The repertoire uses `skos:exactMatch` for equivalent concepts, `skos:closeMatch` for sufficiently similar concepts whose scope requires a distinction, and `skos:relatedMatch` for an associative relationship. These choices are editorial assessments documented for each category. The [W3C SKOS Reference](https://www.w3.org/TR/skos-reference/#mapping) defines the mapping properties.

An empty mapping field means that no equivalent entry was identified in the checked VID. It does not establish that the category is absent from other diplomatic or legal vocabularies.

| Corpus category | VID entry | Declared relationship |
|---|---|---|
| *capitulum* | — | No equivalent identified |
| *defensio* | 220 | `skos:relatedMatch` |
| *fideiussio* | 221b | `skos:closeMatch` |
| *iuramentum* | 218 | `skos:exactMatch` |
| *obligatio* | 219 | `skos:exactMatch` |
| *pactum revocationis* | — | No equivalent identified |
| *precarium* | — | No equivalent identified |
| *prorogatio iurisdictionis* | 235 | `skos:closeMatch` |
| *renuntiatio* | 222 | `skos:exactMatch` |
| *restitutio cum melioratione* | 239 | `skos:exactMatch` |
| *restitutio in integrum* | 238 | `skos:exactMatch` |
| *restrictio alienationis* | — | No equivalent identified |
| *sanctio negativa* | 237 | `skos:exactMatch` |
| *stipulatio* | — | No equivalent identified |

Six categories have exact mappings; two have close mappings; one has an associative mapping; five retain a corpus-specific definition without a declared VID mapping.

### Scope of the VID mappings

- **Fideiussio:** VID 221a–d describe different forms of third-party guarantee. In both annotated instances, the guarantor assumes a personal obligation and takes an oath on the Gospels. The repertoire links this category to VID 221b, the closest specific entry, through `skos:closeMatch`.
- **Defensio:** VID 220 concerns assets assigned as security. The corpus category concerns defence against claims and eviction. Their relationship is associative.
- **Prorogatio iurisdictionis:** VID 235 concerns the selection of competent courts. The corpus formulations accept or extend the authority of the documenting officials and may also mention their *officium*. The declared close mapping preserves the functional correspondence and this difference in scope.
- **Capitulum and precarium:** VID 200 concerns an article or division of a text, while VID 448 concerns the early medieval act of *precaria/prestaria*. Neither is used as an equivalent for the categories annotated here.

## Category definitions and recognition criteria

The CSV contains the complete mapping rationale and a representative excerpt for each category. The following definitions and criteria correspond to its fields.

### capitulum

ANNIE label: `CAPITULUM`.

Clause recording the assembly and collegial action of a monastic community for the transaction documented in the act.

Include formulations establishing the assembled community as a chapter acting collectively, including its convocation and the constitution of the assembly for the business at hand.

Distinguish the assembled community from an article or textual division called capitulum, and from a simple mention of a monastery or its members.

Representative example: `BCSL_22`, `text[1681:1829]`; example identifier `BCSL_22-CAPITULUM-1681-1829` in `clause_examples.csv`.

### defensio

ANNIE label: `DEFENSIO`.

Clause by which a party undertakes to defend the transferred or granted property, right, or benefit against third-party claims and eviction.

Include undertakings to defendere, antistare, or otherwise defend the transferred object or right ab omnibus hominibus, together with associated provisions on eviction where present.

Distinguish this warranty from the general pledge of assets securing performance and from a separate third party's assumption of the warranty obligation.

Representative example: `BCSL_18`, `text[3915:4216]`; example identifier `BCSL_18-DEFENSIO-3915-4216` in `clause_examples.csv`.

### fideiussio

ANNIE label: `FIDEJUSSIO`.

Clause by which a third party assumes a personal obligation to secure the principal party's performance, including defence against third-party claims and eviction.

Include a third party's express assumption of the burden of defence and the binding of that party, their assets, or their successors as recorded in the act. In both BCSL 18 and BCSL 21, the guarantor also takes the oath recorded in the separate IURAMENTUM passage.

Distinguish this additional obligation from the principal party's own warranty and from the mere presence of a husband or mundualdus without an express guarantee.

Representative example: `BCSL_18`, `text[4217:4745]`; example identifier `BCSL_18-FIDEJUSSIO-4217-4745` in `clause_examples.csv`.

### iuramentum

ANNIE label: `IURAMENTUM`.

Clause recording an oath to fulfil and observe the provisions of the act, normally sworn on the Gospels.

Include explicit declarations of an oath securing observance of the transaction, including references to the Gospels being physically touched.

Distinguish the oath clause from an ordinary promise, a stipulation, and references to an oath occurring only in the narrative of another event.

Representative example: `BCSL_14`, `text[12075:12483]`; example identifier `BCSL_14-IURAMENTUM-12075-12483` in `clause_examples.csv`.

### obligatio

ANNIE label: `OBLIGATIO`.

Clause binding a party and their property, and where specified their heirs or successors, to the performance of the act.

Include commitments binding the party's present or future assets to performance, including associated pledges and enforcement provisions within the annotated passage.

Distinguish the principal obligation from a separately assumed third-party guarantee, a defence against eviction, and the penalty imposed for breach.

Representative example: `BCSL_14`, `text[8425:9720]`; example identifier `BCSL_14-OBLIGATIO-8425-9720` in `clause_examples.csv`.

### pactum revocationis

ANNIE label: `PACTUM_REVOCATIONIS`.

Clause allowing the purchaser or purchasing monastery to return the acquired annual rent, requiring the sellers to reimburse the purchase price and take back the rent with the associated ownership and possession.

Include the optional return and reimbursement arrangement expressly agreed in BCSL 20, including its provisions for rent already received.

Distinguish this contractual option from forfeiture following non-performance, restitution including improvements, and the revocation of an authentication device such as a seal.

Representative example: `BCSL_20`, `text[6218:7054]`; example identifier `BCSL_20-PACTUM_REVOCATIONIS-6218-7054` in `clause_examples.csv`.

### precarium

ANNIE label: `PRECARIUM`.

Clause recording that the transferor continues to hold the transferred property or right precario nomine on behalf of the purchaser, with several formulations specifying the purchaser's acquisition of corporeal possession or power of revocation.

Include express declarations of continued holding precario or precario nomine following the transfer, read in their possessory context.

Distinguish this possessory clause from the early medieval act called precaria, from a grant subject to annual rent, and from a generic reference to possession.

Representative example: `BCSL_14`, `text[7318:7514]`; example identifier `BCSL_14-PRECARIUM-7318-7514` in `clause_examples.csv`.

### prorogatio iurisdictionis

ANNIE label: `PROROGATIO_IURISDICTIONIS`.

Clause by which an actor consents to the competence of the documenting officials and voluntarily submits to or extends their jurisdiction, sometimes together with their office, often declaring prior awareness of not ordinarily being subject to them.

Include formulations using prorogare, submittere, or subicere for the actor's acceptance of the officials' authority. Explicit declarations of non-subjection and references to officium vary across the annotated passages.

Distinguish the positive act of submission or extension from a mere reference to the ecclesiastical forum, a waiver of a legal exception, and a generic mention of an official's jurisdiction.

Representative example: `BCSL_29`, `text[1421:1730]`; example identifier `BCSL_29-PROROGATIO_IURISDICTIONIS-1421-1730` in `clause_examples.csv`.

### renuntiatio

ANNIE label: `RENUNTIATIO`.

Clause by which a party waives in advance legal exceptions, remedies, or privileges that could invalidate the transaction or prevent or delay its performance.

Include special and general waivers of exceptions and remedies, including a waiver of the beneficium restitutionis in integrum where it appears within the renunciation.

Distinguish the waiver of a restitution remedy from an operative clause requiring the return of property following non-performance.

Representative example: `BCSL_14`, `text[10697:12074]`; example identifier `BCSL_14-RENUNTIATIO-10697-12074` in `clause_examples.csv`.

### restitutio cum melioratione

ANNIE label: `RESTITUTIO_CUM_MELIORATIONE`.

Clause providing for the return or reversion of the property together with improvements made to it, following non-performance of the contractual obligations.

Include reversion clauses expressly retaining improvements or benefits made to the property, including formulations referring to meliorationes or beneficium in that sense.

Distinguish restitution including improvements from restitution without such an express provision and from a clause merely requiring cultivation or repairs.

Representative example: `BCSL_25`, `text[3639:4371]`; example identifier `BCSL_25-RESTITUTIO_CUM_MELIORATIONE-3639-4371` in `clause_examples.csv`.

### restitutio in integrum

ANNIE label: `RESTITUTIO_IN_INTEGRUM`.

Clause providing for the return or recovery of the property following non-performance of the contractual obligations, such as failure to pay rent or maintain cultivation.

Include provisions linking non-performance to forfeiture of the concession and the grantor's recovery or re-entry into the property, in the diplomatic sense of VID 238.

Distinguish this operative restitution clause from renunciation of the beneficium restitutionis in integrum and from the separately annotated return expressly including improvements.

Representative example: `BCSL_22`, `text[8684:9370]`; example identifier `BCSL_22-RESTITUTIO_IN_INTEGRUM-8684-9370` in `clause_examples.csv`.

### restrictio alienationis

ANNIE label: `RESTRICTIO_ALIENATIONIS`.

Clause regulating the recipient's subsequent transfer of granted property by reserving rent and contractual conditions, excluding specified recipients, or imposing conditions on alienation.

Include qualified permissions to sell, exchange, donate, bequeath, or otherwise transfer the property when they preserve rent and contractual conditions and restrict recipients or require prior recourse to the granting institution.

Distinguish restrictions on the recipient's later disposition from the present act of transfer, institutional consent to that act, and a generic prohibition of alienation in another legal context.

Representative example: `BCSL_25`, `text[3328:3638]`; example identifier `BCSL_25-RESTRICTIO_ALIENATIONIS-3328-3638` in `clause_examples.csv`.

### sanctio negativa

ANNIE label: `SANCTIO_NEGATIVA`.

Clause securing performance of the act by prescribing a penalty against a party who breaches or obstructs its provisions.

Include the penalty, its trigger, and associated provisions on payment, beneficiaries, or the continued force of the act within the annotated passage.

Distinguish the sanction for non-compliance from a general obligation, an oath to perform, and an operative return of the property.

Representative example: `BCSL_14`, `text[9721:10696]`; example identifier `BCSL_14-SANCTIO_NEGATIVA-9721-10696` in `clause_examples.csv`.

### stipulatio

ANNIE label: `STIPULATIO`.

Formula expressly recording the formal stipulation that gives force to a promise, obligation, guarantee, or pact, often together with guadia.

Include express formulaic invocations of stipulatio as the formal mechanism accompanying a commitment, such as per guadiam et stipulacionem or a pact described as stipulacione vestitum.

Distinguish an annotated stipulation formula from the mere description of a recipient as stipulans and from the substantive obligation that the formula accompanies.

Representative example: `BCSL_18`, `text[3734:3786]`; example identifier `BCSL_18-STIPULATIO-3734-3786` in `clause_examples.csv`.

## Corpus identifiers and character offsets

The JSONL contains `text` and `spans` fields but no explicit BCSL document identifiers. The association between records and document identifiers follows the notebook's `DOC_IDS` list. The complete one-based record order is retained in `source_metadata.json` and `clause_examples.csv`.

All examples reproduce the source strings exactly, including transcription signs, spacing, apparent errors and soft hyphens. Offsets refer to the decoded Unicode `text` field of the individual record, using zero-based, start-inclusive and end-exclusive positions. They do not refer to positions in the JSONL file's encoded bytes. RDF examples use the [W3C Text Position Selector](https://www.w3.org/TR/annotation-model/#text-position-selector) to record those ranges.

The RDF document resources identify the text fields of those records. Their `dct:source` points to the JSONL, and `schema:position` records the one-based record index. Character selectors apply to the individual text resource.

All 135 source clause annotations are retained. Two `STIPULATIO` ranges in BCSL 18 share their start position and are nested: `[4666, 4745)` and `[4666, 4712)`. Both remain identifiable in the export. They represent source annotations, not two independent clauses. This overlap does not change document-level presence/absence.

## CSV conventions

CSV files use UTF-8, comma separators, a single header row and quoted fields where required. No text normalization or label replacement is applied. The ANNIE notation `FIDEJUSSIO` is preserved; the preferred Latin label is *fideiussio*, with *fidejussio* as an alternate spelling.

`clause_repertoire.csv` contains: `concept_uri`, `annie_label`, `pref_label_la`, `pref_label_en`, `definition_en`, `inclusion_en`, `exclusion_en`, `vid_mapping`, `vid_id`, `vid_uri`, `mapping_rationale_en`, `example_id`, `example_document`, `example_start`, `example_end`, and `example_text`.

`clause_examples.csv` contains: `example_id`, `example_uri`, `concept_uri`, `annie_label`, `document_id`, `document_uri`, `jsonl_record_1based`, `start`, `end`, `text`, and `document_text_sha256`.

## Namespace and publication path

The intended location is the `vocabulary/` directory of [GiuConso/Formulas_semantics](https://github.com/GiuConso/Formulas_semantics).

Concept URIs use `https://raw.githubusercontent.com/GiuConso/Formulas_semantics/main/vocabulary/clause_repertoire.ttl#`, followed by a category identifier. Example and document resources use the corresponding `clause_examples.ttl#` namespace. Both serializations of each graph use the same identifiers. Retain these filenames and paths when uploading the package.

The main branch carries the current version. The metadata identifies the VID source commit and the corpus content used for this release. The dataset content hash is calculated from the ordered JSON records with `json.dumps(records, ensure_ascii=False, sort_keys=True, separators=(',', ':'))`, encoded as UTF-8. Individual text hashes are calculated directly from each record's text, encoded as UTF-8.

## Validation

With `BCSL_Evora.jsonl` in the repository root, run:

```bash
python vocabulary/validate_repertoire.py
```

Alternatively, supply the dataset location with `--dataset PATH`.

The script checks the RDF/XML documents, equivalence with the single-triple-per-line Turtle subset used here, the fourteen concepts and their preferred labels and notations, CSV/RDF consistency, all 135 annotation ranges and excerpts, and the corpus content hash. It uses the Python standard library. It does not perform unrestricted OWL reasoning or replace the documented scholarly assessment of the mappings.
