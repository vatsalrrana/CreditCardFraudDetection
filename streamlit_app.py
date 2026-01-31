import streamlit as st
from predict_fraud import predict_fraud, feature_columns

st.title('Credit Card Fraud Detection')

st.markdown("Enter the transaction details below to predict if it's fraudulent.")

input_data = {}

default_values = {
    'Time': 0.0, 'V1': 0.0, 'V2': 0.0, 'V3': 0.0, 'V4': 0.0, 'V5': 0.0,
    'V6': 0.0, 'V7': 0.0, 'V8': 0.0, 'V9': 0.0, 'V10': 0.0,
    'V11': 0.0, 'V12': 0.0, 'V13': 0.0, 'V14': 0.0, 'V15': 0.0,
    'V16': 0.0, 'V17': 0.0, 'V18': 0.0, 'V19': 0.0, 'V20': 0.0,
    'V21': 0.0, 'V22': 0.0, 'V23': 0.0, 'V24': 0.0, 'V25': 0.0,
    'V26': 0.0, 'V27': 0.0, 'V28': 0.0, 'Amount': 0.0
}

for feature in feature_columns:
    input_data[feature] = st.number_input(f'Enter {feature}', value=default_values.get(feature, 0.0))

if st.button('Predict Fraud'):
    predicted_class, probability_of_fraud = predict_fraud(input_data)

    st.write("--- Prediction Results ---")
    if predicted_class == 1:
        st.error("**Fraudulent Transaction Detected!**")
        st.write("Probability of Fraud: {:.4f}".format(probability_of_fraud))
        st.warning("Please review this transaction carefully.")
    else:
        st.success("**Legitimate Transaction.**")
        st.write("Probability of Fraud: {:.4f}".format(probability_of_fraud))
        st.info("This transaction appears to be safe.")
