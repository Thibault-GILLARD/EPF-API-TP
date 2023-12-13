import requests
import os
from kaggle.api.kaggle_api_extended import KaggleApi

def download_iris_dataset():
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files('uciml/iris', path='src/data', unzip=True)

    return {"status": "Dataset downloaded successfully"}