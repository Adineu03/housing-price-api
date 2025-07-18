# app/train_model.py
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

def main():
    # 1. Load data
    data = fetch_california_housing(as_frame=True)
    X = data.frame.drop(columns=["MedHouseVal"])
    y = data.frame["MedHouseVal"]

    # 2. Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 3. Train
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # 4. Save
    os.makedirs(os.path.dirname(__file__), exist_ok=True)
    model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
    joblib.dump(model, model_path)
    print(f"Model trained and saved to {model_path}")

if __name__ == "__main__":
    main()