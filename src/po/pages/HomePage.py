from selenium.webdriver.common.by import By

from entities import User
from po.core.BasePage import BasePage
from po.sections.LoginForm import LoginForm


class HomePage(BasePage):

    PROFILE_PHOTO = (By.CSS_SELECTOR, ".profile-photo")

    def __init__(self, driver, url) -> None:
        super().__init__(driver, url)
        self._login_form = LoginForm(driver)

    def login(self, user: User):
        self._f(*self.PROFILE_PHOTO).click()
        self._login_form.submit(user)

    def user_name(self):
        return self._f(*self.PROFILE_PHOTO).text
