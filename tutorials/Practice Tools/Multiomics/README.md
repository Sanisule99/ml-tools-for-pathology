# Learning Series #6 — Image × Omics Fusion (MIL with Tile Features + Omics Labels)

**Goal:** Quick, pathology-centered demo that fuses **tile-level WSI features** with **omics-derived labels** (e.g., **CD274 high vs low**, **KRAS mutation status**) using **Attention-based Multiple Instance Learning (ABMIL)**.

This mini-project assumes you already have tile-level features (e.g., extracted via a CNN). We provide synthetic examples so the notebook runs out-of-the-box, plus hooks to plug in your real data.

---

## 📦 What's inside
- `LS6_Image_Omics_Fusion_ABMIL.ipynb` — end-to-end training & evaluation (PyTorch).
- `example_tiles.csv` — synthetic tile features with `tile_id`, `sample_id`, 64-dim features, and coords.
- `example_labels.csv` — per-sample labels including `CD274_expr`, `CD274_high`, `KRAS_mut`.
- `example_splits.csv` — train/val/test split.
- `README.md` — this file.

---

## 🔧 Quick start (local)
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install pandas numpy scikit-learn matplotlib
jupyter notebook LS6_Image_Omics_Fusion_ABMIL.ipynb
```

> CPU is fine for this demo. For real training, consider GPU and larger batches.

---

## 📥 Expected shapes

- **Tiles/features** (`example_tiles.csv`):
  - `tile_id`, `sample_id`, `x`, `y`, `f0`…`f63`
  - Each row = one tile feature vector (64-d). Tiles grouped by `sample_id` form a **bag**.

- **Labels** (`example_labels.csv`):
  - `sample_id`, `CD274_expr` (numeric), `CD274_high` (0/1), `KRAS_mut` (0/1)

- **Splits** (`example_splits.csv`):
  - `sample_id`, `split` ∈ `train|val|test`

---

## 🧪 What the notebook does
- Loads tile features and builds **MIL bags** per sample.
- Computes bag-level labels from omics (`CD274_high` or `KRAS_mut`).
- Trains a compact **ABMIL** model (Ilse et al., 2018 style) with attention pooling.
- Evaluates on val/test; reports **AUROC** and accuracy.
- Saves:
  - `outputs/metrics.json`
  - `outputs/roc_curve_{{label}}.png` and `.svg`
  - `outputs/loss_curve.png` and `.svg`
  - `outputs/attention_{{sample}}.csv` (tile-level attention for top-N samples)
  - `outputs/model.pt`

---

## 🔌 Plug in your real data
- Replace `example_tiles.csv` with your features. Required columns:
  - `sample_id`, tile feature columns (`f0..fD-1`), optional `x`,`y` for plotting.
- Replace/add labels in `example_labels.csv` with your **CD274** expression and **KRAS** mutation flags.
- Keep `example_splits.csv` or regenerate using your own logic (e.g., stratified split).

---

## ⚠️ Notes
- This is a didactic scaffold; for publications, add PHI-safe overlays, thorough cross-validation, and ablations.
- If your features are `.npy` per tile, write a small loader to aggregate into a CSV with the columns above.
- Charts are plain **matplotlib** with **single-figure plots** and **no explicit colors**, per your style rules.

> Authored: 2025-08-29
