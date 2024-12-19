import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.dashboard import DashboardPage
from pages.recovery import Recovery
from pages.signin import SigninPage
from pages.signup import SignupPage
from pages.welcome_community import WelcomeCommunity
from pages.welcome_community_create import WelcomeCommunityCreate
from pages.welcome_final import WelcomeFinal
from pages.welcome_user_info import WelcomeUserInfo


class BaseTest:
    driver: WebDriver
    signin: SigninPage
    signup: SignupPage
    recovery: Recovery
    dashboard: DashboardPage
    welcome_user_info: WelcomeUserInfo
    welcome_community: WelcomeCommunity
    welcome_community_create: WelcomeCommunityCreate
    welcome_final: WelcomeFinal

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.dashboard = DashboardPage(driver)
        request.cls.recovery = Recovery(driver)
        request.cls.signin = SigninPage(driver)
        request.cls.signup = SignupPage(driver)
        request.cls.welcome_user_info = WelcomeUserInfo(driver)
        request.cls.welcome_community = WelcomeCommunity(driver)
        request.cls.welcome_community_create = WelcomeCommunityCreate(driver)
        request.cls.welcome_final = WelcomeFinal(driver)
