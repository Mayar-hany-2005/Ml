import streamlit as st
import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression
import re
import string
import nltk
from nltk.corpus import stopwords

# تحميل stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# تحميل النموذج و الأدوات
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

# تنظيف النص
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    text = re.sub(r'\@[\w]*', '', text)
    text = re.sub(r'#[A-Za-z0-9_]+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\d+', '', text)
    text = text.strip()
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

# دالة التنبؤ
def predict_sentiment(text):
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])
    pred = model.predict(vec)
    label = encoder.inverse_transform(pred)
    return label[0]


# 🎨 تنسيق CSS مخصص
custom_css = """
<style>
body {
    background: linear-gradient(to bottom, #ffb6c1, #000000);
    color: #fff;
}

[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #ffb6c1 10%, #000000 90%);
    animation: gradientMove 12s ease infinite;
    background-size: 400% 400%;
}

@keyframes gradientMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

h1, .stTextInput label, .stTextArea label, .stButton button {
    color: #fff;
    font-family: 'Segoe UI', sans-serif;
    font-size: 28px;
}

.stTextArea textarea {
    height: 300px !important;
    font-size: 24px !important;
    font-family: 'Segoe UI', sans-serif !important;
    color: #fff !important;
    background-color: #111 !important;
    border: 3px solid #ff69b4 !important;
    border-radius: 20px !important;
    padding: 20px !important;
}

.stButton button {
    border: 2px solid #ff69b4;
    background-color: #222;
    color: #fff;
    border-radius: 20px;
    font-size: 22px;
    font-family: 'Segoe UI', sans-serif;
    padding: 12px 30px;
}

.stButton button:hover {
    background-color: #ff69b4;
    color: #000;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 🎀 Layout
st.title("💬 Sentiment Analyzer")
st.subheader("✨ Write a comment below and let's see how it feels!")

user_input = st.text_area("📝 Your Comment:")

if st.button("🎀 Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("⚠️ Please write something first.")
    else:
        result = predict_sentiment(user_input)
        if result == "positive":
            st.success("🥰 Sentiment: Positive")
        else:
            st.error("😠 Sentiment: Negative")
