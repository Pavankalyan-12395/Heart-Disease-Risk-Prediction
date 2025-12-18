# ❤️ Heart Disease Risk Prediction

A Machine Learning–based web application that predicts the risk of heart disease using patient medical parameters.  
The application provides an easy-to-use interface for real-time prediction.

---

## 🚀 Project Overview
Heart disease is one of the leading causes of death worldwide.  
This project uses Machine Learning techniques to predict whether a person has a **Low Risk** or **High Risk** of heart disease based on clinical data.

The model is trained using the Heart Disease dataset and deployed as an interactive web application using Streamlit.

---

## 🖥️ Web Application Features
- User-friendly interface for entering patient details  
- Real-time prediction of heart disease risk  
- Clear and visually styled output (Low Risk / High Risk)  
- Professional UI with custom CSS styling  

---

## 🧠 Machine Learning Details
- Algorithm: **Random Forest Classifier**
- Preprocessing: **StandardScaler**
- Target Variable:
  - `0` → Low Risk of Heart Disease  
  - `1` → High Risk of Heart Disease  

---

## 📊 Input Parameters
- Age  
- Sex  
- Chest Pain Type  
- Resting Blood Pressure  
- Serum Cholesterol  
- Fasting Blood Sugar  
- Resting ECG Results  
- Maximum Heart Rate Achieved  
- Exercise Induced Angina  
- ST Depression  
- Slope of Peak Exercise ST Segment  
- Number of Major Vessels  
- Thalassemia  

---

## 🛠️ Tech Stack
- Python  
- Machine Learning (Scikit-learn)  
- Streamlit  
- Pandas  
- NumPy  
- Joblib  

---

## ⚙️ How to Run the Project

1️⃣ Install dependencies

pip install -r requirements.txt

2️⃣ Train the model

python train_heart.py

3️⃣ Run the web application

streamlit run app_heart.py

4️⃣ Open in browser

http://localhost:8501

✅ Prediction Output

🟢 Low Risk of Heart Disease

🔴 High Risk of Heart Disease

📌 Conclusion

- This project demonstrates the practical application of Machine Learning in healthcare by providing early risk prediction for heart disease.

- It highlights data preprocessing, model training, and deployment using a web-based interface.
