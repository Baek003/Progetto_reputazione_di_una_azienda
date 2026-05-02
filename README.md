# Progetto Reputazione di una Azienda

## Descrizione
Sistema di monitoraggio della reputazione online basato su analisi del sentiment 
dei testi dai social media, sviluppato con metodologie MLOps.

## Modello
- Modello: cardiffnlp/twitter-roberta-base-sentiment-latest
- Dataset: tweet_eval (sentiment)
- Classificazione: positivo, neutro, negativo

## Struttura del progetto
- `src/sentimenti.py` — caricamento modello e classificazione
- `tests/test_sentimenti.py` — test automatici
- `monitoring.py` — monitoraggio continuo
- `deploy.py` — deploy automatico su HuggingFace
- `.github/workflows/ci.yml` — pipeline CI/CD

## Pipeline CI/CD
Ad ogni push su main GitHub Actions esegue automaticamente:
1. Installazione dipendenze
2. Controllo errori con flake8
3. Test automatici con pytest
4. Deploy su HuggingFace
5. Monitoraggio del sentiment

## HuggingFace Space
https://huggingface.co/spaces/Baek03/Progetto_reputazione_di_una_azienda

## Notebook Colab
https://colab.research.google.com/drive/1m0uDvPxt3F-I619GGmC89guxRPdieWG9
