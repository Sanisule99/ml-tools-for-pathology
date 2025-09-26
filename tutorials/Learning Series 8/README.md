# Learning Series #8 — Multi-Center Data & Batch Effects in Pathology

**Goal:** Demonstrate how site/stain differences create batch effects that confound models, and how simple corrections (e.g., ComBat) + color augmentation reduce spurious site clustering.

## What this repo includes
- `batch_effect_demo.py`: Simulates features with site-driven batch effects, visualizes PCA/UMAP before vs after correction.
- `figures/`: Generated plots.
- Works without any external dataset (uses synthetic data).

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python batch_effect_demo.py --n_sites 4 --n_classes 3 --n 600
```

Artifacts saved to `outputs/`:
- `pca_before.png`, `pca_after.png`
- `umap_before.png`, `umap_after.png`

## Notes for real datasets
- Use slide-level metadata to keep **patient-disjoint** splits across sites.
- Try **stain normalization** (e.g., Macenko) and **color jitter** during training.
- For tabular features, `sklearn`'s `StandardScaler` + `ComBat` (pycombat) can help.
