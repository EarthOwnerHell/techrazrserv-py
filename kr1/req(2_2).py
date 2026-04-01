import requests
url = "http://127.0.0.1:8000/feedback"
data = {
"name": "А",
"message": "Мда, вайбок!"
}
response = requests.post(url, json=data)
print(response.json())
# Ожидаемо: {'detail': [{'type': 'string_too_short', 'loc': ['body', 'name'], 'msg': 'String should have at least 2 characters', 'input': 'А', 'ctx': {'min_length': 2}}, {'type': 'value_error', 'loc': ['body', 'message'], 'msg': 'Value error, Использование недопустимых слов', 'input': 'Мда, вайбок!', 'ctx': {'error': {}}}]}