import re
from pydantic import BaseModel, Field, field_validator

class User(BaseModel):
    id: int
    name: str

class User2(BaseModel):
    name: str
    age: int

class Feedback(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    message: str = Field(..., min_length=10, max_length=500)

    @field_validator('message')
    @classmethod
    def validate_message(cls, value):
        lowered = value.lower()
        banned_patterns = [r"\bкринж\w*\b", r"\bрофл\w*\b", r"\bвайб\w*\b"]
        if any(re.search(pattern, lowered) for pattern in banned_patterns):
            raise ValueError("Использование недопустимых слов")
        return value
