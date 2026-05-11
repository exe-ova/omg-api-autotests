import pytest
import platform
import os
from dotenv import load_dotenv
from datetime import datetime, timezone
from clients.http_client import HttpClient
from api.dashboard import DashboardApi

load_dotenv()

def pytest_configure(config):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H:%M:%S")

    scope = config.getoption("--scope", default="all")

    machine = os.getenv("CI_RUNNER_NAME", platform.node())

    run_title = f"{now}_{scope}_{machine}"

    os.environ["QASE_TESTOPS_RUN_TITLE"] = run_title

@pytest.fixture(scope="session")
def http_client():
    return HttpClient()

@pytest.fixture(scope="session")
def dashboard_api(http_client):
    return DashboardApi(http_client)

def pytest_addoption(parser):
    parser.addoption(
        "--scope",
        action="store",
        default="all",
        help="Scope сценариев: smoke, regression, sanity и т.д."
    )