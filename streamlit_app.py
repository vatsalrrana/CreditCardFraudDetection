import streamlit as st
from predict_fraud import predict_fraud, feature_columns

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Credit Card Fraud Detector",
    page_icon="💳",
    layout="wide"
)

# -------------------- HEADER --------------------
st.markdown(
    """
    <h1 style='text-align: center; color: #ff4b4b;'>
        💳 Credit Card Fraud Detection System
    </h1>
    <p style='text-align: center; font-size:18px;'>
        Protecting your transactions with AI-powered fraud detection 🔐
    </p>
    <hr>
    """,
    unsafe_allow_html=True
)

# -------------------- SIDEBAR --------------------
st.sidebar.header("🧾 Transaction Details")
st.sidebar.write("Enter the transaction values below:")

# Default values
default_values = {
    'Time': 0.0, 'Amount': 0.0,
    **{f'V{i}': 0.0 for i in range(1, 29)}
}

input_data = {}

# Sidebar inputs
for feature in feature_columns:
    input_data[feature] = st.sidebar.number_input(
        label=feature,
        value=default_values.get(feature, 0.0),
        format="%.4f"
    )

# -------------------- MAIN ACTION --------------------
st.markdown("### 🔍 Ready to analyze this transaction?")

if st.button("🚀 Predict Fraud", use_container_width=True):

    with st.spinner("Analyzing transaction... Please wait ⏳"):
        predicted_class, probability_of_fraud = predict_fraud(input_data)

    st.progress(min(int(probability_of_fraud * 100), 100))

    st.markdown("---")
    st.markdown("## 📊 Prediction Results")

    if predicted_class == 1:
        st.error("🚨 **Fraudulent Transaction Detected!**")
        st.metric(
            label="Probability of Fraud",
            value=f"{probability_of_fraud:.2%}"
        )
        st.warning(
            "⚠️ This transaction looks risky. Please review it carefully or block it immediately."
        )
    else:
        st.success("✅ **Legitimate Transaction**")
        st.metric(
            label="Probability of Fraud",
            value=f"{probability_of_fraud:.2%}"
        )
        st.info(
            "🎉 Good news! This transaction appears safe and trustworthy."
        )

# -------------------- FOOTER --------------------
st.markdown(
    """
    <hr>
    <p style='text-align:center; color:gray;'>
        Powered by Machine Learning | Built with Vatsal Rana ❤️
    </p>
    """,
    unsafe_allow_html=True
)
