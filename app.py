import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Stock Trend & Sentiment Analyzer", layout="wide")
st.title("📊 Stock Trend & Market Sentiment Analyzer")

# Load final dataset (price + sentiment)
data_path = "data/final_dataset.csv"

if not os.path.exists(data_path):
    st.error("Final dataset not found. Please run feature_engineering.py first.")
    st.stop()

df = pd.read_csv(data_path)
df["Date"] = pd.to_datetime(df["Date"])
df = df.dropna()

# --- Price Trend ---
st.subheader("📈 Stock Price Trend")
st.line_chart(df.set_index("Date")["Close"])

# --- Sentiment Context ---
st.subheader("📌 Market Context (NLP-based)")

latest = df.iloc[-1]
sentiment_value = latest["daily_sentiment"]

if sentiment_value > 0.1:
    st.info("🟢 Market sentiment is **Positive** based on recent financial news.")
elif sentiment_value < -0.1:
    st.warning("🔴 Market sentiment is **Negative** based on recent financial news.")
else:
    st.write("🟡 Market sentiment is **Neutral**.")

st.write(
    """
    **Why this matters:**  
    - Sentiment does not directly predict price movement  
    - It provides contextual market understanding  
    - Traders can combine model output with sentiment awareness
    """
)
