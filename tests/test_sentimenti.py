from src.sentiment import load_model, classify

def test_output_label():
    model = load_model()
    results = classify(["Covid cases are increasing fast!"], model)
    assert results[0]["label"] in ["positive", "neutral", "negative"]