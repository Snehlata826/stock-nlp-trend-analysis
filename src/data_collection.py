import streamlit as st
import pandas as pd
import os

st.title("📈 Stock Trend & Sentiment Analyzer")

file_path = "data/stock_prices.csv"

if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
    data = pd.read_csv(file_path)

    st.subheader("Stock Closing Price")
    st.line_chart(data["Close"])

    # Moving Averages
    data["MA_20"] = data["Close"].rolling(20).mean()
    data["MA_50"] = data["Close"].rolling(50).mean()

    st.subheader("Moving Averages")
    st.line_chart(data[["Close", "MA_20", "MA_50"]])

else:
    st.warning("Stock data not found. Run data_collection.py first.")
