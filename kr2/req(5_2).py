import requests

base_url = "http://127.0.0.1:8000"

session = requests.Session()
login_payload = {"username": "admin", "password": "password"}

login_response = session.post(f"{base_url}/login", json=login_payload)
print("login:", login_response.status_code, login_response.json())

# Проверка защищенного маршрута
profile_response = session.get(f"{base_url}/profile")
print("profile:", profile_response.status_code, profile_response.json())
#login: 200 {'message': 'Login successful', 'user_id': '9811fd36-2e79-4792-b73a-f4a579114d8b'}
#profile: 200 {'user_id': '9811fd36-2e79-4792-b73a-f4a579114d8b', 'role': 'user'}
