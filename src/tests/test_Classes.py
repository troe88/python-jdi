import pytest
from hamcrest import *
from selenium import webdriver

from po.JdiSite import JdiSite
from tests.base.BaseTestClass import BaseTestClass
from utils.Config import Config
from utils.ResourceLoader import ResourceLoader


@pytest.fixture
def site():
    config = Config()
    driver = webdriver.Chrome(config.conf()["chrome.path"])
    base_url = config.conf()["domain"]
    driver.maximize_window()
    yield JdiSite(driver, base_url)
    driver.close()


@pytest.fixture(scope="module")
def res():
    return ResourceLoader()


@pytest.mark.jdi
@pytest.mark.usefixtures("site")
@pytest.mark.usefixtures("res")
class TestClass(BaseTestClass):

    @pytest.mark.skip(reason="I don't want run it")
    def test_open_home_page(self, site: JdiSite, res: ResourceLoader):
        site.open()
        assert_that(site.get_title(), equal_to("Index Page"))

    def test_login(self, site: JdiSite, res: ResourceLoader):
        user = res.get_user("user_1")

        site.open()
        site.home_page().login(user)
        assert_that(site.home_page().user_name(), equal_to(user.name()))
