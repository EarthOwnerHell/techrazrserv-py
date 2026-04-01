import requests

url = "http://127.0.0.1:8000/products/search"
params = {
    "keyword": "Ноутбук",
    "category": "electronics",
    "limit": 5
}

response = requests.get(url, params=params)
print(response.json())
#[{'product_id': 1, 'name': 'Ноутбук Pro', 'category': 'electronics', 'price': 1299.99}]