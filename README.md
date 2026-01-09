## Personalized Learning Recommendation System
An AI-based system that recommends personalized learning content to students based on their academic performance, interests, and learning behavior using machine learning techniques.

## Objectives
- Analyze student performance data
- Group students into learning profiles
- Recommend suitable learning resources

## Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit

### How it Works
1. Student data is clustered using K-Means.
2. Each cluster represents a learning profile.
3. Rule-based logic maps profiles to recommendations.
4. Streamlit UI allows real-time input and recommendations.

### Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
