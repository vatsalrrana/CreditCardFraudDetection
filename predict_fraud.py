import joblib
import pandas as pd
import numpy as np

model = joblib.load('logistic_regression_model.joblib')
scaler = joblib.load('scaler.joblib')

feature_columns = ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',                   'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',                   'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount']

def predict_fraud(transaction_data):
    input_df = pd.DataFrame([transaction_data], columns=feature_columns)
    scaled_input = scaler.transform(input_df)
    predicted_class = model.predict(scaled_input)[0]
    probability_of_fraud = model.predict_proba(scaled_input)[:, 1][0]
    return int(predicted_class), float(probability_of_fraud)
