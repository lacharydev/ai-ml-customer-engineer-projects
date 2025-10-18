Image classification pipeline using TensorFlow + Google Cloud Vertex AI for real-time inference.

# Image Classification Pipeline (TensorFlow + GCP + Vertex AI)

Train a small TensorFlow CNN locally on Fashion-MNIST, export a **SavedModel**, upload it to **Cloud Storage**, and deploy a real-time **Vertex AI Endpoint** you can call via REST.

## Quickstart

### 0) Setup
```bash
python -m venv .venv && source .venv/bin/activate   # win: .venv\Scripts\activate
pip install -r requirements.txt
cp env.example .env    # fill PROJECT_ID, LOCATION, BUCKET
gcloud auth login
gcloud auth application-default login
bash scripts/setup_gcp.sh
