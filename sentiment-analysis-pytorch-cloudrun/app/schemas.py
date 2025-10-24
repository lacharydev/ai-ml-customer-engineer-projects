from pydantic import BaseModel, Field

class PredictRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Text to analyze")

class PredictResponse(BaseModel):
    label: str
    score: float

