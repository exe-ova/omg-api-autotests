from clients.http_client import HttpClient

class DashboardApi:
    def __init__(self, client: HttpClient):
        self.client = client

    def get_kpis(self, params: dict = None) -> requests.Response:
        return self.client.get("/kpis", params=params)

    def get_orders (self, params: dict = None) -> requests.Response:
        return self.client.get("/orders", params=params)

    def get_revenue_chart (self, params: dict = None) -> requests.Response:
        return self.client.get("/revenue-chart", params=params)