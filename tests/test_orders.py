import pytest
from qase.pytest import qase
from clients.http_client import log_request
from models.dashboard import KPIsResponse, OrdersResponse


class TestGetKPIs:

    @qase.id(1)
    @qase.title("GET with default params - get (all) the data")
    @pytest.mark.smoke
    def test_get_default_20_orders(self, dashboard_api):
        page_default = 1
        per_page_default = 20

        response = dashboard_api.get_orders(params={"page_default": page_default, "per_page_default": per_page_default})

        model = OrdersResponse(**response.json())
        assert response.status_code == 200
        assert model.page == page_default
        assert model.per_page == per_page_default
        assert len(model.orders) == per_page_default