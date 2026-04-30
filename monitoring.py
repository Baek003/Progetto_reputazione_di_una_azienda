import json
import os
from datetime import datetime
from transformers import pipeline
from datasets import load_dataset

def load_model():
    model_path = "cardiffnlp/twitter-roberta-base-sentiment-latest"
    return pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)

def monitor():
    model = load_model()
    dataset = load_dataset("tweet_eval", "sentiment")
    texts = dataset["test"]["text"][:10]

    results = []
    for text in texts:
        result = model(text)[0]
        results.append({
            "timestamp": datetime.now().isoformat(),
            "text": text,
            "label": result["label"],
            "score": result["score"]
        })

    # Salva i risultati in un file JSON
    with open("monitoring_log.json", "w") as f:
        json.dump(results, f, indent=2)

    # Stampa un riepilogo
    labels = [r["label"] for r in results]
    print(f"Totale testi analizzati: {len(results)}")
    print(f"Positive: {labels.count('positive')}")
    print(f"Neutral:  {labels.count('neutral')}")
    print(f"Negative: {labels.count('negative')}")

if __name__ == "__main__":
    monitor()