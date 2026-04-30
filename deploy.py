import os
from huggingface_hub import HfApi

api = HfApi()
api.upload_folder(
    folder_path=".",
    repo_id="Baek003/Progetto_reputazione_di_una_azienda",
    repo_type="space",
    token=os.environ["HF_TOKEN"]
)