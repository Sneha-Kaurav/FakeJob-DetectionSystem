# Advice: Keep model.pkl in the root directory, next to api.py.

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Initialize FastAPI app
app = FastAPI()

# Load model and vectorizer
model_xgb = joblib.load("xgb_model.joblib")
vectorizer = joblib.load("vectorizer.joblib")

# # Define request schema
# class InputData(BaseModel):                               # for array of 100 input numbers
#     data: list[float]

class JobText(BaseModel):
    text: str


# # Prediction endpoint
# @app.post("/predict")
# def predict(input: InputData):
#     arr = np.array(input.data).reshape(1, -1)
#     prediction = model_xgb.predict(arr)[0]
#     return {"prediction": int(prediction)}

@app.post("/predict")
def predict(input: JobText):
    # Extract the raw text input
    text = input.text

    # Vectorize using your saved TF-IDF vectorizer
    X = vectorizer.transform([text])

    # Predict using the trained XGBoost model
    prediction = model_xgb.predict(X)[0]

    # Return a human-friendly label
    return {"prediction": "Fake" if prediction == 1 else "Real"}

