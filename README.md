# 🌠 Star Classifier

This project predicts the type of a star based on its physical and spectral properties using machine learning.

## Overview

- **📓 Jupyter Notebook:**  
  - Complete exploration of the star dataset  
  - Visualizations (HR diagram, radius vs temperature, mass vs luminosity)  
  - Data cleaning and encoding  
  - Model training and evaluation with Random Forest, Logistic Regression, and KNN  
  - Cross-validation and feature importance analysis  

- **🌐 Streamlit App:**  
  - Interactive interface to input star properties  
  - Predict star type in real-time using the trained Random Forest model  

- **🧪 Testing:**  
  - Unit tests for encoders, model, and prediction pipeline  
  - Integration test to simulate a full prediction from raw inputs  

- **✔️ Saved Models and Encoders:**  
  - Random Forest model (`star_classifier_optimized.pkl`)  
  - Label encoders for `Star color` and `Spectral Class`  

## Streamlit App

The Streamlit app (`app.py`) allows users to:

- Input star properties interactively
- Get predicted star type in real-time

### How to Run

1. **Clone the repository:**

```bash
git clone https://github.com/iahmad03/star-classifier.git
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the Streamlit app:**

```bash
streamlit run app.py
```
