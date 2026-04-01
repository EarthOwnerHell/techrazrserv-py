import requests
url = "http://127.0.0.1:8000/feedback"
reviews = []  # Список для хранения отзывов
data = {
"name": "Александр",
"message": "Отличный день! Мне нравится ходить в школу!"
}

response = requests.post(url, json=data)
print(response.json())
#Вернет: {'message': 'Feedback received. Thank you, Александр.'}
