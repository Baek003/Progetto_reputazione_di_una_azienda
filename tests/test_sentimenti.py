from src.sentimenti import load_model, load_dataset_sentiment, classify

def test_load_model():
    model = load_model()
    assert model is not None

def test_load_dataset():
    texts = load_dataset_sentiment()
    assert len(texts) == 10
    assert isinstance(texts[0], str)

def test_classify():
    model = load_model()
    texts = ["I love this!", "This is terrible!"]
    results = classify(texts, model)
    
    assert len(results) == 2
    for result in results:
        assert "label" in result
        assert "score" in result
        assert result["label"] in ["positive", "neutral", "negative"]
        assert 0 <= result["score"] <= 1