import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load data
data = pd.read_csv("data/students.csv")

# Features for clusteringpip install pandas numpy scikit-learn

features = data[
    ["math_score", "cs_score", "ai_score", "study_hours", "interest_level"]
]

# Scale features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Apply K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
data["cluster"] = kmeans.fit_predict(scaled_features)

# Show results
print(data)
