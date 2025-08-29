# 🧠 Learning Series #2: What Makes a Good Marker for Tissue-of-Origin Classification?

## 🔍 The Concept
In molecular diagnostics and pathology, a **marker** is only useful if it helps you distinguish between tissues clearly and reliably. In RNA-based tissue classifiers, good markers are those genes whose expression is:

- **High in one tissue**
- **Low or absent in others**
- **Consistent across individuals**

## 🔬 Why It Matters in Pathology
- Accurate diagnosis of metastatic tumors
- Tissue-of-origin prediction for CUP (Cancer of Unknown Primary)
- Optimizing IHC panels based on molecular evidence

## 🧪 Features of a Good Marker
| Feature | Example | Why It Matters |
|--------|---------|----------------|
| High tissue specificity | ALB (Liver) | Easy to attribute source |
| Low background expression | GATA3 (Breast) | Avoids false positives |
| High expression level | CDX2 (Colon) | Reliable detection |
| Low inter-sample variability | KLK3 (Prostate) | Reduces uncertainty |

## 🧰 Tools You Can Try
- [`IHC Marker Selector using GTEx`](https://github.com/Sanisule99/ml-tools-for-pathology/blob/main/decision-support/ihc_marker_selector_model.ipynb)
- Human Protein Atlas (https://www.proteinatlas.org/)
- GTEx Portal (https://gtexportal.org/home/)

## 📚 Learn More
- Uhlen et al., 2015: *Tissue-based map of the human proteome* (Science)  
- GTEx Consortium: https://gtexportal.org/home/

## 🗂️ Coming Next
> **Learning Series #3: How Does a Tissue Classifier Actually Learn? (PCA, Genes, and Confusion)**
