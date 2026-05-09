from clients.http_client import HttpClient

class DashboardApi:
    def __init__(self, client: HttpClient):
        self.client = client

    def get_kpis(self) -> requests.Response:
        return self.client.get("/kpis")