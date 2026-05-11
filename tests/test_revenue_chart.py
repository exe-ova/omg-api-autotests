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

    @qase.id(8)
    @qase.title("Get Revenue Chart w/ date params - get a requested data")
    @pytest.mark.smoke
    def test_get_w_date_params_get_requested(self, dashboard_api):
        date = "2024-01-04"
        revenue = 1135.5

        response = dashboard_api.get_revenue_chart(params={"start_date": date, "end_date": date})

        assert response.status_code == 200
        adapter = TypeAdapter(list[RevenueChartItem])
        model = adapter.validate_python(response.json())
        assert model[0].revenue == revenue
        assert model[0].month == date[:-3]

    @qase.id(9)
    @qase.title("Get Revenue Chart w/ date params - get empty chart")
    @pytest.mark.smoke
    def test_get_w_date_params_get_empty(self, dashboard_api):
        date = "2024-01-02"

        response = dashboard_api.get_revenue_chart(params={"start_date": date, "end_date": date})

        assert response.status_code == 200
        adapter = TypeAdapter(list[RevenueChartItem])
        model = adapter.validate_python(response.json())
        assert len(model) == 0