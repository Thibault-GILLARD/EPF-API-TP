from google.cloud import firestore

class FirestoreClient:
    """Wrapper around a database"""

    client: firestore.Client

    def __init__(self) -> None:
        """Init the client."""
        self.client = firestore.Client.from_service_account_json('services/epf-flower-data-science/src/config/api-5a-firebase-adminsdk-g30qh-dd4ca83ef5.json')

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
        
    def add(self, collection_name: str, data: dict) -> None:
        """Add a document to a collection.
        Args:
            collection_name: The collection name
            data: The document data
        """
        try:
            doc_ref = self.client.collection(collection_name).add(data)
            return {"message": f"Document added with ID: {doc_ref.id}"}
        except Exception as e:
            return {"error": f"Error adding document: {e}"}
        
    def update(self, collection_name: str, document_id: str, data: dict) -> None:
        """Update a document in a collection.
        Args:
            collection_name: The collection name
            document_id: The document id
            data: The document data
        """
        try:
            doc_ref = self.client.collection(collection_name).document(document_id)
            doc_ref.update(data)
            return {"message": f"Document updated with ID: {doc_ref.id}"}
        except Exception as e:
            return {"error": f"Error updating document: {e}"}
        
        
        
    