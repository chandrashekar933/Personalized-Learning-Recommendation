import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def load_model():
    data = pd.read_csv("data/students.csv")

    features = data[
        ["math_score", "cs_score", "ai_score", "study_hours", "interest_level"]
    ]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(features)

    model = KMeans(n_clusters=3, random_state=42)
    model.fit(X_scaled)

    return model, scaler
