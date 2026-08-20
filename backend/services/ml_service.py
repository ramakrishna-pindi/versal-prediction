from pathlib import Path
import joblib
import pandas as pd

MODEL_PATH = Path(__file__).resolve().parents[2] / "ml" / "electricity_model.joblib"
_model_bundle = None

def load_model():
    global _model_bundle
    if _model_bundle is None:
        if not MODEL_PATH.exists():
            raise FileNotFoundError("Model missing. Run: python ml/train_model.py")
        _model_bundle = joblib.load(MODEL_PATH)
    return _model_bundle

def predict_bill(data) -> float:
    bundle = load_model()
    row = pd.DataFrame([{f: getattr(data, f) for f in bundle["features"]}])
    return round(max(0.0, float(bundle["model"].predict(row)[0])), 2)
