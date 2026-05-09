import requests
import json
from config.settings import BASE_URL

class HttpClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})
        self.base_url = BASE_URL

    def get(self, path: str, params: dict = None) -> requests.Response:
        url = f"{self.base_url}{path}"
        return self.session.get(url, params=params)

def log_request(response):
    print("\n--- Request info ---")
    print(f"URL: {response.request.url}")
    print(f"method: {response.request.method}")
    print(f"status: {response.status_code}")
    try:
        print(f"<<< BODY: {json.dumps(response.json(), indent=2)}")
    except:
        print(f"<<< BODY: {response.text}")
    print("--------------------------\n")