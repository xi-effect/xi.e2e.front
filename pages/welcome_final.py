from dataclasses import dataclass

import allure
from pages.base import BasePage


@dataclass
class Locators:
    """Class for welcome community final page locators"""

    title: str = '//*[@id="title"]'  # text Добро пожаловать!
    show_tour_link: str = '//a[@href="/communities/1/home?show-tour=true"]'
    about_link: str = '//a[@href="href="https://xieffect.ru/"'
    start_button: str = '//button[normalize-space()="Начать работать"]'


class WelcomeFinal(BasePage):
    """Class for welcome final page elements"""

    locators: Locators = Locators()

    @allure.step("Click start button")
    def click_start_button(self):
        self.click(self.locators.start_button)
