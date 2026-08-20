from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

ROOT = Path(__file__).resolve().parent
rng = np.random.default_rng(42)
n = 3000
previous = rng.integers(50, 500, n)
current = np.clip(previous + rng.normal(20, 70, n), 30, 650)
people = rng.integers(1, 8, n)
acs = rng.integers(0, 4, n)
fans = rng.integers(1, 8, n)
fridges = rng.integers(1, 3, n)
tvs = rng.integers(0, 5, n)
month = rng.integers(1, 13, n)
season = np.where(np.isin(month, [4,5,6,7]), 1.15, 1.0)
bill = (250 + current*8.2 + previous*1.2 + people*25 + acs*140 + fans*15 + fridges*45 + tvs*18)*season + rng.normal(0,120,n)
bill = np.maximum(bill, 300)

df = pd.DataFrame({"previous_units":previous,"current_units":current.round(1),"people":people,"acs":acs,"fans":fans,"fridges":fridges,"tvs":tvs,"month":month,"bill":bill.round(2)})
df.to_csv(ROOT / "electricity_training_data.csv", index=False)
features = ["previous_units","current_units","people","acs","fans","fridges","tvs","month"]
X_train,X_test,y_train,y_test=train_test_split(df[features],df.bill,test_size=.2,random_state=42)
model=RandomForestRegressor(n_estimators=250,random_state=42,n_jobs=-1)
model.fit(X_train,y_train)
pred=model.predict(X_test)
print("MAE:",round(mean_absolute_error(y_test,pred),2))
print("R2 :",round(r2_score(y_test,pred),4))
joblib.dump({"model":model,"features":features},ROOT/"electricity_model.joblib")
print("Model saved:", ROOT/"electricity_model.joblib")
