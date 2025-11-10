import pytest
import os

def pytest_configure(config):
    """Create a report file in the reports directory."""
    if not config.option.htmlpath:
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__)))
        reports_dir = os.path.join(project_root, "reports")
        if not os.path.exists(reports_dir):
            os.makedirs(reports_dir)
        config.option.htmlpath = os.path.join(reports_dir, "report.html")


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="staging", help="Environment to run tests")

@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")

pytest_plugins = ["fixtures.auth_fixture"]

