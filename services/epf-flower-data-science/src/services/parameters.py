import joblib
import pandas as pd
from src.services.data import split_dataset  # Importing the split_dataset function
from google.cloud import firestore
from sklearn.linear_model import LogisticRegression

class FirestoreClient:
    """Wrapper around a database"""

    client: firestore.Client

    def __init__(self) -> None:
        """Init the client."""
        self.client = firestore.Client.from_service_account_json('path/to/your/api-5a-firebase-adminsdk-g30qh-dd4ca83ef5.json')

    def get(self, collection_name: str, document_id: str) -> dict:
        """Find one document by ID.
        Args:
            collection_name: The collection name
            document_id: The document id
        Return:
            Document value.
        """
        doc_ref = self.client.collection(collection_name).document(document_id)
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict()
        raise FileExistsError(
            f"No document found at {collection_name} with the id {document_id}"
        )

def train_model(test_size):
    try:
        dataset = pd.read_csv('src/data/Iris.csv')

        firestore_client = FirestoreClient()
        model_params = firestore_client.get('parameters', '42iGjY3IdVqGug0uNkO5')  # Get parameters from Firestore

        X_train, X_test, y_train, y_test = split_dataset(test_size)

        model = LogisticRegression(**model_params)  

        model.fit(X_train, y_train)  

        joblib.dump(model, 'src/data/trained_model_fireparam.pkl')

        return {"status": "Model trained and saved successfully"}

    except Exception as e:
        return {"error": f"Error training model: {e}"}

def predict_flower(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm):
    try:
        model = joblib.load('src/data/trained_model_fireparam.pkl')
        prediction = model.predict([[SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]])
        return {"prediction": prediction[0]}

    except Exception as e:
        return {"error": f"Error predicting flower: {e}"}
