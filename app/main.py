# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os

# 1. Load the trained model at startup
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")
model = joblib.load(MODEL_PATH)

# 2. Define request schema
class HousingFeatures(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

app = FastAPI(title="California Housing Price API")

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
def predict(payload: HousingFeatures):
    # 3. Convert to DataFrame
    df = pd.DataFrame([payload.dict()])
    # 4. Make prediction
    pred = model.predict(df)[0]
    return {"predicted_price": round(float(pred), 3)}