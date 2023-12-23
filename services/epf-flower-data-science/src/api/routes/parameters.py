from fastapi import APIRouter, HTTPException
from src.services.parameters import train_model_fireparam, predict_flower_fireparam, add_parameters, update_parameters


router = APIRouter()

@router.post("/add-parameters")
async def add_parameters_route(parameters: dict):
    result = add_parameters(parameters)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result

@router.put("/update-parameters/{document_id}")
async def update_parameters_route(document_id: str, new_parameters: dict):
    result = update_parameters(document_id, new_parameters)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result

@router.get("/train-model-fireparam")
def train_model_route(test_size: float = 0.2):
    result = train_model_fireparam(test_size)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result

@router.get("/predict-flower-fireparam")
def predict_flower_route(SepalLengthCm: float, SepalWidthCm: float, PetalLengthCm: float, PetalWidthCm: float):
    result = predict_flower_fireparam(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result