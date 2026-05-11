import pytest
from pydantic import TypeAdapter
from qase.pytest import qase
from clients.http_client import log_request
from models.dashboard import RevenueChartItem


class TestGetRevenueChart:

    @qase.id(7)
    @qase.title("Get Revenue Chart w/o params - get (all) the data")
    @pytest.mark.smoke
    def test_get_default_chart(self, dashboard_api):
        response = dashboard_api.get_revenue_chart()

        assert response.status_code == 200
        adapter = TypeAdapter(list[RevenueChartItem])
        model = adapter.validate_python(response.json())
        assert len(model) > 0