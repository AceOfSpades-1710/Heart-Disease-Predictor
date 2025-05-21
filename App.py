import streamlit as st
import numpy as np
import joblib

model = joblib.load("heart_model.pkl")

st.title("❤️ Heart Disease Prediction App")
st.markdown("Enter the patient details below:")

# Feature input fields
age = st.number_input("Age", min_value=0, max_value=120)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type (0-3)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure")
chol = st.number_input("Cholesterol Level")
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
restecg = st.selectbox("Resting ECG Results (0-2)", [0, 1, 2])
thalach = st.number_input("Max Heart Rate Achieved")
exang = st.selectbox("Exercise Induced Angina (0 = No, 1 = Yes)", [0, 1])
oldpeak = st.number_input("ST depression induced")
slope = st.selectbox("Slope of peak exercise ST segment (0-2)", [0, 1, 2])
ca = st.selectbox("Number of major vessels (0-3)", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia (0 = normal, 1 = fixed defect, 2 = reversible defect)", [0, 1, 2])

# Mapping categorical fields
sex = 1 if sex == "Male" else 0

if st.button("Predict"):
    user_input = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach,
                            exang, oldpeak, slope, ca, thal]])
    prediction = model.predict(user_input)

    if prediction[0] == 1:
        st.error("You might have heart disease.")
    else:
        st.success("You are unlikely to have heart disease.")
