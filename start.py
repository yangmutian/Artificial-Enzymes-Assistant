from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from catboost import CatBoostClassifier
from typing import Any
import os
import numpy as np
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_PATHS = {
    "catalase": "./catalase/model",
    "peroxidase": "./peroxidase/model",
    "oxidase": "./oxidase/model"
}

MODELS = {
    "catalase": [],
    "peroxidase": [],
    "oxidase": []
}

EXPECTED_FEATURES = []

print("Initializing nanozyme multi-model system...")

for m_type, path in MODEL_PATHS.items():
    if not os.path.exists(path):
        print(f" Warning: Path {path} not found. Please check if the directory exists!")
        continue
        
    for filename in os.listdir(path):
        if filename.endswith('.cbm'):
            filepath = os.path.join(path, filename)
            model = CatBoostClassifier()
            model.load_model(filepath)
            MODELS[m_type].append(model)
            
            if not EXPECTED_FEATURES:
                EXPECTED_FEATURES = model.feature_names_
                
    print(f" [{m_type.upper()}] Successfully loaded {len(MODELS[m_type])} models.")

print(f"⚠️ Expected number of features for the model: {len(EXPECTED_FEATURES)}")

class FeatureInput(BaseModel):
    features: list[Any]
    model_type: str

@app.post("/predict")
def predict(data: FeatureInput):
    m_type = data.model_type
    
    if m_type not in MODELS or not MODELS[m_type]:
        return {"error": f"Models related to {m_type} are not loaded. Please check the backend status."}
    
    if len(data.features) != len(EXPECTED_FEATURES):
        return {"error": f"Feature count mismatch! Expected {len(EXPECTED_FEATURES)} features, but received {len(data.features)}."}
    
    try:
        input_df = pd.DataFrame([data.features], columns=EXPECTED_FEATURES)
        
        probabilities = [model.predict_proba(input_df)[0][1] for model in MODELS[m_type]]
        avg_probability = np.mean(probabilities)
        
        return {
            "average_probability": round(float(avg_probability), 4)
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)