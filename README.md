# ⚡ Smart Electricity Bill Prediction & Energy Saving Website

A complete learning-oriented full-stack project:

FRONTEND: HTML + CSS + JavaScript
BACKEND: Python + FastAPI
ML: Pandas + NumPy + Scikit-learn + Joblib
DATABASE: MySQL + SQLAlchemy
AUTH: JWT

## Exact build order
1. Install Python 3.11+
2. Create virtual environment
3. Install requirements.txt
4. Create MySQL database `electricity_db`
5. Copy `.env.example` to `.env` and set password
6. Run `python ml/train_model.py`
7. Run `uvicorn backend.main:app --reload`
8. Open http://127.0.0.1:8000
9. Swagger: http://127.0.0.1:8000/docs

## Database
Run:
CREATE DATABASE electricity_db;

Tables are created automatically on first startup.

## Project order for learning
A. frontend/html -> structure
B. frontend/css -> design
C. frontend/js -> browser logic and Fetch API
D. backend/main.py -> FastAPI app
E. backend/schemas -> Pydantic validation
F. backend/models + database -> MySQL
G. backend/routers/auth.py -> registration/login
H. backend/routers/predictions.py -> prediction/history/dashboard
I. backend/services/ml_service.py -> model inference
J. backend/services/recommendations.py -> bill-saving advice
K. ml/train_model.py -> data generation/training/evaluation

## Important
The included dataset is synthetic so the application runs immediately. It is for learning/demo purposes. Replace it with a real utility dataset before claiming real-world accuracy.
