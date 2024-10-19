"""This module will expose the rest apis
"""

from fastapi import FastAPI
from pydantic import BaseModel

class CalculatorRequest(BaseModel):
    value1: int
    value2: int

class CalculatorResponse(BaseModel):
    value1: int
    value2: int
    result: int


app = FastAPI()

@app.get("/")
def home():
    return {"mesage": "home"}


@app.get("/add/{value_1}/{value_2}")
def add(value_1:int, value_2: int):
    return value_1 + value_2

@app.post("/sub",response_model=CalculatorResponse)
def sub(request: CalculatorRequest):
    response = CalculatorResponse(
        value1 = request.value1,
        value2 = request.value2,
        result = request.value1 - request.value2
    )
    return response

@app.post("/mul", response_model=CalculatorResponse)
def mul(request: CalculatorRequest):
    response = CalculatorResponse(
        value1 = request.value1,
        value2 = request.value2,
        result = request.value1 * request.value2
    )
    return response