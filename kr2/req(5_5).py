import requests

base_url = "http://127.0.0.1:8000"

headers_ok = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.9,es;q=0.8",
}

resp_info = requests.get(f"{base_url}/info", headers=headers_ok)
print("info:", resp_info.status_code, resp_info.json())
print("X-Server-Time:", resp_info.headers.get("X-Server-Time"))

#info: 200 {'message': 'Добро пожаловать! Ваши заголовки успешно обработаны.', 'headers': {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)', 'Accept-Language': 'en-US,en;q=0.9,es;q=0.8'}}
#X-Server-Time: 2026-04-01T11:59:53