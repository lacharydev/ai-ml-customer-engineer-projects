FROM python:3.11-slim

# System deps (git helps transformers resolve refs)
RUN apt-get update && apt-get install -y --no-install-recommends \
    git && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Pre-download model weights at build time (improves first-request latency)
ENV MODEL_NAME=distilbert-base-uncased-finetuned-sst-2-english
RUN python -c "from transformers import pipeline; \
nlp=pipeline('sentiment-analysis', model='${MODEL_NAME}'); \
print(nlp('pre-download ok'))"

COPY app ./app

# Use a non-root user (best practice)
RUN useradd -m appuser
USER appuser

EXPOSE 8080
ENV PORT=8080
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

