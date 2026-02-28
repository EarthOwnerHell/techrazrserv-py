import requests
url = "http://127.0.0.1:8000/user"
data = {
    "name": "Александр",
    "age": 25
}

response = requests.post(url, json=data)
print(response.json())
#Вернет: {'name': 'Александр', 'age': 25, 'is_adult': True}