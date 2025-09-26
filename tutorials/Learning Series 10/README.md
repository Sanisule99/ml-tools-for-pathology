# Learning Series #10 — Survival Analysis Meets Pathology AI

**Goal:** Show how image-derived features (or any embeddings) can be linked to outcomes using Kaplan–Meier curves and Cox proportional hazards.

## What this repo includes
- `survival_link_demo.py`: Simulates features + survival times, runs KM curves and Cox PH model, and outputs plots + model summary.
- Works offline with synthetic data.

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python survival_link_demo.py
```
Artifacts in `outputs/`: `km_curves.png`, `cox_summary.txt`.
