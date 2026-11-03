# Formulas and Semantics in Digital Diplomatics

Research data and analysis notebook accompanying the paper *Formulas and Semantics in Digital Diplomatics* by Giuseppe Consolo, Tamás Kovács, and Georg Vogeler (University of Graz).

## Corpus

The corpus comprises sixteen notarial charters dated between 1393 and 1486, preserved in the Biblioteca Comunale “Sabino Loffredo” in Barletta (BCSL).

## Repository contents

- `BCSL_Evora.jsonl`: human-validated ANNIE annotations, preserving each document’s text and the labels and character offsets of its annotated spans.
- `Evora_ANNIE_FLAME_Integration.ipynb`: Jupyter notebook integrating ANNIE clause annotations, FLAME similarities, and contextual metadata.
- `Output_Default_Flame.zip`: FLAME outputs required by the notebook, including the similarity matrix and reports.

## Analysis

The notebook derives document-level presence/absence profiles for fourteen clause categories and compares their Jaccard similarities with the cosine similarities produced by FLAME. The comparison uses Spearman’s correlation and a document-label permutation test with 10,000 random permutations and a fixed random seed (42).

## Running the notebook

Keep the notebook, JSONL dataset, and FLAME ZIP archive in the same working directory. Run the notebook cells in order.

Required Python packages: NumPy, pandas, SciPy, and Matplotlib.

When using Google Colab, upload both input files to the session’s working directory before running the analysis.
