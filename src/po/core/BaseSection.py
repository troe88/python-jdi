__author__ = "Dmitry_Lebedev1"
__date__ = "25-May-18"

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BaseSection(object):
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _f(self, *locator) -> WebElement:
        return self._driver.find_element(*locator)
