import pytest
from clients.http_client import log_request
class TestGetKPIs:

    def test_get_default_kpis(self, dashboard_api):
        response = dashboard_api.get_kpis()
        body = response.json()
        assert response.status_code == 200
        assert response.json()["total_orders"] == 1000
        assert isinstance(body["total_revenue"], float)
        assert isinstance(body["avg_order_value"], float)

    def test_get_kpis_w_date_params(self, dashboard_api):
        response = dashboard_api.get_kpis(params={"start_date": "2024-01-01", "end_date": "2024-01-02"})
        body = response.json()
        assert response.status_code == 200
        assert isinstance(body["total_revenue"], float)
        assert isinstance(body["total_orders"], int)
        assert isinstance(body["avg_order_value"], float)