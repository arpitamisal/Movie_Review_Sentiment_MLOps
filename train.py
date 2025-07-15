# train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Sample data loading stub (replace with real IMDb dataset)
df = pd.read_csv(
    "IMDB_Dataset.csv"
)  # Make sure to include a 'review' and 'sentiment' column
X_train, X_test, y_train, y_test = train_test_split(
    df["review"], df["sentiment"], test_size=0.2, random_state=42
)

vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

model = LogisticRegression()
model.fit(X_train_vec, y_train)

joblib.dump(model, "model.joblib")
joblib.dump(vectorizer, "vectorizer.joblib")
