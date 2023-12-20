"""API Router for Fast API."""
from fastapi import APIRouter

from src.api.routes import hello, data, analysis, parameters
 
router = APIRouter()

router.include_router(hello.router, tags=["Hello"])
router.include_router(data.router, tags=["Data"])
router.include_router(analysis.router, tags=["Analysis"])
router.include_router(parameters.router, tags=["Analysis"])