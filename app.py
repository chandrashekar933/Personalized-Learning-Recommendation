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
    data = pd.read_csv("data/students.csv")

    features = data[
        ["math_score", "cs_score", "ai_score", "study_hours", "interest_level"]
    ]

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(scaled_features)

    # Predict cluster for new student
    new_student = scaler.transform([[math, cs, ai, hours, interest]])
    cluster = kmeans.predict(new_student)[0]

    st.subheader(f"Student Profile Cluster: {cluster}")
    st.subheader("Recommended Learning Plan")

    for rec in recommend_resources(cluster):
        st.write("•", rec)
