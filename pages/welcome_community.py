from dataclasses import dataclass

import allure
from pages.base import BasePage


@dataclass
class Locators:
    """Class for welcome community page locators"""

    title: str = '//*[@id="title"]'
    create_btn: str = (
        '//span[normalize-space()="Создать"]//ancestor::node()[2][@type="button"]'
    )
    join_btn: str = (
        '//span[normalize-space()="Присоединиться"]//ancestor::node()[2][@type="button"]'
    )
    continue_btn: str = '//button[normalize-space()="Продолжить"]'
    go_back_btn: str = '//button[normalize-space()="Назад"]'


class WelcomeCommunity(BasePage):
    """Class for welcome community page elements"""

    locators: Locators = Locators()

    @allure.step("Click create button")
    def click_create_button(self) -> None:
        self.click(self.locators.create_btn)

    @allure.step("Click continue button")
    def click_continue_button(self) -> None:
        self.click(self.locators.continue_btn)
