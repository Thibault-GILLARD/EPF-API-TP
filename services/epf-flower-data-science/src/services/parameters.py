import joblib
import pandas as pd
from src.services.data import split_dataset  # Importing the split_dataset function
from google.cloud import firestore
from sklearn.ensemble import RandomForestClassifier
from src.services.utils import FirestoreClient
from fastapi import FastAPI

app = FastAPI()
firestore_client = FirestoreClient()  # Initialize your Firestore client

def update_parameters(document_id: str, new_parameters: dict):
    """
    Updates parameters in Firestore.

    Args:
        document_id (str): The document ID where the parameters are updated.
        new_parameters (dict): The new parameters to be updated.

    Returns:
        dict: Confirmation message or error message.
    """
    try:
        firestore_client.update("parameters", document_id, new_parameters)
        return {"message": "Parameters updated successfully"}
    except Exception as e:
        return {"error": f"Error updating parameters: {e}"}

def add_parameters(parameters: dict):
    """
    Adds parameters to Firestore.

    Args:
        parameters (dict): The parameters to be added.

    Returns:
        dict: Confirmation message or error message.
    """
    try:
        firestore_client.add("parameters", parameters)
        return {"message": "Parameters added successfully"}
    except Exception as e:
        return {"error": f"Error adding parameters: {e}"}

def train_model_fireparam(test_size, document_id: str):
    """
    Trains a model using parameters from Firestore.

    Args:
        test_size (float): Size of the test dataset.
        document_id (str): The document ID containing model parameters.

    Returns:
        dict: Result of the model training process or error message.
    """
    try:
        dataset = pd.read_csv('src/data/Iris.csv')
        firestore_client = FirestoreClient()
        model_params = firestore_client.get('parameters', document_id)

        X_train, X_test, y_train, y_test = split_dataset(test_size)

        model = RandomForestClassifier(**model_params)
        model.fit(X_train, y_train)
        joblib.dump(model, 'src/data/trained_model_fireparam.pkl')

        return {"status": "Model trained and saved successfully"}

    except Exception as e:
        return {"error": f"Error training model: {e}"}

def predict_flower_fireparam(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm):
    """
    Predicts a flower type using a trained model.

    Args:
        SepalLengthCm (float): Length of the sepal in centimeters.
        SepalWidthCm (float): Width of the sepal in centimeters.
        PetalLengthCm (float): Length of the petal in centimeters.
        PetalWidthCm (float): Width of the petal in centimeters.

    Returns:
        dict: Prediction result or error message.
    """
    try:
        model = joblib.load('src/data/trained_model_fireparam.pkl')
        prediction = model.predict([[SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]])
        return {"prediction": prediction[0]}

    except Exception as e:
        return {"error": f"Error predicting flower: {e}"}