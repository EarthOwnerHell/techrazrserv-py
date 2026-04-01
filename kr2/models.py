import re
from pydantic import BaseModel, Field, EmailStr, field_validator

class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    age: int = Field(..., ge=0, le=120)
    is_subscribed: bool = False

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        cleaned = value.strip()
        if cleaned != value:
            value = cleaned
        if not re.match(r"^[A-Za-zА-Яа-яЁё\s-]+$", value):
            raise ValueError("Имя может содержать только буквы, пробелы и дефисы")
        return value
    
class Product(BaseModel):
    product_id: int
    name: str
    category: str
    price: float

    @field_validator("price")
    @classmethod
    def validate_price(cls, value: float) -> float:
        if value <= 0:
            raise ValueError("Цена должна быть положительным числом")
        return value


class CommonHeaders(BaseModel):
    user_agent: str = Field(alias="User-Agent")
    accept_language: str = Field(alias="Accept-Language")

    @field_validator("accept_language")
    @classmethod
    def validate_accept_language(cls, value: str) -> str:
        # Пример формата: en-US,en;q=0.9,es;q=0.8
        pattern = r"^[A-Za-z]{1,8}(?:-[A-Za-z0-9]{1,8})?(?:\s*,\s*[A-Za-z]{1,8}(?:-[A-Za-z0-9]{1,8})?(?:;q=0(?:\.\d{1,3})?|;q=1(?:\.0{1,3})?)?)*$"
        if not re.match(pattern, value):
            raise ValueError("Неверный формат Accept-Language")
        return value
