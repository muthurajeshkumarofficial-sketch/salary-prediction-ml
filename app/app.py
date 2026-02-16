# ============================================
# Import necessary libraries
# ============================================

import streamlit as st
import pandas as pd
import pickle

# ============================================
# Load model and encoders
# ============================================

model = pickle.load(open("../model/random_forest_model.pkl", "rb"))
encoders = pickle.load(open("../model/label_encoders.pkl", "rb"))

# ============================================
# App Title
# ============================================

st.title("Salary Prediction App")
st.write("Enter details to predict salary")

# ============================================
# User Inputs
# ============================================

experience_level = st.selectbox(
    "Experience Level",
    encoders["experience_level"].classes_
)

employment_type = st.selectbox(
    "Employment Type",
    encoders["employment_type"].classes_
)

job_title = st.selectbox(
    "Job Title",
    encoders["job_title"].classes_
)

company_size = st.selectbox(
    "Company Size",
    encoders["company_size"].classes_
)

remote_ratio = st.slider(
    "Remote Ratio",
    0, 100, 50
)

company_location = st.selectbox(
    "Company Location",
    encoders["company_location"].classes_
)

# ============================================
# Prediction Button
# ============================================

if st.button("Predict Salary"):

    input_data = {
        "experience_level": encoders["experience_level"].transform([experience_level])[0],
        "employment_type": encoders["employment_type"].transform([employment_type])[0],
        "job_title": encoders["job_title"].transform([job_title])[0],
        "company_size": encoders["company_size"].transform([company_size])[0],
        "remote_ratio": remote_ratio,
        "company_location": encoders["company_location"].transform([company_location])[0],
    }

    input_df = pd.DataFrame([input_data])

    prediction = model.predict(input_df)[0]

    st.success(f"Predicted Salary: ${int(prediction)}")
