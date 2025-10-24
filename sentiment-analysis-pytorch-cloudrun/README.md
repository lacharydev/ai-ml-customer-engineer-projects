# Sentiment Analysis API (PyTorch + Cloud Run)

A tiny FastAPI that returns sentiment for any sentence using a pre-trained DistilBERT (SST-2).

## Quickstart (local)
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

