import requests
from config.settings import BASE_URL

class HttpClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})
        self.base_url = BASE_URL

    def get(self, path: str, params: dict = None) -> requests.Response:
        url = f"{self.base_url}{path}"
        return self.session.get(url, params=params)