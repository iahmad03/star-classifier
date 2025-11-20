import joblib

def test_model_loads():
    model = joblib.load("notebook\\star_classifier_optimized.pkl")
    assert model is not None
