import pandas as pd

def merge_stock_and_sentiment():
    # Load stock data
    stock = pd.read_csv("data/stock_prices.csv")
    stock["Date"] = pd.to_datetime(stock["Date"])

    # Sort by date
    stock = stock.sort_values("Date")

    # Create technical indicators
    stock["MA_20"] = stock["Close"].rolling(window=20).mean()
    stock["Volatility"] = stock["Close"].rolling(window=20).std()

    # Load daily sentiment
    sentiment = pd.read_csv("data/daily_sentiment.csv")
    sentiment["Date"] = pd.to_datetime(sentiment["Date"])

    # Merge on Date
    final_df = pd.merge(stock, sentiment, on="Date", how="left")

    # Handle missing sentiment (no news that day)
    final_df["daily_sentiment"] = final_df["daily_sentiment"].fillna(0)

    # Keep relevant columns only
    final_df = final_df[
        ["Date", "Close", "MA_20", "Volatility", "daily_sentiment"]
    ]

    # Save final dataset
    final_df.to_csv("data/final_dataset.csv", index=False)

    print("Final dataset created successfully.")

if __name__ == "__main__":
    merge_stock_and_sentiment()
