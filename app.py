from fastapi import FastAPI
from fastapi.responses import FileResponse
from models import User

app = FastAPI()


# ===== Задание 1-1 =====
@app.get("/")
def read_root():
    return {"message": "Добро пожаловать в моё приложение FastAPI!"}


# ===== Задание 1-2 =====
# В исходных файлах здесь тоже был путь "/", поэтому в общем app.py
# вынесено на отдельный маршрут, чтобы не было конфликта роутов.
@app.get("/html")
def read_html():
    return FileResponse("index.html")


# ===== Задание 1-3 =====
@app.post("/calculate")
def calculate(num1: float, num2: float):
    return {"result": num1 + num2}

# ===== Задание 1_4 =====
user_data = {"id": "1", "name": "Зюзюков Александр"}
user = User(**user_data)


@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    return user
