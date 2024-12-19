from dataclasses import dataclass

from pages.base import BasePage


@dataclass
class Locators:
    recovery_form_title: str = '//h1[text()="Восстановление"]'
    input_email: str = '//input[@name="email"]'
    submit_btn: str = '//button[@type="submit"]'
    signin_link: str = '//a[text()="Войти"]'


class Recovery(BasePage):
    locators: Locators = Locators()
