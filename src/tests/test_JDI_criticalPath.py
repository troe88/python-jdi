import allure
import pytest
from hamcrest import *

from po.JdiSite import JdiSite
from tests.base.BaseTestClass import BaseTestClass
from utils.ResourceLoader import ResourceLoader


@pytest.mark.jdi_criticalPath
@pytest.mark.usefixtures("site")
@pytest.mark.usefixtures("resources")
class TestClass(BaseTestClass):

    # @pytest.mark.skip(reason="I don't want run it")
    def test_open_home_page(self, site: JdiSite, resources: ResourceLoader):
        site.open()
        title = site.get_title()
        expected_title = "Index Page1"
        with allure.step(f"Check that '{title}' equals to '{expected_title}'"):
            assert_that(title, equal_to(expected_title))

    def test_login(self, site: JdiSite, resources: ResourceLoader):
        user = resources.get_user("user_1")

        site.open()
        site.home_page().login(user)
        actual = site.home_page().user_name()
        with allure.step(f"Check that '{actual}' equals to '{user.name()}'"):
            assert_that(actual, equal_to(user.name()))
