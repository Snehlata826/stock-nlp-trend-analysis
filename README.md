# 📊 Stock Price Trend & Market Sentiment Analysis

## Overview
An end-to-end **Machine Learning and NLP project** that analyzes stock price trends and extracts **market sentiment from financial news** to provide contextual insights for decision-making.

---

## Problem
Stock prices are influenced by both **historical price movements** and **market sentiment** expressed through financial news.  
Traditional price-only models fail to capture this qualitative context.

---

## Solution
- Analyzed historical stock data using technical indicators (Moving Average, Volatility)
- Built an NLP pipeline to preprocess financial news headlines
- Applied sentiment analysis using **VADER**
- Trained and evaluated ML models
- Deployed insights using an interactive **Streamlit dashboard**

---

## Tech Stack
**Python · Pandas · Scikit-learn · NLTK (VADER) · Streamlit · Git**

---

## Model Evaluation

| Model | Features Used | Accuracy |
|------|--------------|----------|
| Baseline | MA, Volatility | ~0.52 |
| With Sentiment | MA, Volatility, Sentiment | ~0.50 |

> Sentiment is used as **contextual insight** rather than a direct predictor, reflecting real-world financial analytics practices.

---

## Features
- Stock price trend visualization
- Market sentiment interpretation (Positive / Neutral / Negative)
- Explainable insights alongside ML predictions

---

## How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
