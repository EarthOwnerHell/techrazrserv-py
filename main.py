from fastapi import FastAPI
app = FastAPI()

@app.post("/calculate")
def calculate(num1: float, num2: float):
    return {"result": num1 + num2}

#curl -X POST "http://127.0.0.1:8000/calculate?num1=7&num2=6"

#{"result":13.0}       