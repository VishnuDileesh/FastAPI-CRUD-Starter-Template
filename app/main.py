from fastapi import FastAPI

from app.api.v1.api import api_router
from app.logger import setup_logging

setup_logging()


app = FastAPI(title="Inkling Ebooks", version="1.0.0")

app.include_router(api_router, prefix="/api/v1")


@app.get("/", tags=["Health Check"])
def read_root():
    return {"status": "ok", "message": "Inkling Ebooks API is up!"}
