import requests
url = "http://127.0.0.1:8000/create_user"
data = {
    "name": "Alice",
    "email": "alice@example.com",
    "age": 30,
    "is_subscribed": True
}

response = requests.post(url, json=data)
print(response.json())
#Вернет: {'name': 'Alice', 'email': 'alice@example.com', 'age': 30, 'is_subscribed': True, 'is_adult': True}