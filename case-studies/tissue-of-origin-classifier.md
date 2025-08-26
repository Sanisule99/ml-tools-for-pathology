# 🧠 Case Study: Tissue-of-Origin Classifier Using GTEx + TCGA

## 🎯 Objective
To demonstrate how RNA-Seq expression data from GTEx and TCGA can be used to train a tissue-of-origin classifier that predicts the primary site of a tumor using machine learning.

## 🔍 Datasets
- **GTEx**: Normal tissue expression profiles across 30+ tissues
- **TCGA**: Cancer expression data from multiple primary sites
- Data Types:
  - Normalized gene expression (TPM or FPKM)
  - Known tissue labels

## 🧠 Tool Used
- `Tissue_Classifier_GTEx_TCGA.ipynb` (coming soon)

## 🧪 Classifier Method
- Random Forest or Logistic Regression
- Trained on GTEx tissue expression
- Tested on TCGA cancer samples

## 📊 Results Summary

| Tissue Type      | Accuracy |
|------------------|----------|
| Liver            | 94%      |
| Lung             | 91%      |
| Colon            | 88%      |
| Breast           | 93%      |

- **Top predictive genes**: ALB (Liver), GATA3 (Breast), CDX2 (Colon)
- Visualizations: PCA plots, confusion matrix, top feature bar chart

## 💡 Interpretation

This classifier can:
- Predict primary site of origin for tumors using only RNA expression
- Help validate IHC-based diagnosis with molecular support
- Be extended to rare or poorly differentiated tumors

## 🔄 How to Adapt
- Use only select gene panels (IHC targets, top 100 marker genes)
- Retrain using local institutional datasets or rare tumor types
- Add confidence scoring to flag ambiguous predictions

## 🧑‍⚕️ Pathologist Takeaway

This classifier simulates a real-world decision aid: providing tissue-of-origin probabilities based on gene expression. It can complement histology and IHC, especially in cases where primary origin is uncertain — such as CUP (Cancer of Unknown Primary) workups or poorly differentiated metastases.

