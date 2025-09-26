# Learning Series #12 — Pathology Meets Foundation Models

**Goal:** Introduce vision/language foundation models (CLIP, SAM, etc.) for pathology and provide a safe starter script to test zero-shot classification on tiles.

## Contents
- `clip_zero_shot_skeleton.py`: A runnable skeleton using OpenCLIP. Requires internet the first time to download weights.
- `notes.md`: Talking points, pitfalls, and how to adapt to histology.

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
# Place a few images in data/demo/
python clip_zero_shot_skeleton.py --data_dir data/demo --labels "lymphocyte, eosinophil, background"
```
