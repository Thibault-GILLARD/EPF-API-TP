import pytest
from src.services.utils import FirestoreClient
    
# Unit tests for the FirestoreClient class

class TestFirestoreClient:
    @pytest.fixture
    def firestore_client(self) -> FirestoreClient:
        """
        Test client for integration tests
        """
        return FirestoreClient()

    def test_get(self, firestore_client):
        # Setup some test data
        collection_name = "parameters"
        document_id = "test_document"

        # Call the function to be tested
        response = firestore_client.get(collection_name, document_id)

        # Assert the output
        assert response == {
            "test_param": "test_value"
        }
        
    def test_add(self, firestore_client):
        # Setup some test data
        collection_name = "parameters"
        data = {
            "test_param": "test_value"
        }

        # Call the function to be tested
        response = firestore_client.add(collection_name, data)

        # Assert the output
        assert response == {
            "message": "Document added with ID: test_document"
        }
        
    def test_update(self, firestore_client):
        # Setup some test data
        collection_name = "parameters"
        document_id = "test_document"
        data = {
            "test_param": "test_value"
        }

        # Call the function to be tested
        response = firestore_client.update(collection_name, document_id, data)

        # Assert the output
        assert response == {
            "message": "Document updated with ID: test_document"
        }
        