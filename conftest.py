import pytest
from selenium import webdriver

from po.JdiSite import JdiSite
from utils.ResourceLoader import ResourceLoader
from utils.config import Config


def pytest_addoption(parser):
    parser.addoption("--domain", action="store", default="qa",
                     help="Specify domain")
    parser.addoption("--browser", action="store", default="chrome",
                     help="Specify browser type")


@pytest.fixture(scope="module")
def config() -> Config:
    return Config()


@pytest.fixture(scope="module")
def resources() -> ResourceLoader:
    return ResourceLoader()


@pytest.fixture(scope="module")
def site(my_opt, driver, config: Config) -> JdiSite:
    base_url = config.conf()["domains"][my_opt["domain"]]
    yield JdiSite(driver, base_url)
    driver.close()


@pytest.fixture(scope="module")
def driver(my_opt, config) -> webdriver:
    d = webdriver.Chrome(config.conf()["chrome.path"])
    d.set_page_load_timeout(config.conf()["page.load.timeout"])
    d.set_script_timeout(config.conf()["script.timeout"])
    d.implicitly_wait(config.conf()["implicitly.wait"])
    d.maximize_window()
    return d


@pytest.fixture(scope="module")
def my_opt(request):
    return {
        "domain": request.config.getoption("--domain"),
        "browser": request.config.getoption("--browser")
    }
