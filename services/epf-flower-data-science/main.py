import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from fastapi import FastAPI, File, HTTPException
from pathlib import Path
import shutil

from src.app import get_application

app = get_application()

@app.get("/")
def redirect_to_docs():
    return RedirectResponse(url="/docs")

if __name__ == "__main__":
    uvicorn.run("main:app", debug=True, reload=True, port=8080)
