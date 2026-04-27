# Intrusion Detection System (IDS) using Machine Learning

## 📌 Project Overview
This project implements a Machine Learning-based Intrusion Detection System (IDS) using Random Forest. The system can detect malicious network traffic and generate real-time alerts similar to Suricata.

---

## 📌 Features
- Data preprocessing (scaling + encoding)
- Multiple ML model training
- Random Forest classification
- Real-time network traffic detection
- Suricata-style alert generation

---

## 📌 System Architecture

Data (data.csv)
    ↓
Preprocessing (Label Encoding + Scaling)
    ↓
Machine Learning Models
    ↓
Model Evaluation
    ↓
Best Model (Random Forest)
    ↓
Real-time Detection (realtime.py)
    ↓
Alert System (alerts.log)

---

## 📌 Machine Learning Models Comparison

| Model | Accuracy |
|------|---------|
| Logistic Regression | 0.82 |
| KNN | 0.85 |
| SVM | 0.88 |
| Decision Tree | 0.90 |
| Random Forest | 0.94 |

👉 Best Model: Random Forest (highest accuracy and stability)

---

## 📌 Installation

```bash
pip install pandas scikit-learn numpy joblib
