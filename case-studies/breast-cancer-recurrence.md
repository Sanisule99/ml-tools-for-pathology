# 🧪 Case Study: Predicting Breast Cancer Recurrence with SCNA Burden

## 🎯 Objective
To demonstrate how the `CNA_Burden_Recurrence_Predictor.ipynb` tool can be used to identify patients at higher risk for disease recurrence using somatic copy number alteration (SCNA) data and basic clinical features.

## 🔍 Dataset
- Source: TCGA Breast Cancer (BRCA) via cBioPortal
- Data Types:
  - Fraction Genome Altered (SCNA burden)
  - Mutation count
  - Clinical outcomes: Disease-Free Event (Yes/No)

## 🧠 Tool Used
- [CNA_Burden_Recurrence_Predictor.ipynb](../tutorials/CNA_Burden_Recurrence_Predictor.ipynb)

## 📊 Results Summary

| Feature                  | Importance |
|--------------------------|------------|
| Fraction Genome Altered | 0.39       |
| Endocrine Therapy        | 0.21       |
| Mutation Count           | 0.14       |

- **ROC AUC:** 0.81
- Patients with SCNA > 0.3 had significantly higher recurrence rates
- Visualized via boxplots and Random Forest feature importance

## 💡 Interpretation

This simple ML tool was able to:
- Stratify recurrence risk based on genomic instability
- Reinforce the clinical value of SCNA burden beyond classical staging
- Serve as a template for integrating genomic data in pathology QI efforts

## 🔄 How to Adapt
- Replace input with local institution data (e.g., OncoPanel + pathology reports)
- Apply to other cancer types with SCNA burden variation
- Customize thresholds for clinical alerts

## 🧑‍⚕️ Pathologist Takeaway

This workflow reflects a practical use case for integrating molecular data into real-world pathology decision-making — especially in breast cancer tumor boards or QI projects focused on endocrine therapy response.

