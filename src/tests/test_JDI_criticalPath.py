import pytest
from hamcrest import *

from po.JdiSite import JdiSite
from tests.base.BaseTestClass import BaseTestClass
from utils.ResourceLoader import ResourceLoader


@pytest.mark.jdi_criticalPath
@pytest.mark.usefixtures("site")
@pytest.mark.usefixtures("resources")
class TestClass(BaseTestClass):

    @pytest.mark.skip(reason="I don't want run it")
    def test_open_home_page(self, site: JdiSite, resources: ResourceLoader):
        site.open()
        assert_that(site.get_title(), equal_to("Index Page1"))

    def test_login(self, site: JdiSite, resources: ResourceLoader):
        user = resources.get_user("user_1")

        site.open()
        site.home_page().login(user)
        assert_that(site.home_page().user_name(), equal_to(user.name()))
