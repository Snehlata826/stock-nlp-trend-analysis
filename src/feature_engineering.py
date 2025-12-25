import pandas as pd

def aggregate_daily_sentiment():
    # Load sentiment data
    news = pd.read_csv("data/news_with_sentiment.csv")

    # Convert Date to datetime
    news["Date"] = pd.to_datetime(news["Date"])

    # Aggregate sentiment by date (mean)
    daily_sentiment = (
        news.groupby("Date")["sentiment_score"]
        .mean()
        .reset_index()
        .rename(columns={"sentiment_score": "daily_sentiment"})
    )

    # Save result
    daily_sentiment.to_csv("data/daily_sentiment.csv", index=False)

    print("Daily sentiment aggregation completed.")

if __name__ == "__main__":
    aggregate_daily_sentiment()
