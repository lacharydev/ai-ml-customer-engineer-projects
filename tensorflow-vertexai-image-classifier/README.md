# 🧠 TensorFlow + Vertex AI Image Classifier

A simple end-to-end pipeline:
- Train a CNN on Fashion-MNIST using TensorFlow
- Export a SavedModel
- Upload to Google Cloud Storage
- Deploy on Vertex AI Endpoint
- Run real-time predictions via Python or REST API

---

## 🔧 Tech Stack
- TensorFlow 2.15
- Google Cloud Vertex AI
- Google Cloud Storage
- Python 3.11
- Pillow, NumPy, Matplotlib

---

## 🧩 Project Flow
1. **Train model**
   ```bash
   python src/train.py --epochs 1 --output_dir artifacts/saved_model_v4
