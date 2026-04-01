import requests

base_url = "http://127.0.0.1:8000"

session = requests.Session()

login_payload = {"username": "admin", "password": "password"}
login_response = session.post(f"{base_url}/login", json=login_payload)
print("login:", login_response.status_code, login_response.json())

user_response = session.get(f"{base_url}/user")
print("user:", user_response.status_code, user_response.json())
#login: 200 {'message': 'Login successful'}
#user: 200 {'username': 'admin', 'role': 'user'}
