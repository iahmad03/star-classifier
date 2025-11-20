import streamlit as st
import pandas as pd
import joblib

st.title("Star Classifier")

model = joblib.load("notebook\\star_classifier_optimized.pkl")
le_color = joblib.load("notebook\\le_color.pkl")
le_spectral = joblib.load("notebook\\le_spectral.pkl")

with st.form("star_form", clear_on_submit=False):
    temperature = st.slider("Temperature (K)", 1000, 50000, 5000, step=100)
    luminosity = st.slider("Luminosity (L/Lo)", 0.0001, 100000.0, 1.0)
    radius = st.slider("Radius (R/Ro)", 0.01, 1000.0, 1.0)
    absolute_magnitude = st.slider("Absolute Magnitude (Mv)", -10, 20, 5)
    star_color = st.selectbox("Star Color", le_color.classes_)
    spectral_class = st.selectbox("Spectral Class", le_spectral.classes_)

    submitted = st.form_submit_button("Predict Star Type")

if submitted:
    color_encoded = le_color.transform([star_color])[0]
    spectral_encoded = le_spectral.transform([spectral_class])[0]

    input_df = pd.DataFrame({
        "Temperature (K)": [temperature],
        "Luminosity(L/Lo)": [luminosity],
        "Radius(R/Ro)": [radius],
        "Absolute magnitude(Mv)": [absolute_magnitude],
        "Star color": [color_encoded],
        "Spectral Class": [spectral_encoded]
    })

    prediction = model.predict(input_df)
    st.success(f"Predicted Star Type: {prediction[0]}")
