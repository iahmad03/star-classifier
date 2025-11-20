import joblib
import pandas as pd

model = joblib.load("notebook\\star_classifier_optimized.pkl")

def test_prediction_shape():
    input_df = pd.DataFrame({
        "Temperature (K)": [5000],
        "Luminosity(L/Lo)": [1.0],
        "Radius(R/Ro)": [1.0],
        "Absolute magnitude(Mv)": [5],
        "Star color": [0],
        
        "Spectral Class": [0]
    })
    pred = model.predict(input_df)
    assert len(pred) == 1
