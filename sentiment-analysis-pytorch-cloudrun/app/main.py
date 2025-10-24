from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import PredictRequest, PredictResponse
from app.model import get_pipeline

app = FastAPI(title="Sentiment API", version="1.0.0")

# Optional CORS (helpful for quick demos from a browser app)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictResponse)
def predict(payload: PredictRequest):
    try:
        nlp = get_pipeline()
        result = nlp(payload.text)[0]   # {'label': 'POSITIVE', 'score': 0.999}
        return PredictResponse(label=result["label"], score=float(result["score"]))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

