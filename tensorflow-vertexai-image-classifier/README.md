# 🧠 TensorFlow + Vertex AI Image Classifier  
**End-to-end machine learning pipeline using TensorFlow, Google Cloud Storage, and Vertex AI**

---

## 📋 Overview
This project demonstrates a complete MLOps workflow:
1. **Train** a Convolutional Neural Network (CNN) on the [Fashion-MNIST dataset](https://github.com/zalandoresearch/fashion-mnist) using TensorFlow.
2. **Export** the trained model as a TensorFlow SavedModel.
3. **Upload** artifacts to **Google Cloud Storage (GCS)**.
4. **Deploy** the model to **Vertex AI** for real-time serving.
5. **Predict** live images via Vertex AI Endpoints using Python or REST API.

It’s designed for **Customer Engineer / AI Engineer portfolios** — readable, reproducible, and cloud-ready.

---

## ⚙️ Tech Stack

| Component | Technology |
|------------|-------------|
| Language | Python 3.11 |
| Framework | TensorFlow 2.15 (Keras 3 compatible) |
| Cloud | Google Cloud Platform (Vertex AI, Cloud Storage) |
| Serving | Vertex AI Prediction Service |
| Tools | google-cloud-aiplatform, pillow, numpy, matplotlib, scikit-learn |

---

## 🧩 Architecture

```
 ┌──────────────────┐
 │ TensorFlow Model │  ← train.py (local)
 └────────┬─────────┘
          │ export (SavedModel)
          ▼
 ┌──────────────────────────┐
 │ Google Cloud Storage (GCS)│
 └────────┬─────────────────┘
          │ deploy
          ▼
 ┌──────────────────────────────┐
 │ Vertex AI Endpoint (Online) │
 └────────┬─────────────────────┘
          │ predict (REST/Python)
          ▼
      Real-time Predictions
```

---

## 🚀 Quickstart

### 1️⃣ Environment Setup
```bash
python -m venv .venv
.\.venv\Scriptsctivate
pip install -r requirements.txt
gcloud auth application-default login
```

### 2️⃣ Train Model
```bash
python src/train.py --epochs 1 --output_dir artifacts/saved_model_v4
```
✅ Output: `artifacts/saved_model_v4/saved_model.pb`

---

### 3️⃣ Upload to GCS
```bash
gsutil -m rsync -r artifacts/saved_model_v4 gs://lakshmi-vertex-models-123/models/v4/saved_model
```

---

### 4️⃣ Deploy to Vertex AI
Ensure `src/deploy_vertex.py` includes:
```python
DEFAULT_SERVING_IMAGE = "us-docker.pkg.dev/vertex-ai/prediction/tf2-cpu.2-15:latest"
```
Then deploy:
```bash
python src/deploy_vertex.py --model_uri gs://lakshmi-vertex-models-123/models/v4/saved_model --display_name tf-cnn-fmnist-v4
```

✅ Output:
```
→ Uploading model tf-cnn-fmnist-v4 ...
✅ Deployed! Endpoint ID: 7669145280784105472
```

---

### 5️⃣ Run Prediction
```bash
python src/predict_vertex.py --endpoint_id 7669145280784105472 --image_path assets/sample_images/test.png
```

✅ Output:
```
→ Sending image test.png to endpoint
✅ Predicted: sandal (confidence: 0.93)
```

---

### 6️⃣ REST API (optional)
```bash
curl -X POST   -H "Authorization: Bearer $(gcloud auth print-access-token)"   -H "Content-Type: application/json"   https://us-central1-aiplatform.googleapis.com/v1/projects/lakshmi-ml-demo/locations/us-central1/endpoints/7669145280784105472:predict   -d @request.json
```

---

## 📈 Results

| Metric | Value (1 epoch) |
|---------|-----------------|
| Accuracy | ~0.89 |
| Precision / Recall | Varies by class |
| Classes | 10 Fashion categories |
| Framework | TensorFlow CNN with 2 Conv2D + Dense layers |

---

## 🧠 Model Summary

| Layer | Output Shape | Params |
|-------|---------------|--------|
| Conv2D (32 filters, 3x3) | (28,28,32) | 320 |
| MaxPooling2D | (14,14,32) | 0 |
| Conv2D (64 filters, 3x3) | (14,14,64) | 18496 |
| MaxPooling2D | (7,7,64) | 0 |
| Flatten | (3136) | 0 |
| Dense (128) | (128) | 401536 |
| Dropout (0.3) | (128) | 0 |
| Dense (10, softmax) | (10) | 1290 |

---

## 🗂️ Folder Structure

```
tensorflow-vertexai-image-classifier/
 ┣ src/
 ┃ ┣ model.py
 ┃ ┣ train.py
 ┃ ┣ deploy_vertex.py
 ┃ ┣ predict_vertex.py
 ┣ artifacts/
 ┃ ┗ saved_model_v4/
 ┣ assets/
 ┃ ┣ sample_images/
 ┃ ┗ plots/
 ┣ requirements.txt
 ┣ README.md
 ┗ .env.example
```

---

## 🧹 Cleanup
```bash
gcloud ai endpoints delete 7669145280784105472 --region us-central1 --quiet
```

---

## 💡 Learnings
- TensorFlow models must include a **`serving_default` signature** for Vertex AI.
- Always use a **supported serving container** (`tf2-cpu.2-15` or `tf_opt-cpu.2-14`).
- Exporting a `tf.Module` wrapper ensures all variables are tracked correctly.
- Vertex AI handles **autoscaling, versioning**, and **real-time predictions** seamlessly.

---

## 👩‍💻 Author
**Lakshmi Achary**  
AI / ML Customer Engineer Portfolio Project  
📧 [lakshmirachary8@gmail.com](mailto:lakshmirachary8@gmail.com)  
🌐 [github.com/lacharydev](https://github.com/lacharydev)

---

> “Developed and deployed a TensorFlow CNN image classifier on Google Cloud Vertex AI with real-time prediction endpoint, integrating GCS and REST API for inference.”
