from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

class PredictionRequest(BaseModel):
    previous_units: float = Field(ge=0, le=10000)
    current_units: float = Field(gt=0, le=10000)
    people: int = Field(ge=1, le=50)
    acs: int = Field(ge=0, le=20)
    fans: int = Field(ge=0, le=50)
    fridges: int = Field(ge=0, le=20)
    tvs: int = Field(ge=0, le=30)
    month: int = Field(ge=1, le=12)

class PredictionResponse(PredictionRequest):
    model_config = ConfigDict(from_attributes=True)
    id: int
    predicted_bill: float
    created_at: datetime

class Recommendation(BaseModel):
    title: str
    message: str
    priority: str

class DashboardResponse(BaseModel):
    total_predictions: int
    average_bill: float
    highest_bill: float
    lowest_bill: float
    recommendations: list[Recommendation]
