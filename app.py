# app.py
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load("model.joblib")
vectorizer = joblib.load("vectorizer.joblib")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    review = data["review"]
    review_vec = vectorizer.transform([review])
    pred = model.predict(review_vec)
    return jsonify({"sentiment": pred[0]})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
