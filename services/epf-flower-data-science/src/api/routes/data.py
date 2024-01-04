from fastapi import APIRouter, HTTPException
from src.services.data import download_iris_dataset, load_iris_dataset_, process_iris_dataset, split_dataset

router = APIRouter()

@router.get("/download-iris")
def download_iris():
    """Download the dataset"""
    return download_iris_dataset()

"""@router.get("/load-iris-dataset")
def get_iris_dataset():
    dataset = load_iris_dataset_()
    if "error" in dataset:
        raise HTTPException(status_code=404, detail=dataset["error"])
    return dataset"""

@router.get("/process-iris-dataset")
def get_processed_iris_dataset():
    """Process the dataset"""
    processed_data = process_iris_dataset()
    if "error" in processed_data:
        raise HTTPException(status_code=404, detail=processed_data["error"])
    return processed_data

@router.get("/split-iris-dataset")
def split_iris_dataset(test_size: float = 0.2):
    """Split the dataset into train and test sets"""
    result = split_dataset(test_size)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result