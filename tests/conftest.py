import pytest
from clients.http_client import HttpClient
from api.dashboard import DashboardApi

@pytest.fixture(scope="session")
def http_client():
    return HttpClient()

@pytest.fixture(scope="session")
def dashboard_api(http_client):
    return DashboardApi(http_client)