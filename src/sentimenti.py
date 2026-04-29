from transformers import pipeline

def load_model():
    model_path = "cardiffnlp/twitter-roberta-base-sentiment-latest"
    return pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)

def classify(texts, model):
    results = model(texts)
    return results