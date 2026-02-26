from pydantic import BaseModel
from fastapi import FastAPI
app = FastAPI()

@app.get('/users/{user_id}, re')

class User(BaseModel):
    id: int
    name: str

