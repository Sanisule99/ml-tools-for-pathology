# 🧠 Learning Series #3: How Does a Tissue Classifier Actually Learn?

## 🧬 The Concept
A tissue-of-origin classifier uses **patterns in gene expression** to predict where a tumor came from. It learns by finding **statistical differences** in expression between tissues.

Under the hood, you're teaching a model to recognize that:
- ALB → Liver
- GATA3 → Breast
- TTF1 → Lung
- CDX2 → Colon

## ⚙️ What Happens During Learning?
1. **Input Data**: Expression matrix (genes x samples), each sample labeled with its tissue
2. **Feature Extraction**: The model identifies patterns — e.g., high CDX2 = Colon
3. **Training**: It builds a decision boundary to separate tissues based on gene values
4. **Evaluation**: Tested on unseen samples using metrics like accuracy or AUC

## 📊 Visual Tools to Understand This
- **PCA plots** – Shows how tissues cluster in 2D space
- **Confusion matrix** – Reveals what tissues are commonly misclassified
- **Top genes per class** – Understand what the model “relies” on

## 🧰 Tools You Can Try
- [`Tissue_Classifier_GTEx_TCGA.ipynb`](https://github.com/Sanisule99/ml-tools-for-pathology/blob/main/tutorials/Tissue_Classifier_GTEx_TCGA.ipynb)
- scikit-learn for classifiers (`RandomForest`, `LogReg`, `XGBoost`)
- `SHAP` and `feature_importances_` for interpretation

## 🧠 Model Tip
A good classifier is not just accurate — it's:
- **Interpretable**
- **Biologically plausible**
- **Generalizable to new cohorts**

## 🗂️ Coming Next
> **Learning Series #4: What Makes a Model “Fair” in Pathology AI?**
