import allure
import pytest
from hamcrest import *

from po.JdiSite import JdiSite
from tests.base.BaseTestClass import BaseTestClass
from utils.ResourceLoader import ResourceLoader


@allure.story('Story1')
@allure.feature('Feature1')
@pytest.mark.jdi_criticalPath
@pytest.mark.usefixtures("site")
@pytest.mark.usefixtures("resources")
class TestClassCriticalPath(BaseTestClass):

    # @pytest.mark.skip(reason="I don't want run it")
    @allure.testcase('TESTCASE-1')
    def test_open_home_page(self, site: JdiSite, resources: ResourceLoader):
        """Home page can be opened"""
        expected_title = "Index Page1"

        site.open()
        title = site.get_title()
        with allure.step(f"Check that '{title}' equals to '{expected_title}'"):
            assert_that(title, equal_to(expected_title))

    @allure.testcase('TESTCASE-2')
    def test_user_can_login(self, site: JdiSite, resources: ResourceLoader):
        """Regular user can login in the system"""
        user = resources.get_user("user_1")

        site.open()
        site.home_page().login(user)
        actual = site.home_page().user_name()
        with allure.step(f"Check that '{actual}' equals to '{user.name()}'"):
            assert_that(actual, equal_to(user.name()))
