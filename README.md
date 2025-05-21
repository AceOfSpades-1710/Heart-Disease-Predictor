# Heart Disease Prediction using Machine Learning
---

This project uses machine learning to predict whether a person is likely to have heart disease based on clinical attributes. It includes a trained model using a Random Forest Classifier and a user-friendly web app built with Streamlit.

---
Database Link: https://www.kaggle.com/datasets/ketangangal/heart-disease-dataset-uci
---

## 🚀 Project Overview

- 🧠 **Model**: Random Forest Classifier
- 📁 **Dataset**: `heart.csv`
- 📊 **Features**: Includes age, sex, chest pain type, cholesterol, and more
- 🌐 **Deployment**: Streamlit app for real-time user input and prediction
- 📈 **Goal**: Help users predict the likelihood of heart disease based on input features

---

## 📝 Dataset Description

The dataset used is a standard heart disease dataset with the following columns:

| Column Name | Description |
|-------------|-------------|
| age         | Age of the patient |
| sex         | Sex (Male/Female) |
| cp          | Chest pain type (0-3) |
| trestbps    | Resting blood pressure |
| chol        | Serum cholesterol (mg/dl) |
| fbs         | Fasting blood sugar > 120 mg/dl (1 = true; 0 = false) |
| restecg     | Resting electrocardiographic results |
| thalach     | Maximum heart rate achieved |
| exang       | Exercise induced angina |
| oldpeak     | ST depression induced by exercise |
| slope       | Slope of the peak exercise ST segment |
| ca          | Number of major vessels (0-3) colored by fluoroscopy |
| thal        | Thalassemia (1 = normal, 2 = fixed defect, 3 = reversible defect) |
| target      | 1 = disease, 0 = no disease (target variable) |

---

## 🧑‍💻 How It Works

1. Load and explore the dataset (`heart.csv`)
2. Encode categorical variables (like 'Male'/'Female') numerically
3. Split data into training and testing sets
4. Train a `RandomForestClassifier`
5. Evaluate model accuracy
6. Save the trained model using `joblib`
7. Build a frontend using Streamlit for real-time user input and predictions

---

## 📂 Project Structure

```bash
.
├── heart.csv
├── heart_model.pkl
├── app.py
├── requirements.txt
└── README.md
```

---

## 🧠 Model Performance

| Metric      | Value       |
|-------------|-------------|
| Accuracy    |  ~98% (varies depending on dataset split)|
| Model       | Random Forest Classifier |

---

## 📸 Screenshot

![Screen Shot 2025-05-22 at 2 41 38 AM](https://github.com/user-attachments/assets/923530bb-e1b4-4bf4-8ed1-b42bae4bed85)

![Screen Shot 2025-05-22 at 2 41 46 AM](https://github.com/user-attachments/assets/78f185ac-1523-433e-bec9-f1d7ec034a84)
