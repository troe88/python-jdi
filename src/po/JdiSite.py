__author__ = "Dmitry_Lebedev1"
__date__ = "25-May-18"

import allure
from selenium.webdriver.remote.webdriver import WebDriver

from po.pages.HomePage import HomePage


class JdiSite:

    def __init__(self, driver: WebDriver, base_url):
        self._home_page = HomePage(driver, f"{base_url}tests/index.htm")
        self._driver = driver

    def home_page(self):
        return self._home_page

    @allure.step('Open JDI site on Home page')
    def open(self):
        self.home_page().open()

    @allure.step('Get current page title')
    def get_title(self):
        return self._driver.title
