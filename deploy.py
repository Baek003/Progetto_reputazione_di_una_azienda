import os
from huggingface_hub import HfApi

api = HfApi()

# Crea lo Space se non esiste
api.create_repo(
    repo_id="Baek003/Progetto_reputazione_di_una_azienda",
    repo_type="space",
    space_sdk="gradio",
    exist_ok=True,
    token=os.environ["HF_TOKEN"]
)

# Carica i file
api.upload_folder(
    folder_path=".",
    repo_id="Baek003/Progetto_reputazione_di_una_azienda",
    repo_type="space",
    token=os.environ["HF_TOKEN"],
    ignore_patterns=["*.pyc", "__pycache__", ".git", ".github"]
 )