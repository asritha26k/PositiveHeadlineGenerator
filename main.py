from fastapi import FastAPI
from pydantic import BaseModel
from model_loader import predict  # Import directly from model_loader.py

app = FastAPI()

# Root endpoint to check if API is working
@app.get("/")
def read_root():
    return {"message": "API is working!"}

class InputText(BaseModel):
    text: str

@app.post("/predict/")
def get_prediction(input_data: InputText):
    result = predict(input_data.text)
    return {"modified_text": result}
