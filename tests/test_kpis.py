import pytest
from qase.pytest import qase
from clients.http_client import log_request
from models.dashboard import KPIsResponse

class TestGetKPIs:

    @qase.id(1)
    @qase.title("GET with default params - get (all) the data")
    @pytest.mark.smoke
    def test_get_default_kpis(self, dashboard_api):
        response = dashboard_api.get_kpis()

        model = KPIsResponse(**response.json())
        assert response.status_code == 200
        assert model.total_orders > 0
        assert model.total_revenue > 0
        assert model.avg_order_value > 0

    @qase.id(2)
    @qase.title("GET with custom params - get custom response")
    @pytest.mark.smoke
    def test_get_kpis_w_date_params(self, dashboard_api):
        start_date = "2024-01-04"
        end_date = "2024-01-04"
        expected_total_orders = 2
        expected_total_revenue = 1135.5
        expected_avg_order_value = 567.75

        response = dashboard_api.get_kpis(params={"start_date": start_date, "end_date": end_date})

        model = KPIsResponse(**response.json())
        assert response.status_code == 200
        assert model.total_orders == expected_total_orders
        assert model.total_revenue == expected_total_revenue
        assert model.avg_order_value == expected_avg_order_value