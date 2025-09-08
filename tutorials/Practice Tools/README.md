# Learning Series #3 — Survival & Prognostic Biomarker Tools (TCGA)

This mini-project shows how to evaluate prognostic biomarkers using public cancer datasets (e.g., TCGA).
It walks through Kaplan–Meier curves and Cox proportional-hazards models given a gene's expression.

> **Why this matters for pathology:** Survival analysis connects molecular markers (e.g., PD-L1/CD274, GATA3, TTF1) to outcomes.
> This bridges bioinformatics and diagnostic pathology, and is a great talking point during interviews.

---

## 📁 What's here

- `LS3_Survival_Prognostic_Biomarkers.ipynb` — main tutorial notebook.
- `example_clinical.csv` — toy clinical data template (OS time/status + grade/subtype).
- `example_expression.csv` — toy gene expression matrix template (rows=samples, cols=genes).
- `README.md` — this file.

---

## 🧪 Quick Start (local)

1. **Create/activate** a Python 3.10+ environment (conda or venv is fine).
2. Install packages:
   ```bash
   pip install pandas numpy lifelines matplotlib scipy statsmodels
   ```
3. Launch the notebook:
   ```bash
   jupyter notebook LS3_Survival_Prognostic_Biomarkers.ipynb
   ```

> If you'd rather use R, add a sibling R Markdown using `survival` and `survminer`; structure mirrors this notebook.

---

## 📂 Expected inputs

- **Clinical** (`example_clinical.csv` columns):
  - `sample_id` — unique ID matching expression matrix row names
  - `OS_time` — overall survival time (days or months; specify in notebook)
  - `OS_event` — 1 = death/event, 0 = censored
  - Optional: `age`, `sex`, `grade`, `stage`, `subtype`, etc.

- **Expression** (`example_expression.csv` format):
  - First column: `sample_id`
  - Other columns: gene symbols (e.g., `CD274`, `GATA3`, `TTF1` as `NKX2-1` in HGNC)

> You can export TCGA data via GDC (or cBioPortal/cBioPortalR) and reformat to this shape.

---

## 🔍 Analyses included

- Split patients by **high vs low gene expression** (median, tertiles, or custom cutoffs)
- Plot **Kaplan–Meier** survival curves with log-rank test
- Fit **Cox models** (univariable and multivariable)
- Optional: make a **forest plot** of hazard ratios across multiple markers
- Save publication-ready figures (PNG/SVG)

---

## 🧷 Typical use-cases

- Prognosis by **PD-L1 (CD274)** in LUAD
- Tissue markers like **TTF1 (NKX2-1)** or **GATA3**
- Immune signatures (e.g., CD8A) or proliferation markers (MKI67)

---

## 🧰 Repo integration

Recommended repo structure:
```
ML-Tools-for-Pathology/
  Learning-Series-3-Survival-Biomarkers/
    LS3_Survival_Prognostic_Biomarkers.ipynb
    example_clinical.csv
    example_expression.csv
    README.md
```
Then add, commit, and push:
```bash
git add Learning-Series-3-Survival-Biomarkers
git commit -m "Add LS3: Survival & prognostic biomarker tools (TCGA)"
git push origin main
```

---

## ✍️ Suggested write-up (README snippet)

*This notebook demonstrates a pragmatic, pathology-centered survival workflow.
Given a candidate marker (e.g., CD274), it shows how to form risk groups, generate KM curves,
and quantify risk using Cox PH — suitable for translational pathology posters or manuscripts.*

> Authored: 2025-08-29
