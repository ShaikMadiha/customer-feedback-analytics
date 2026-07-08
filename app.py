from flask import Flask, render_template, request
import torch
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification

app = Flask(__name__)

# Load tokenizer and model
MODEL_PATH = "models/distilbert_model"

tokenizer = DistilBertTokenizerFast.from_pretrained(MODEL_PATH)
model = DistilBertForSequenceClassification.from_pretrained(MODEL_PATH)

model.eval()

labels = {
    0: "Negative",
    1: "Neutral",
    2: "Positive"
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    review = request.form["review"]

    inputs = tokenizer(
        review,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    with torch.no_grad():
        outputs = model(**inputs)

    probabilities = torch.nn.functional.softmax(
        outputs.logits,
        dim=1
    )[0]

    prediction = torch.argmax(probabilities).item()

    sentiment = labels[prediction]

    confidence = float(probabilities[prediction]) * 100

    result = {
        "review": review,
        "sentiment": sentiment,
        "confidence": round(confidence, 2),
        "positive": round(float(probabilities[2]) * 100, 2),
        "neutral": round(float(probabilities[1]) * 100, 2),
        "negative": round(float(probabilities[0]) * 100, 2),
    }

    return render_template(
        "index.html",
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)