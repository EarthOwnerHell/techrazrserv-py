from fastapi import FastAPI, Query, Request, Response, Form, HTTPException, Depends, Header
from fastapi.responses import FileResponse
from models import UserCreate, Product, CommonHeaders
import uuid
import time
from datetime import datetime
from itsdangerous import Signer, BadSignature


app = FastAPI()
users = []
products = [
    {"product_id": 1, "name": "Ноутбук Pro", "category": "electronics", "price": 1299.99},
    {"product_id": 2, "name": "Наушники NoiseX", "category": "electronics", "price": 199.99},
    {"product_id": 3, "name": "Кофе Эспрессо", "category": "grocery", "price": 5.50},
    {"product_id": 4, "name": "Книга Python", "category": "books", "price": 29.90},
    {"product_id": 5, "name": "Кроссовки RunMax", "category": "sportswear", "price": 89.00},
]

SECRET_KEY = "dev-secret-key"
signer = Signer(SECRET_KEY)


# ===== Задание 3-1 =====
@app.post("/create_user")
def create_user(user: UserCreate):
    users.append(user)
    return {
        "name": user.name,
        "email": user.email,
        "age": user.age,
        "is_subscribed": user.is_subscribed,
        "is_adult": user.age >= 18,
    }


# ===== Задание 3-2=====
@app.get("/product/{product_id}", response_model=Product)
def get_product(product_id: int):
    return {"product_id": product_id, "name": "Продукт", "category": "Категория", "price": 100}
@app.get("/products/search", response_model=list[Product])
def search_products(
    keyword: str = Query(..., min_length=1),
    category: str | None = Query(None, min_length=1),
    limit: int = Query(10, ge=1),
):
    # поиск по ключевому слову и категории (если указана)
    kw_lower = keyword.lower()
    results = []
    for item in products:
        if kw_lower not in item["name"].lower():
            continue
        if category and item["category"].lower() != category.lower():
            continue
        results.append(item)
        if len(results) >= limit:
            break
    return results


# ===== Задание 5-2 / 5-3 =====
@app.post("/login")
async def login(
    request: Request,
    response: Response,
    username: str | None = Form(None),
    password: str | None = Form(None),
):
    if username is None or password is None:
        try:
            payload = await request.json()
        except Exception:
            payload = {}
        if username is None:
            username = payload.get("username")
        if password is None:
            password = payload.get("password")

    if not username or not password:
        raise HTTPException(status_code=400, detail="Missing credentials")

    if not (username == "admin" and password == "password"):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    user_id = str(uuid.uuid4())
    timestamp = int(time.time())
    payload = f"{user_id}.{timestamp}"
    token = signer.sign(payload).decode()
    response.set_cookie(
        key="session_token",
        value=token,
        httponly=True,
        secure=False,
        max_age=300,
        samesite="lax",
    )
    return {"message": "Login successful", "user_id": user_id}

@app.get("/profile")
def get_profile(request: Request, response: Response):
    token = request.cookies.get("session_token")
    if not token:
        response.status_code = 401
        return {"message": "Session expired"}

    try:
        payload = signer.unsign(token).decode()
    except BadSignature:
        response.status_code = 401
        return {"message": "Invalid session"}

    try:
        user_id, ts_raw = payload.split(".", 1)
        uuid.UUID(user_id)
        timestamp = int(ts_raw)
    except Exception:
        response.status_code = 401
        return {"message": "Invalid session"}

    now = int(time.time())
    if timestamp > now:
        response.status_code = 401
        return {"message": "Invalid session"}

    elapsed = now - timestamp
    if elapsed > 300:
        response.status_code = 401
        return {"message": "Session expired"}

    if 180 <= elapsed < 300:
        new_payload = f"{user_id}.{now}"
        new_token = signer.sign(new_payload).decode()
        response.set_cookie(
            key="session_token",
            value=new_token,
            httponly=True,
            secure=False,
            max_age=300,
            samesite="lax",
        )

    return {"user_id": user_id, "role": "user"}


# ===== Задание 5-4 / 5-5 =====
def get_common_headers(
    user_agent: str | None = Header(None),
    accept_language: str | None = Header(None),
) -> CommonHeaders:
    if not user_agent or not accept_language:
        raise HTTPException(status_code=400, detail="Missing required headers")
    return CommonHeaders(**{"User-Agent": user_agent, "Accept-Language": accept_language})


@app.get("/headers")
def read_headers(headers: CommonHeaders = Depends(get_common_headers)):
    return {
        "User-Agent": headers.user_agent,
        "Accept-Language": headers.accept_language,
    }


@app.get("/info")
def read_info(response: Response, headers: CommonHeaders = Depends(get_common_headers)):
    response.headers["X-Server-Time"] = datetime.now().isoformat(timespec="seconds")
    return {
        "message": "Добро пожаловать! Ваши заголовки успешно обработаны.",
        "headers": {
            "User-Agent": headers.user_agent,
            "Accept-Language": headers.accept_language,
        },
    }
