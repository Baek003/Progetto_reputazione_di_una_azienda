from transformers import pipeline
from datasets import load_dataset


def load_model():
    model_path = "cardiffnlp/twitter-roberta-base-sentiment-latest"
    return pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)


def load_dataset_sentiment():
    dataset = load_dataset("tweet_eval", "sentiment")
    return dataset["test"]["text"][:10]


def classify(texts, model):
    results = []
    for text in texts:
        result = model(text)[0]
        results.append(result)
    return results