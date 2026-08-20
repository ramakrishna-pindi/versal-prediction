from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from .database.base import Base
from .database.session import engine
from . import models
from .routers import auth, predictions

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Electricity Bill Prediction API", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.include_router(auth.router)
app.include_router(predictions.router)

@app.get("/api/health", tags=["System"])
def health():
    return {"status":"ok"}

FRONTEND = Path(__file__).resolve().parent.parent / "frontend"
app.mount("/", StaticFiles(directory=FRONTEND, html=True), name="frontend")
