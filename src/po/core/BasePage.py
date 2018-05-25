__author__ = "Dmitry_Lebedev1"
__date__ = "25-May-18"

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage(object):
    def __init__(self, driver: WebDriver, url):
        self._url = url
        self._driver = driver
        self.timeout = 30

    def _f(self, *locator: By) -> WebElement:
        return self._driver.find_element(*locator)

    def open(self):
        self._driver.get(self._url)

    def get_title(self) -> str:
        return self._driver.title

    def get_url(self) -> str:
        return self._driver.current_url
