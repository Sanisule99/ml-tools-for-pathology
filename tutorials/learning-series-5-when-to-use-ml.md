# 🧠 Learning Series #5: When Should Pathologists Use ML — and When Shouldn’t They?

## 🧬 The Concept
Machine learning is a powerful tool — but it’s not a replacement for pathology judgment. Knowing **when** to use ML (and when not to) is as important as the models themselves.

This series entry outlines appropriate use cases and red flags for integrating ML into diagnostic and research workflows.

## ✅ Good Times to Use ML
- **Quantifying patterns at scale** (e.g., mitotic figures, tile classification)
- **Supplementing expert review** (e.g., second opinion tools, flagging discordance)
- **Identifying subtle patterns** not easily seen by the eye (e.g., gene signatures, SCNA burden)
- **Educational augmentation** for training residents and students
- **Workflow triage** (e.g., sorting low- vs high-suspicion cases)

## 🚫 When NOT to Use ML
- As a **sole diagnostic tool** without interpretability or oversight
- When model performance is unvalidated for your population
- When **data distribution has shifted** (e.g., new stain protocols, scanner upgrades)
- If the task is already fast, cheap, and highly reliable by human review
- When you can't explain what the model is doing

## 🧠 Questions to Ask
- Does ML add value *beyond* what a pathologist can already do?
- Can I verify the model’s output with clinical logic?
- Is the model trained and validated on a population similar to mine?

## 🔍 Bonus Tip
Trust the model only as far as you can **audit the result** or **explain its failure**.

## 🧰 Tools That Make ML Safer
- `SHAP`, `Grad-CAM` → Interpretability
- `Fairlearn`, `CheckList` → Bias and robustness checks
- `streamlit` dashboards for human-in-the-loop ML

## 🗂️ Coming Next
> Learning Series #6: How Do You Calibrate an ML Model in Pathology?
