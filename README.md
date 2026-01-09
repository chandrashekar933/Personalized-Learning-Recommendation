# Personalized Learning Recommendation System

This is a **basic machine learning project** that groups students based on their scores and study habits, and then suggests how they should study.

The goal of this project is **not** to build a perfect AI system, but to understand how an ML model can be trained, saved, loaded, and used inside a real application.



## What this project does

* Takes student inputs:

  * Math score
  * CS score
  * AI score
  * Study hours per day
  * Interest level
* Uses **K-Means clustering** to group similar students
* Assigns the student to a learning profile (cluster)
* Shows a **simple learning recommendation** using a Streamlit web app

## How it works (simple)

1. Student data is loaded from a CSV file
2. Features are scaled using `StandardScaler`
3. K-Means clusters students into groups
4. The trained model and scaler are reused
5. New student input is taken from the UI
6. A recommendation is shown based on the cluster

## Tech stack

* Python
* Pandas & NumPy
* Scikit-learn
* Streamlit

## Project structure


Personalized-Learning-Recommendation/
│
├── app.py              # Streamlit UI
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── students.csv
│
├── src/
│   ├── model.py        # Model loading
│   ├── clustering.py   # K-Means logic
│   └── recommend.py    # Recommendation rules
│
└── .venv/              # Local environment (not pushed)

## How to run the project

pip install -r requirements.txt
streamlit run app.py

The app will open in the browser at:

http://localhost:8501

## Why I built this

* To understand ML beyond notebooks
* To learn proper project structure
* To practice using Git and virtual environments
* To see how an ML model works inside a real app

## Limitations

* Uses a small sample dataset
* Recommendations are basic
* No advanced model tuning

This project is mainly for **learning and practice**.