import pandas as pd
import numpy as np
import joblib

def test_full_prediction():
    model = joblib.load("notebook\\star_classifier_optimized.pkl")
    le_color = joblib.load("notebook\\le_color.pkl")
    le_spectral = joblib.load("notebook\\le_spectral.pkl")

    raw_input = {
        "Temperature (K)": 5000,
        "Luminosity(L/Lo)": 1.0,
        "Radius(R/Ro)": 1.0,
        "Absolute magnitude(Mv)": 5,
        "Star color": "Red",
        "Spectral Class": "G"
    }

    raw_input["Star color"] = le_color.transform([raw_input["Star color"]])[0]
    raw_input["Spectral Class"] = le_spectral.transform([raw_input["Spectral Class"]])[0]

    input_df = pd.DataFrame([raw_input])

    prediction = model.predict(input_df)

    assert prediction.shape[0] == 1
    assert isinstance(prediction[0], (int, np.integer, str))
