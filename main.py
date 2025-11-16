from fastapi import FastAPI
import pandas as pd
import joblib

# Load the model & metadata
model = joblib.load("models/churn_xgb_model.pkl")
feature_cols = joblib.load("models/churn_feature_columns.pkl")
cat_cols = joblib.load("models/churn_categorical_columns.pkl")

app = FastAPI(
    title="SaaS Churn Prediction API",
    description="Predict churn probability for SaaS customers",
    version="1.0"
)

def prepare_features(data: dict):
    df = pd.DataFrame([data])  # convert JSON→DataFrame structure

    # Convert bool to int
    for col in df.select_dtypes(include=["bool"]).columns:
        df[col] = df[col].astype(int)

    # One-hot encode
    df_encoded = pd.get_dummies(df, columns=cat_cols, drop_first=True)

    # Align columns
    df_encoded = df_encoded.reindex(columns=feature_cols, fill_value=0)

    return df_encoded

@app.post("/predict")
def predict(data: dict):
    X = prepare_features(data)
    proba = model.predict_proba(X)[0][1]
    pred = int(model.predict(X)[0])

    return {
        "churn_prediction": pred,
        "churn_probability": float(proba)
    }
