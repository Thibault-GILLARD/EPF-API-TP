from fastapi import APIRouter , HTTPException
from src.services.analysis import train_model, predict_flower

router = APIRouter()

@router.get("/train-model")
def train_model_route(test_size: float = 0.2):
    """
    Trains a model for flower prediction.

    Args:
        test_size (float): Size of the test dataset (default is 0.2).

    Returns:
        dict: Result of the training process or error message.
    """
    result = train_model(test_size)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result

@router.get("/predict-flower")
def predict_flower_route(SepalLengthCm: float, SepalWidthCm: float, PetalLengthCm: float, PetalWidthCm: float):
    """
    Predicts a flower type based on given parameters.

    Args:
        SepalLengthCm (float)
        SepalWidthCm (float)
        PetalLengthCm (float)
        PetalWidthCm (float)

    Returns:
        dict: Prediction result or error message.
    """
    result = predict_flower(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result