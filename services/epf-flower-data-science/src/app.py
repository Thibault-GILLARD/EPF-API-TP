from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from starlette.middleware.cors import CORSMiddleware

from src.api.router import router
import os
import requests
from fastapi import APIRouter

def get_application() -> FastAPI:
    application = FastAPI(
        title="epf-flower-data-science",
        description="Fast API",
        version="1.0.0",
        redoc_url=None,  # Disables ReDoc if you prefer only Swagger UI
    )

    @application.get("/", include_in_schema=False)
    def redirect_to_docs():
        return RedirectResponse(url='/docs')

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(router)
    return application