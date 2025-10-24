from transformers import pipeline
from functools import lru_cache
import os

MODEL_NAME = os.getenv("MODEL_NAME", "distilbert-base-uncased-finetuned-sst-2-english")

@lru_cache(maxsize=1)
def get_pipeline():
    # Uses PyTorch by default when available
    return pipeline("sentiment-analysis", model=MODEL_NAME)

