from dataclasses import dataclass

from selenium.webdriver.support import expected_conditions as EC

import allure
import configs.config
from pages.base import BasePage


@dataclass
class Locators:
    signin_form_title: str = '//h1[text()="Вход в аккаунт"]'
    input_email: str = '//input[@name="email"]'
    input_password: str = '//input[@name="password"]'
    reset_password: str = '//a[@href="/reset-password"]'
    signup_link: str = '//a[@id="to-signup-link"]'
    submit_btn: str = '//button[@type="submit"]'


class SigninPage(BasePage):
    """Class for signin page"""

    page_url = configs.config.signin_page
    locators = Locators()

    @allure.step("Enter login")
    def enter_login(self, login: str) -> None:
        self.send_keys(self.locators.input_email, login)

    @allure.step("Enter password")
    def enter_password(self, password: str) -> None:
        self.send_keys(self.locators.input_password, password)

    @allure.step("Click submit button")
    def click_submit_button(self) -> None:
        self.click(self.locators.submit_btn)
