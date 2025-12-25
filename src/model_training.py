import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def train_model():
    # Load final dataset
    df = pd.read_csv("data/final_dataset.csv")

    # Drop rows with NaN values (from rolling indicators)
    df = df.dropna().reset_index(drop=True)

    # Create target variable (next-day movement)
    df["target"] = (df["Close"].shift(-1) > df["Close"]).astype(int)

    # Drop last row (no future price)
    df = df[:-1]

    # Features and target
    X = df[["MA_20", "Volatility", "daily_sentiment"]]
    y = df["target"]

    # Train-test split (time-aware)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    # Train model
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Evaluation
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))

    # ✅ SAVE MODEL (IMPORTANT)
    joblib.dump(model, "data/stock_sentiment_model.pkl")
    print("Model saved as data/stock_sentiment_model.pkl")

if __name__ == "__main__":
    train_model()
