# Learning Series #9 — Explainability Beyond Heatmaps

**Goal:** Compare Grad-CAM, Integrated Gradients, and SHAP; discuss when each is appropriate and pitfalls. This repo provides a runnable skeleton and a synthetic demo so you can plug in your own model/images.

## Contents
- `explainability_skeleton.py`: shows API stubs for loading a model and computing 3 explanation types.
- `synthetic_demo.py`: trains a tiny CNN on synthetic shapes and visualizes saliency to illustrate pros/cons without real data.
- `figures/`: output directory.

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python synthetic_demo.py
```
Then replace stubs in `explainability_skeleton.py` with your model and data loaders.
