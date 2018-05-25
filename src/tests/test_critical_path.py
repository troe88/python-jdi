__author__ = "Dmitry_Lebedev1"
__date__ = "25-May-18"

import allure
import pytest
from hamcrest import equal_to, assert_that

from po.JdiSite import JdiSite
from tests.base.BaseTestClass import BaseTestClass
from utils.ResourceLoader import ResourceLoader


@allure.story('Story1')
@allure.feature('Feature1')
@pytest.mark.jdi
@pytest.mark.jdi_criticalPath
@pytest.mark.usefixtures("site")
@pytest.mark.usefixtures("resources")
class TestClassCriticalPath(BaseTestClass):

    @allure.testcase('TESTCASE-1')
    def test_open_home_page(self, site: JdiSite, resources: ResourceLoader):
        """Home page can be opened"""
        expected_title = "Index Page"

        site.open()
        title = site.get_title()
        with allure.step(f"Check that '{title}' equals to '{expected_title}'"):
            assert_that(title, equal_to(expected_title))

    @allure.testcase('TESTCASE-2')
    def test_user_can_login(self, site: JdiSite, resources: ResourceLoader):
        """Regular user can login in the system"""
        e_user = resources.get_user("user_1")

        site.open()
        site.home_page().login(e_user)
        a_user_name = site.home_page().user_name()
        with allure.step(f"Check '{a_user_name}' equals to '{e_user.name()}'"):
            assert_that(a_user_name, equal_to(e_user.name()))
