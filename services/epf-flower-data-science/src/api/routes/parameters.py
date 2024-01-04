from fastapi import APIRouter, HTTPException
from src.services.parameters import train_model_fireparam, predict_flower_fireparam, add_parameters, update_parameters


router = APIRouter()
router.post("/add-parameters")
async def add_parameters_route(parameters: dict):
    """
    Adds parameters to the system.

    Args:
        parameters (dict): The parameters to be added.

    Returns:
        dict: Result of adding parameters or error message.
    """
    result = add_parameters(parameters)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result

@router.put("/update-parameters/{document_id}")
async def update_parameters_route(document_id: str, new_parameters: dict):
    """
    Updates parameters in the system.

    Args:
        document_id (str): The ID of the document to be updated.
        new_parameters (dict): The new parameters.

    Returns:
        dict: Result of updating parameters or error message.
    """
    result = update_parameters(document_id, new_parameters)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result

@router.get("/train-model-fireparam")
def train_model_route(test_size: float = 0.2, document_id: str = '42iGjY3IdVqGug0uNkO5'):
    """
    Trains a model using fire parameters.

    Args:
        test_size (float): The size of the test dataset.
        document_id (str): The ID of the document to use for training.

    Returns:
        dict: Result of the training process or error message.
    """
    result = train_model_fireparam(test_size, document_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result

@router.get("/predict-flower-fireparam")
def predict_flower_route(SepalLengthCm: float, SepalWidthCm: float, PetalLengthCm: float, PetalWidthCm: float):
    """
    Predicts a flower using fire parameters.

    Args:
        SepalLengthCm (float): Length of the sepal in centimeters.
        SepalWidthCm (float): Width of the sepal in centimeters.
        PetalLengthCm (float): Length of the petal in centimeters.
        PetalWidthCm (float): Width of the petal in centimeters.

    Returns:
        dict: Prediction result or error message.
    """
    result = predict_flower_fireparam(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result