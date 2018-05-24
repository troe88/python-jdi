import pytest


def pytest_addoption(parser):
    parser.addoption("--domain", action="store", default="qa",
                     help="Specify domain")
    parser.addoption("--browser", action="store", default="chrome",
                     help="Specify browser type")


@pytest.fixture
def my_opt(request):
    return {
        "domain": request.config.getoption("--domain"),
        "browser": request.config.getoption("--browser")
    }
