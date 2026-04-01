import requests

base_url = "http://127.0.0.1:8000"

headers_ok = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.9,es;q=0.8",
}

headers_bad = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
}

resp_ok = requests.get(f"{base_url}/headers", headers=headers_ok)
print("headers ok:", resp_ok.status_code, resp_ok.json())

resp_bad = requests.get(f"{base_url}/headers", headers=headers_bad)
print("headers missing:", resp_bad.status_code, resp_bad.json())

#headers ok: 200 {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)', 'Accept-Language': 'en-US,en;q=0.9,es;q=0.8'}
#headers missing: 400 {'detail': 'Missing required headers'}