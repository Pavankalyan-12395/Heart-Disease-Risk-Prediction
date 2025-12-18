import streamlit as st
import joblib
import numpy as np

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Heart Disease Risk Prediction",
    page_icon="❤️",
    layout="centered"
)

# ---------------- CSS STYLE ----------------
def load_css():
    def load_css():
        st.markdown("""
        <style>

        /* Full background */
        .stApp {
            background: linear-gradient(135deg, #0f172a, #020617);
            font-family: 'Segoe UI', sans-serif;
        }

        /* Main card */
        .block-container {
            max-width: 950px;
            padding: 2.5rem;
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(14px);
            border-radius: 24px;
            box-shadow: 0 25px 60px rgba(0,0,0,0.6);
        }

        /* Title */
        h1 {
            text-align: center;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 0.2rem;
        }

        /* Subtitle text */
        .stMarkdown p {
            text-align: center;
            color: #cbd5f5;
            font-size: 16px;
            margin-bottom: 1.5rem;
        }

        /* Section headers */
        h2, h3 {
            color: #7dd3fc;
            margin-top: 1.2rem;
        }

        /* Labels */
        label {
            color: #e5e7eb !important;
            font-weight: 500;
            font-size: 14px;
        }

        /* Inputs */
        .stNumberInput input,
        .stSelectbox div[data-baseweb="select"] > div {
            background: rgba(255, 255, 255, 0.12) !important;
            color: white !important;
            border-radius: 14px;
            border: 1px solid rgba(255,255,255,0.2);
            padding: 10px;
        }

        /* Button */
        .stButton button {
            width: 100%;
            background: linear-gradient(90deg, #38bdf8, #2563eb);
            color: white;
            font-size: 17px;
            font-weight: 700;
            padding: 0.8rem;
            border-radius: 16px;
            border: none;
            margin-top: 1.2rem;
            transition: all 0.3s ease;
        }

        .stButton button:hover {
            background: linear-gradient(90deg, #0ea5e9, #1d4ed8);
            transform: translateY(-2px) scale(1.01);
        }

        /* Success card */
        .stAlertSuccess {
            background: linear-gradient(90deg, #064e3b, #022c22);
            color: #ecfdf5;
            border-radius: 18px;
            padding: 1rem;
            font-size: 18px;
            text-align: center;
        }

        /* Error card */
        .stAlertError {
            background: linear-gradient(90deg, #7f1d1d, #450a0a);
            color: #fee2e2;
            border-radius: 18px;
            padding: 1rem;
            font-size: 18px;
            text-align: center;
        }

        </style>
    """, unsafe_allow_html=True)
load_css()
st.markdown("<p>Enter patient health details to predict heart disease risk.</p>",
    unsafe_allow_html=True
)


# ✅ CALL CSS HERE (ONLY ONCE)
load_css()

# ---------------- LOAD MODEL ----------------
model = joblib.load("model_heart.pkl")

# ---------------- TITLE ----------------
st.title("❤️ Heart Disease Risk Prediction")
st.write("Enter patient health details to predict heart disease risk.")

st.divider()

# ---------------- INPUT FORM ----------------
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 1, 120, 62)
    sex = st.selectbox("Sex", ["Male", "Female"])
    cp = st.selectbox("Chest Pain Type (0–3)", [0, 1, 2, 3])
    trestbps = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 124)
    chol = st.number_input("Serum Cholesterol (mg/dl)", 100, 400, 209)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])

with col2:
    restecg = st.selectbox("Resting ECG Results (0–2)", [0, 1, 2])
    thalach = st.number_input("Maximum Heart Rate Achieved", 60, 220, 163)
    exang = st.selectbox("Exercise Induced Angina", [0, 1])
    oldpeak = st.number_input("ST Depression Induced by Exercise", 0.0, 6.0, 2.0)
    slope = st.selectbox("Slope of Peak Exercise ST Segment (0–2)", [0, 1, 2])
    ca = st.selectbox("Number of Major Vessels (0–4)", [0, 1, 2, 3, 4])
    thal = st.selectbox(
        "Thalassemia (1 = normal, 2 = fixed defect, 3 = reversible defect)",
        [1, 2, 3]
    )

sex = 1 if sex == "Male" else 0

# ---------------- PREDICTION ----------------
st.divider()

if st.button("Predict Heart Disease Risk"):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs,
                            restecg, thalach, exang, oldpeak,
                            slope, ca, thal]])

    prediction = model.predict(input_data)

    if prediction[0] == 0:
        st.success("✅ Low Risk of Heart Disease")
    else:
        st.error("⚠️ High Risk of Heart Disease")


