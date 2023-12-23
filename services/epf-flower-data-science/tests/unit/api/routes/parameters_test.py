import pytest
from src.services.parameters import  FirestoreClient

def test_firestore_client():
    firestore_client = FirestoreClient()

    try:
        collection_name = "parameters"
        document_id = "your_document_id_here"
        result = firestore_client.get(collection_name, document_id)
        assert result is not None  # Check if the result is not None
    except Exception as e:
        pytest.fail(f"Error: {e}")
