from fastapi import FastAPI
from app.core.bootstrap.app import create_app

app: FastAPI = create_app()


@app.get("/")
def root():
    return {"message": "API is up and running"}


@app.get("/health")
def health():
    return {"status": "healthy"}