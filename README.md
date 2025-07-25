# Ml

# 💬 Sentiment Analyzer Web App

This is a simple and elegant **Sentiment Analysis** web application built using **Streamlit** and a machine learning model trained with **scikit-learn**.

The app takes a user comment or review and predicts whether its sentiment is **Positive** or **Negative** after preprocessing and classification.

---

## 🚀 Demo

🌐 Try the live app: [Click here](https://hvpidpc2mtg8dkmkz4fjgt.streamlit.app/
)  

---

## 🎯 Features

- 🧠 Trained ML model with `LogisticRegression`
- ✨ Custom styled Streamlit UI (Black + Pink theme)
- 🧹 Text cleaning and NLP preprocessing
- 🗣️ Handles URLs, hashtags, mentions, stopwords, and punctuation
- ✅ Supports real-time sentiment prediction

---

## 🛠️ Tech Stack

- Python
- scikit-learn
- Streamlit
- NLTK
- NumPy
- Pickle

---

▶️ Run Locally
To launch the app locally using Streamlit:

streamlit run app.py
Make sure the following files are in the root directory:

app.py

model.pkl

vectorizer.pkl

encoder.pkl

📝 Model Details
The model was trained on a labeled dataset of text reviews. It uses:

TfidfVectorizer for feature extraction

LogisticRegression for classification

LabelEncoder for encoding sentiment labels

