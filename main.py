from fastapi import FastAPI
from pydantic import BaseModel
from model_loader import predict  # Import directly from model_loader.py

app = FastAPI()

class InputText(BaseModel):
    text: str

@app.post("/predict/")
def get_prediction(input_data: InputText):
    result = predict(input_data.text)
    return {"modified_text": result}
