import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

from recommend import recommend_resources

# Load data
data = pd.read_csv("data/students.csv")

# Features for clustering
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

for index, row in data.iterrows():
    print(f"\nStudent ID: {row['student_id']}")
    print(f"Cluster: {row['cluster']}")
    print("Recommendations:")
    for rec in recommend_resources(row['cluster']):
        print("-", rec)
