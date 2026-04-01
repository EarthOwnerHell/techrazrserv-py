import time
import requests

base_url = "http://127.0.0.1:8000"

session = requests.Session()
login_payload = {"username": "admin", "password": "password"}

login_response = session.post(f"{base_url}/login", json=login_payload)
print("login:", login_response.status_code, login_response.json())

# Запрос сразу (cookie не должна обновляться)
profile_response = session.get(f"{base_url}/profile")
print("profile t0:", profile_response.status_code, profile_response.json())

# Ждем ~4 минуты, чтобы попасть в окно продления (>=3 и <5 минут)
print("sleep 4 minutes...")
time.sleep(240)
profile_response = session.get(f"{base_url}/profile")
print("profile t+4:", profile_response.status_code, profile_response.json())

# Ждем ~6 минут, чтобы сессия истекла (>5 минут)
print("sleep 6 minutes...")
time.sleep(360)
profile_response = session.get(f"{base_url}/profile")
print("profile t+10:", profile_response.status_code, profile_response.json())

#login: 200 {'message': 'Login successful', 'user_id': '8f068f28-639c-45b9-98d7-b34130c7f55b'}
#profile t0: 200 {'user_id': '8f068f28-639c-45b9-98d7-b34130c7f55b', 'role': 'user'}
#sleep 4 minutes...
#profile t+4: 200 {'user_id': '8f068f28-639c-45b9-98d7-b34130c7f55b', 'role': 'user'}
#sleep 6 minutes...
#profile t+10: 200 {'user_id': '8f068f28-639c-45b9-98d7-b34130c7f55b', 'role': 'user'}