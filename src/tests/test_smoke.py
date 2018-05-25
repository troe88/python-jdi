__author__ = "Dmitry_Lebedev1"
__date__ = "25-May-18"

import allure
import pytest
from hamcrest import assert_that, equal_to

from po.JdiSite import JdiSite
from tests.base.BaseTestClass import BaseTestClass
from utils.ResourceLoader import ResourceLoader


@allure.story('Story1')
@allure.feature('Feature2')
@pytest.mark.jdi
@pytest.mark.jdi_smoke
@pytest.mark.usefixtures("site")
@pytest.mark.usefixtures("resources")
class TestSmoke(BaseTestClass):

    @allure.testcase('TESTCASE-456')
    def test_failed_example(self,
                            site: JdiSite,
                            resources: ResourceLoader) -> None:
        """Example of failed test"""
        with allure.step("Example of failed step"):
            assert_that(True, equal_to(False))

    @allure.testcase('TESTCASE-432')
    @pytest.mark.skip(reason="I don't want run it")
    def test_skipped_example(self,
                             site: JdiSite,
                             resources: ResourceLoader) -> None:
        """Example of skipped test"""
        pass
