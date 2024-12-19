from dataclasses import dataclass

from selenium.webdriver.support import expected_conditions as EC

import allure
import configs.config
import data
from configs.config import signin_page
from data.person import Person, PersonCreateInfo
from pages.signin import SigninPage


@dataclass
class Locators:
    signup_form_title = "//h1"
    input_username: str = '//input[@name="username"]'
    input_email: str = '//input[@name="email"]'
    input_password: str = '//input[@name="password"]'
    signin_link: str = '//a[@href="/signin"]'
    submit_btn: str = '//button[@type="submit"]'


class SignupPage(SigninPage):
    """Class for signup page"""

    page_url = configs.config.signup_page
    locators = Locators()

    @allure.step("Enter username")
    def enter_username(self, username: str) -> None:
        self.send_keys(self.locators.input_username, username)

    @allure.step("Enter login")
    def enter_email(self, email: str) -> None:
        self.send_keys(self.locators.input_email, email)

    @allure.step("Enter password")
    def enter_password(self, password: str) -> None:
        self.send_keys(self.locators.input_password, password)

    @allure.step("Click submit button")
    def click_submit_button(self) -> None:
        self.click(self.locators.submit_btn)

    def go_to_signin_page(self) -> None: ...

    def is_signup_page(self) -> bool:
        title = ("xpath", self.locators.signup_form_title)
        return self.wait.until(EC.text_to_be_present_in_element(title, "Регистрация"))
