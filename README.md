# Ml

# 💬 Sentiment Analyzer Web App

This is a simple and elegant **Sentiment Analysis** web application built using **Streamlit** and a machine learning model trained with **scikit-learn**.

The app takes a user comment or review and predicts whether its sentiment is **Positive** or **Negative** after preprocessing and classification.

---

## 🚀 Demo

🌐 Try the live app: [Click here](https://hvpidpc2mtg8dkmkz4fjgt.streamlit.app/
)  
_(Replace with actual link when deployed)_

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

## 📦 Installation

Clone the repository and install the dependencies:


git clone https://github.com/Mayar-hany-2005/Ml.git
cd Ml
pip install -r requirements.txt

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


👩‍💻 Author
Mayar Hany
📧 mayarhany1999@gmail.com
📍 Cairo, Egypt
🔗 LinkedIn
🎨 Portfolio
