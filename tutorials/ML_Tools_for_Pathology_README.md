# Machine Learning Tools for Pathology

This repository contains practical workflows that demonstrate how machine learning can support diagnostic pathology and pathology informatics.  
Each notebook is designed to be accessible for trainees, researchers, and clinicians interested in computational pathology.

---

## 🔬 What’s Inside
- **Copy Number Alteration (CNA) Burden Analysis**  
  Pan-cancer pipeline using MSK-CHORD to explore CNA burden, histologic grade, and survival outcomes.  
  ![CNA burden vs survival](figures/cna_survival.png)

- **Tissue-of-Origin Classifier**  
  Integrated GTEx + TCGA RNA expression data for calibrated tumor classification.  
  ![Confusion matrix](figures/confusion_matrix.png)

- **Explainable AI for Cytomorphology**  
  Bone marrow cytology classifier with SHAP & Grad-CAM visualizations.  
  ![SHAP overlays](figures/shap_grid.png)

---

## 📘 Why This Matters
These workflows illustrate how **bioinformatics and pathology intersect**:  
- Pathologists can explore omics data alongside morphology.  
- Models are designed to be interpretable and reproducible.  
- Supports diagnostic reasoning, not just black-box predictions.

---

## ▶️ How to Use
1. Clone the repo:  
   ```bash
   git clone https://github.com/USERNAME/ml-tools-for-pathology.git
   cd ml-tools-for-pathology
   ```
2. Install requirements:  
   ```bash
   pip install -r requirements.txt
   ```
3. Open Jupyter notebooks in `/notebooks`.

---

## 📂 Repo Structure
```
/notebooks
  ├── cna_survival_analysis.ipynb
  ├── tissue_of_origin_classifier.ipynb
  └── cytomorphology_ai_explainability.ipynb
/figures
/requirements.txt
```

---

## ✨ Residency Relevance
This repo highlights how I integrate **molecular data, AI, and diagnostic pathology** to build practical, interpretable workflows that advance patient care.
