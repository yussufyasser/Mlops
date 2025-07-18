from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

# Load model
model = joblib.load("best_model.pkl")

# Define FastAPI app
app = FastAPI()

# Define input format
class CustomerFeatures(BaseModel):
    features: list

# Define prediction endpoint
@app.post("/predict")
def predict_churn(data: CustomerFeatures):
    arr = np.array(data.features).reshape(1, -1)
    prediction = model.predict(arr)[0]
    probability = model.predict_proba(arr)[0, 1]
    return {
        "prediction": int(prediction),
        "churn_probability": round(float(probability), 4)
    }

