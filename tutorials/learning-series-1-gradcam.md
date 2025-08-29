# 🧠 Learning Series #1: What Is Grad-CAM in Pathology?

## 🔍 The Concept
**Grad-CAM** (Gradient-weighted Class Activation Mapping) is a technique that helps us understand *why* a convolutional neural network (CNN) made a certain prediction — by highlighting the most important regions of an image that influenced the output.

In pathology, this means we can visualize which areas of an H&E slide “convinced” the model that it’s looking at, say, a blast vs a lymphocyte.

## 🔬 Why It Matters in Pathology
- Enhances **trust** in AI predictions by making models more interpretable
- Identifies **morphologic features** that align with pathologists' intuition
- Aids **education** by letting trainees visualize decision-making regions
- Helps detect **model bias** (e.g., overreliance on staining artifacts)

## 💡 Common Use Cases
- Bone marrow differential classification
- Tumor subtype detection
- Mitotic figure recognition

## 🧰 Tools You Can Try
- [`Grad-CAM for EfficientNet`](https://github.com/Sanisule99/ml-tools-for-pathology/blob/main/tutorials/CNA_Burden_Recurrence_Predictor.ipynb)
- `torchcam`, `captum`, and `keras-vis` for plug-and-play integrations

## 📚 Learn More
- Selvaraju et al., 2017: [Grad-CAM Paper](https://arxiv.org/abs/1610.02391)
- Slideflow implementation: [slideflow.dev](https://slideflow.dev)

## 🗂️ Coming Next
> **Learning Series #2: What Makes a Good Marker for Tissue-of-Origin Classification?**
