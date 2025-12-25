import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon (run once)
nltk.download("vader_lexicon")

def perform_sentiment_analysis():
    # Load cleaned news data
    news = pd.read_csv("data/news_cleaned.csv")

    # Initialize VADER
    sia = SentimentIntensityAnalyzer()

    # Generate sentiment score
    news["sentiment_score"] = news["clean_headline"].apply(
        lambda x: sia.polarity_scores(str(x))["compound"]
    )

    # Save output
    news.to_csv("data/news_with_sentiment.csv", index=False)

    print("Sentiment analysis completed. Saved to data/news_with_sentiment.csv")

if __name__ == "__main__":
    perform_sentiment_analysis()
