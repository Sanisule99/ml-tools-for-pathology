# 🧬 Case Study: Selecting Tissue-Specific IHC Markers with GTEx Data

## 🎯 Objective
To demonstrate how the `ihc_marker_selector_model.ipynb` tool can be used to identify tissue-specific immunohistochemical (IHC) markers using GTEx expression data.

## 🔍 Dataset
- Source: GTEx v8 RNA-Seq expression (TPM)
- Data Types:
  - Median gene expression across tissues
  - Annotated tissue types

## 🧠 Tool Used
- [ihc_marker_selector_model.ipynb](../decision-support/ihc_marker_selector_model.ipynb)

## 📊 Results Summary

For **Liver** tissue:
| Gene | Specificity Score |
|------|-------------------|
| ALB  | 45.1              |
| HP   | 32.7              |
| TF   | 25.3              |

For **Prostate** tissue:
| Gene  | Specificity Score |
|-------|-------------------|
| KLK3  | 38.9              |
| ACPP  | 29.5              |
| NKX3-1| 20.2              |

## 💡 Interpretation

- The GTEx-based tool correctly prioritized canonical IHC markers for common tissue types.
- Supports building or validating diagnostic panels for pathology workflows.
- Can help in ambiguous biopsy cases where lineage determination is unclear.

## 🔄 How to Adapt
- Upload new expression matrix (e.g., from local or rare tumor dataset)
- Customize specificity score threshold for marker filtering
- Extend to subtype-specific marker discovery

## 🧑‍⚕️ Pathologist Takeaway

This tool provides a data-driven approach to selecting IHC markers that are maximally specific to a tissue of interest — ideal for supplementing or cross-validating panels in diagnostic pathology, especially in cases involving metastases or tumors of unknown primary.

