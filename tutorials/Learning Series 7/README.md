# Learning Series #7 — How Do Pathology Models Handle Small Datasets?

**Goal:** Show why small datasets cause overfitting in pathology AI and how to improve results with **transfer learning + augmentation** (and optional MixUp).  
Works with any folder of images arranged like `root/class_name/image.jpg`.

## Why this matters
- Pathology datasets are often **small** and **imbalanced**.
- Naive training → **overfitting** and poor generalization.
- Simple fixes (transfer learning, augmentation) can make small data go much further.

## Two runnable scripts
1) `baseline_small_dataset.py` — trains a small CNN from scratch on a tiny subset to illustrate overfitting.
2) `transfer_augment_small_dataset.py` — uses pretrained ResNet18 + strong augmentations (+ optional MixUp) to improve performance.

## Quickstart

```bash
# (optional) create env
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Put your data here (or update DATA_DIR in config.yaml)
# data/tiny_demo/<classA>/*.png
# data/tiny_demo/<classB>/*.png
# ...

# Baseline
python baseline_small_dataset.py --data_dir data/tiny_demo --epochs 15 --img_size 224

# Transfer + Augmentation
python transfer_augment_small_dataset.py --data_dir data/tiny_demo --epochs 15 --img_size 224 --mixup_alpha 0.2
```

Outputs (per run) land in `outputs/`:
- `metrics.json` (train/val curves + final metrics)
- `confusion_matrix.png`
- `learning_curves.png`
- `example_augs.png` (for transfer script)

## Tips for Pathology Datasets
- Keep **validation set** patient-disjoint if possible.
- Use **color jitter / stain-like augmentation**; consider stain normalization if you have reference slides.
- Try **weak supervision** (MIL/CLAM) for WSI-level labels.
- Consider **synthetic tiles** (GAN/diffusion) cautiously for rare classes.

## Citeable talking points (for your post)
- Small data → high variance; transfer learning reduces sample complexity.
- Augmentations increase the effective dataset size and improve robustness.
- MixUp and label-smoothing regularize decision boundaries with few examples.
