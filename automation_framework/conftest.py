import pytest

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="staging", help="Environment to run tests")

@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")

pytest_plugins = ["fixtures.auth_fixture"]

