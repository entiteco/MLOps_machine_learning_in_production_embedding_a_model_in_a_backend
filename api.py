from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI(title="House Price Predictor API")

# Chargement du modèle de régression
model = joblib.load("regression.joblib")

class HouseFeatures(BaseModel):
    size: float
    rooms: int
    garden: int

# Endpoint POST avec prédiction réelle
@app.post("/predict")
def predict_post(features: HouseFeatures):
    data = [[features.size, features.rooms, features.garden]]
    prediction = model.predict(data)
    return {"y_pred": float(prediction[0])}