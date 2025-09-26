# Learning Series #11 — Synthetic Patients in Pathology (Without a GAN)

**Goal:** Discuss pros/cons of synthetic data and show safer augmentation strategies (MixUp/CutMix/style jitter) that work with tiny datasets.

## What this repo includes
- `augment_strategies_demo.py`: Applies MixUp/CutMix/color-jitter-style transforms to a small folder of images and saves before/after grids.
- Works with your own tiny dataset in `data/mini/<class>/*.png` (or any folder).

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
# Put a few images under data/mini/ClassA and ClassB (even 5-10 each)
python augment_strategies_demo.py --data_dir data/mini --img_size 224
```
Outputs: `mixup_grid.png`, `cutmix_grid.png`, `colorjitter_grid.png`.
