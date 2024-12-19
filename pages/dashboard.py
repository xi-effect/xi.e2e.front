from dataclasses import dataclass, field

from selenium.webdriver.support import expected_conditions as EC

import allure
from pages.base import BasePage


@dataclass
class UserProfileMenu:
    to_profile_btn: str = '//div[@id="user-profile-menu"]'  # root
    display_name: str = f"{to_profile_btn}//child::node()[2]/child::node()[1]"
    user_name: str = f"{to_profile_btn}//child::node()[2]/child::node()[2]"


@dataclass
class CommunityProfileMenu:
    root: str = '//div[@id="community-profile"]'
    community_profile_btn: str = f'{root}/parent::div[@type="button"]'
    community_profile_title: str = f"{root}/div[1]"


@dataclass
class Locators:
    title: str = "//h2"
    community_name: str = "//h2//following-sibling::node()/p"
    user_role: str = "//header/p"
    community_profile_menu: CommunityProfileMenu = field(
        default_factory=CommunityProfileMenu
    )
    user_profile_menu: UserProfileMenu = field(default_factory=UserProfileMenu)
    to_onboarding_btn: str = (
        '//span[text()="Пройти обучение"]//parent::node()[@type="button"]'
    )


class DashboardPage(BasePage):
    """Class for dashboard page"""

    locators: Locators = Locators()

    @allure.step("Check we at dashboard page")
    def is_dashboard_page(self) -> bool:
        title = self.generate_locator(self.locators.title)
        return self.wait.until(
            EC.text_to_be_present_in_element(title, "Добро пожаловать в сообщество")
        )

    def get_community_name(self) -> str:
        return self.get_element_text(self.locators.community_name)

    def get_user_name(self) -> str:
        return self.get_element_text(self.locators.user_profile_menu.user_name)

    def get_display_name(self) -> str:
        return self.get_element_text(self.locators.user_profile_menu.display_name)

    def get_community_profile_title(self) -> str:
        return self.get_element_text(
            self.locators.community_profile_menu.community_profile_title
        )

    @allure.step('Verify that the user role displayed on the UI is "Administrator"')
    def is_admin_user_role(self) -> bool:
        return "администратор" in self.get_element_text(self.locators.user_role)
