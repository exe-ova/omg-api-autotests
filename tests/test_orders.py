import pytest
from qase.pytest import qase
from clients.http_client import log_request
from models.dashboard import KPIsResponse, OrdersResponse


class TestGetKPIs:

    @qase.id(4)
    @qase.title("Get Orders w/ default params - get first 20 orders")
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

    @qase.id(5)
    @qase.title("Get Orders w/ custom params - get a requested data")
    @pytest.mark.smoke
    def test_get_w_custom_params_get_requested_order(self, dashboard_api):
        page_default = 1
        per_page_default = 20
        date = "2024-01-22"
        status = "cancelled"
        customer_name = "Laura Bennett"
        id = 979
        product = "Collaboration Hub"
        quantity = 10
        revenue = 859.5

        response = dashboard_api.get_orders(params={"start_date": date,
                                                    "end_date": date,
                                                    "status": status,
                                                    "search": customer_name,
                                                    "page_default": page_default,
                                                    "per_page_default": per_page_default})

        model = OrdersResponse(**response.json())
        assert response.status_code == 200
        assert model.page == page_default
        assert model.per_page == per_page_default
        assert len(model.orders) == 1
        assert model.orders[0].id == id
        assert model.orders[0].product == product
        assert model.orders[0].quantity == quantity
        assert model.orders[0].revenue == revenue

    @qase.id(6)
    @qase.title("Get Orders w/ custom params - get zero orders")
    @pytest.mark.smoke
    def test_get_0_orders(self, dashboard_api):
        page_default = 1
        per_page_default = 20
        order_date = "2024-01-05"
        status = "refunded"
        expected_orders = 0

        response = dashboard_api.get_orders(params={"start_date": order_date,
                                                    "end_date": order_date,
                                                    "status": status,
                                                    "page_default": page_default,
                                                    "per_page_default": per_page_default})

        model = OrdersResponse(**response.json())
        assert response.status_code == 200
        assert model.page == page_default
        assert model.per_page == per_page_default
        assert len(model.orders) == expected_orders