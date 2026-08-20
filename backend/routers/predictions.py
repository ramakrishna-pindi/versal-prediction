from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from ..database.session import get_db
from ..dependencies import get_current_user
from ..models import User, Prediction
from ..schemas.prediction import PredictionRequest, PredictionResponse, DashboardResponse
from ..services.ml_service import predict_bill
from ..services.recommendations import recommendations

router = APIRouter(prefix="/api", tags=["Electricity"])

@router.post("/predict", response_model=PredictionResponse)
def predict(data: PredictionRequest, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    try:
        bill = predict_bill(data)
    except FileNotFoundError as exc:
        raise HTTPException(status_code=500, detail=str(exc))
    record = Prediction(user_id=user.id, **data.model_dump(), predicted_bill=bill)
    db.add(record); db.commit(); db.refresh(record)
    return record

@router.get("/predictions", response_model=list[PredictionResponse])
def history(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return list(db.scalars(select(Prediction).where(Prediction.user_id == user.id).order_by(Prediction.created_at.desc())).all())

@router.delete("/predictions/{prediction_id}", status_code=204)
def delete_prediction(prediction_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    record = db.scalar(select(Prediction).where(Prediction.id == prediction_id, Prediction.user_id == user.id))
    if not record: raise HTTPException(status_code=404, detail="Prediction not found")
    db.delete(record); db.commit()

@router.get("/dashboard", response_model=DashboardResponse)
def dashboard(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    rows = list(db.scalars(select(Prediction).where(Prediction.user_id == user.id)).all())
    if not rows:
        return {"total_predictions":0,"average_bill":0,"highest_bill":0,"lowest_bill":0,"recommendations":[]}
    bills = [r.predicted_bill for r in rows]
    latest = max(rows, key=lambda r: r.created_at)
    tips = recommendations(latest)
    return {"total_predictions":len(rows),"average_bill":round(sum(bills)/len(bills),2),"highest_bill":round(max(bills),2),"lowest_bill":round(min(bills),2),"recommendations":tips}
