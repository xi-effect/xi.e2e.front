from dataclasses import dataclass

import allure
from pages.base import BasePage


@dataclass
class Locators:
    """Class for welcome user info page locators"""

    title: str = '//*[@id="title"]'
    upload_file: str = '//input[@type="file"]'
    display_name: str = '//input[@name="displayName"]'
    email: str = (
        '//label[normalize-space()="Электронная почта"]//following-sibling::node()[1]'
    )
    submit_btn: str = '//button[@type="submit"]'


class WelcomeUserInfo(BasePage):
    """Class for welcome user info page elements"""

    locators: Locators = Locators()

    @allure.step("Check that we on the welcome user info page")
    @allure.step("Enter display name")
    def enter_display_name(self, display_name: str) -> None:
        self.send_keys(self.locators.display_name, display_name)
