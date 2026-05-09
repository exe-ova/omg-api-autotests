import pytest

class TestGetKPIs:

    def test_get_default(self, dashboard_api):
        response = dashboard_api.get_kpis()
        assert response.status_code == 200
        assert response.json()["total_orders"] == 1000