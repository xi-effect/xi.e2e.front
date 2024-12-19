from dataclasses import dataclass

import allure
from pages.base import BasePage


@dataclass
class Locators:
    """Class for welcome community create page locators"""

    title: str = '//*[@id="title"]'  # text Создайте сообщество
    upload_file: str = '//input[@type="file"]'
    community_name: str = '//input[@name="community"]'
    continue_btn: str = '//button[normalize-space()="Продолжить"]'
    go_back_btn: str = '//button[normalize-space()="Назад"]'


class WelcomeCommunityCreate(BasePage):
    """Class for welcome community create page elements"""

    locators: Locators = Locators()

    @allure.step("Enter community name")
    def enter_community_name(self, community_name: str) -> None:
        self.send_keys(self.locators.community_name, community_name)

    @allure.step("Click create button")
    def click_continue_button(self) -> None:
        self.click(self.locators.continue_btn)
