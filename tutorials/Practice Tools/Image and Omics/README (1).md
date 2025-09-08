# Learning Series #5 — Multi-Omics Mini-Pipeline (Expression + Mutations + Survival)

**Goal:** A compact, pathology-centered pipeline that merges **expression**, **mutations (MAF-like)**, and **clinical** data to produce:
- Survival curves (KM) and Cox models using combined molecular features
- Mutation burden and driver mutation indicators (e.g., TP53, KRAS, EGFR)
- Simple expression signatures (e.g., immune activation via CD8A/GZMB, PD-L1 via CD274)
- Publication-ready figures (PNG/SVG) and summary tables (CSV)

> **Pathology angle:** Demonstrates how molecular profiles augment morphologic diagnosis and risk stratification (e.g., PD-L1, TP53) with clear survival implications.

## Quick Start
```bash
pip install pandas numpy lifelines matplotlib scipy statsmodels
jupyter notebook LS5_MultiOmics_MiniPipeline.ipynb
```

> Authored: 2025-08-29
