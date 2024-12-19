from dataclasses import dataclass

import allure
from pages.base import BasePage


@dataclass
class Locators:
    """Class for welcome community invite page locators"""

    invite_link: str = '//*[@class="relative"]/input'
    continue_btn: str = '//button[@type="submit"]'
    go_back_btn: str = '//button[normalize-space()="Назад"]'


class WelcomeCommunityInvite(BasePage):
    """Class for welcome community page elements"""

    # move submit button to components
