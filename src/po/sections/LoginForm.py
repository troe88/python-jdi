__author__ = "Dmitry_Lebedev1"
__date__ = "25-May-18"

from selenium.webdriver.common.by import By

from po.core.BaseSection import BaseSection


class LoginForm(BaseSection):

    LOGIN = (By.CSS_SELECTOR, "#Login")
    PASSWORD = (By.CSS_SELECTOR, "#Password")
    ENTER = (By.CSS_SELECTOR, "form button")

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def submit(self, user) -> None:
        self._f(*self.LOGIN).send_keys(user.login())
        self._f(*self.PASSWORD).send_keys(user.password())
        self._f(*self.ENTER).click()
