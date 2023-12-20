from fastapi import APIRouter , HTTPException
from src.services.analysis import train_model

router = APIRouter()

@router.get("/train-model")
def train_model_route(test_size: float = 0.2):
    result = train_model(test_size)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result
