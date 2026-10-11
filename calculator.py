from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Calculator CRUD API",
    description="Example API showing GET, POST, PUT and DELETE",
    version="1.0"
)


class NumberData(BaseModel):
    num1: float
    num2: float


# GET
@app.get("/calculator")
def get_calculator_info():
    return {
        "message": "Calculator API is running",
        "methods": ["GET", "POST", "PUT", "DELETE"]
    }


# POST
@app.post("/calculator/add")
def add_numbers(data: NumberData):
    return {
        "operation": "addition",
        "result": data.num1 + data.num2
    }


# PUT
@app.put("/calculator/update")
def update_numbers(data: NumberData):
    return {
        "message": "Values updated successfully",
        "num1": data.num1,
        "num2": data.num2
    }


# DELETE
@app.delete("/calculator/{record_id}")
def delete_record(record_id: int):
    return {
        "message": f"Record {record_id} deleted successfully"
    }