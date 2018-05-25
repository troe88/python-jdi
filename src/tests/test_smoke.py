import pytest

from po.JdiSite import JdiSite
from tests.base.BaseTestClass import BaseTestClass
from utils.ResourceLoader import ResourceLoader


@pytest.mark.jdi_smoke
@pytest.mark.usefixtures("site")
@pytest.mark.usefixtures("resources")
class TestSmoke(BaseTestClass):

    def test_open_home_page(self, site: JdiSite, resources: ResourceLoader):
        pass

    def test_login(self, site: JdiSite, resources: ResourceLoader):
        pass
