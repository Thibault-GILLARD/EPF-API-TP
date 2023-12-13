import requests
import os
from kaggle.api.kaggle_api_extended import KaggleApi

import pandas as pd
from sklearn.model_selection import train_test_split

def download_iris_dataset():
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files('uciml/iris', path='src/data', unzip=True)

    return {"status": "Dataset downloaded successfully"}

def load_iris_dataset():
    try:
        dataset = pd.read_csv('src/data/Iris.csv')
        return dataset
    except Exception as e:
        return {"error": f"Error loading dataset: {e}"}
    
def process_iris_dataset():
    try:
        dataset = pd.read_csv('src/data/Iris.csv')
        dataset = dataset.drop(['Id'], axis=1)
        return dataset
    except Exception as e:
        return {"error": f"Error processing dataset: {e}"}
    
def split_dataset(test_size):
    try:
        dataset = pd.read_csv('src/data/Iris.csv')
        dataset = dataset.drop(['Id'], axis=1)
        X = dataset.iloc[:, :-1].values
        y = dataset.iloc[:, -1].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=1)
        return {"X_train": X_train, "X_test": X_test, "y_train": y_train, "y_test": y_test}
    except Exception as e:
        return {"error": f"Error splitting dataset: {e}"}