__author__ = "Dmitry_Lebedev1"
__date__ = "25-May-18"

import allure
from selenium.webdriver.common.by import By

from entities import User
from po.core.BasePage import BasePage
from po.sections.LoginForm import LoginForm


class HomePage(BasePage):
    PROFILE_PHOTO = (By.CSS_SELECTOR, ".profile-photo")
    TITLE = "Index Page"

    def __init__(self, driver, url) -> None:
        super().__init__(driver, url)
        self._login_form = LoginForm(driver)

    @allure.step("Login on JDI site by {1}")
    def login(self, user: User):
        self._f(*self.PROFILE_PHOTO).click()
        self._login_form.submit(user)

    @allure.step("Get name of current User")
    def user_name(self):
        return self._f(*self.PROFILE_PHOTO).text
