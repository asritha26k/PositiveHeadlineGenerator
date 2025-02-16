from fastapi import FastAPI, Body
from fastapi.responses import PlainTextResponse
from model_loader import predict  # Import directly from model_loader.py

app = FastAPI()

@app.get("/")
def read_root():
    return "API is working!"

@app.post("/predict/", response_class=PlainTextResponse)
def get_prediction(text: str = Body(..., media_type="text/plain")):
    return predict(text)
