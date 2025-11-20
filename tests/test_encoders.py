import joblib

le_color = joblib.load("notebook\\le_color.pkl")
le_spectral = joblib.load("notebook\\le_spectral.pkl")

def test_encoder_classes():
    assert "Red" in le_color.classes_ or len(le_color.classes_) > 0
    assert len(le_spectral.classes_) > 0
