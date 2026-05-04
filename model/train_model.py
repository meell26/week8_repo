import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

df = pd.read_csv("../features/features.csv")

model = IsolationForest(contamination=0.2)
model.fit(df)

joblib.dump(model, "model.pkl")

print("Model saved")