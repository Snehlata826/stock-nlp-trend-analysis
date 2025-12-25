import pandas as pd
from nlp_preprocessing import clean_text

def preprocess_news():
    news = pd.read_csv("data/news_data.csv")

    # Clean headlines
    news["clean_headline"] = news["Headline"].apply(clean_text)

    # Keep only required columns for now
    processed_news = news[["Date", "clean_headline", "Sentiment"]]

    processed_news.to_csv("data/news_cleaned.csv", index=False)
    print("Processed news saved to data/news_cleaned.csv")

if __name__ == "__main__":
    preprocess_news()
