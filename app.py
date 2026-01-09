from src.model import load_model

import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from src.recommend import recommend_resources

st.title("Personalized Learning Recommendation System")

st.write("Enter student details to get learning recommendations")

# Input fields
math = st.slider("Math Score", 0, 100, 50)
cs = st.slider("CS Score", 0, 100, 50)
ai = st.slider("AI Score", 0, 100, 50)
hours = st.slider("Study Hours per Day", 0, 10, 3)
interest = st.slider("Interest Level (1-5)", 1, 5, 3)

if st.button("Get Recommendation"):
    # Load existing student data
    model, scaler = load_model()

    new_student = scaler.transform([[math, cs, ai, hours, interest]])
    cluster = model.predict(new_student)[0]


    st.subheader(f"Student Profile Cluster: {cluster}")
    st.subheader("Recommended Learning Plan")

    for rec in recommend_resources(cluster):
        st.write("•", rec)
