# Misclassification Atlas: AI Meets Pathology

This project explores **where and why AI misclassifies pathology images**, and uses those errors as **teaching tools** for pathologists and trainees.  

---

## 🔬 Example
**AI Prediction:** Blast  
**True Diagnosis:** Promyelocyte  
![Example overlay](figures/blast_vs_promyelocyte.png)

**Why the AI got confused:**  
- High nuclear-cytoplasmic ratio  
- Fine chromatin overlap  

**How a pathologist resolves it:**  
- Azurophilic granules  
- Subtle nucleolar prominence

---

## 📘 Why This Matters
- **AI explainability**: Not just performance metrics, but understanding *why* models err.  
- **Educational value**: Misclassifications become case-based vignettes for pathology trainees.  
- **Residency preparation**: Shows ability to bridge computational insights with morphologic reasoning.

---

## ▶️ How to Use
- Browse `/notebooks/misclassification_cases.ipynb` for worked examples.  
- Explore `/figures` for curated overlays and explanatory notes.  

---

## 📂 Repo Structure
```
/notebooks
  └── misclassification_cases.ipynb
/figures
  ├── blast_vs_promyelocyte.png
  ├── lymphocyte_vs_plasma.png
  └── ...
```
