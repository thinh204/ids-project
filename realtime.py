import joblib
import numpy as np

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
le = joblib.load("label_encoder.pkl")

def get_flow():
    return np.array([[3, 1000, 5, 2, 500, 200, 100, 80, 300, 50, 60]])

flow = get_flow()

flow_scaled = scaler.transform(flow)

pred = model.predict(flow_scaled)[0]
label = le.inverse_transform([pred])[0]

if label != "BENIGN":
    print(f"[ALERT] Suspicious traffic detected: {label}. Destination Port: 80")
else:
    print("[OK] BENIGN traffic")