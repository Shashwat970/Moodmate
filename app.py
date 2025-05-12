from transformers import pipeline
import gradio as gr
import random
import csv
from collections import defaultdict

sentiment_pipeline = pipeline("sentiment-analysis")


def load_boosters(filepath="custom_sentiment.csv"):
    boosters = defaultdict(list)
    with open(filepath, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            label = row["label"].upper()
            boosters[label].append(row["text"])
    return boosters

boosters = load_boosters()

def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    sentiment = result["label"]
    score = result["score"]
    remedy = random.choice(boosters[sentiment])
    response = f"**Sentiment:** {sentiment} ({score:.2f})\n\n💬 **Suggestion:** {remedy}"
    return response

iface = gr.Interface(fn=analyze_sentiment,
                     inputs="text",
                     outputs="markdown",
                     title="MoodMate 🧠 Sentiment Chatbot",
                     description="Type something and get a mood booster!")

if __name__ == "__main__":
    iface.launch()
