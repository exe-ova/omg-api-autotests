# omg-api-autotests

OMG Dashboard API tests

To run tests:
1. add .env file with:
  BASE_URL=...

To enable QASE integration:
1. Add to the .env file:
  QASE_TESTOPS_API_TOKEN=..
  QASE_TESTOPS_PROJECT=..
2. In the pytest.ini enable:
  addopts=..

