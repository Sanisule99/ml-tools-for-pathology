# Learning Series #4 — Pathology-Linked Variant Explorer (TCGA-like MAF)

**Goal:** Given a mutation table (MAF-like), compute per-gene mutation frequencies, test associations with pathology variables (grade/subtype), visualize a compact oncoplot-style heatmap, and optionally link to survival.

> Pathology angle: connects actionable variants (EGFR, KRAS, TP53) to histologic features and clinical outcomes.

## Files
- `LS4_Pathology_Linked_Variant_Explorer.ipynb` — main Python notebook.
- `example_maf.csv` — toy MAF-like file.
- `example_clinical.csv` — toy clinical annotations.
- `README.md` — this file.

## Quick Start
```bash
pip install pandas numpy matplotlib scipy lifelines
jupyter notebook LS4_Pathology_Linked_Variant_Explorer.ipynb
```

## Outputs
- Top mutated genes table
- Bar plot of mutation frequency
- Oncoplot-style heatmap (samples × top-N genes)
- Chi-square/Fisher tests for grade/subtype associations
- Optional gene-level survival analysis (KM + Cox)

> Authored: 2025-08-29
