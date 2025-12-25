import streamlit as st
import pandas as pd

st.title("Stock Trend & Sentiment Analyzer")

data = pd.read_csv("data/stock_prices.csv")
st.line_chart(data['Close'])
