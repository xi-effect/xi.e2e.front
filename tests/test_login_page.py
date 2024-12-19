import time

import allure
from configs.config import Credentials
from data.person import Person, PersonCreateInfo
from tests.base_test import BaseTest


class TestLoginPage(BaseTest):

    @allure.title("Successfully signin")
    def test_signin(self):
        credentials = Credentials()
        with allure.step("Go to signin page"):
            self.signin.go_to_page()
            self.signin.is_page_opened()
        with allure.step("Fill form with test data"):
            self.signin.enter_login(credentials.test_login)
            self.signin.enter_password(credentials.test_password)
            self.signin.click_submit_button()
        assert self.dashboard.is_dashboard_page(), "We are not on dashboard page"
        assert self.dashboard.get_user_name() == "test"

    @allure.title("Successful registration with community creation")
    def test_signup_with_community_creation(self):
        with allure.step("Create person"):
            person: Person = PersonCreateInfo.user_create_info()
        with allure.step("Go to signup page"):
            self.signup.go_to_page()
            self.signup.is_page_opened()
        with allure.step("Fill form with person data"):
            self.signup.enter_username(person.username)
            self.signup.enter_login(person.email)
            self.signup.enter_password(person.password)
            self.signin.click_submit_button()
        with allure.step("Enter display name and submit"):
            self.welcome_user_info.enter_display_name(person.display_name)
            self.signin.click_submit_button()
        with allure.step("Create community"):
            self.welcome_community.click_create_button()
            self.welcome_community.click_continue_button()
            self.welcome_community_create.enter_community_name(person.community_name)
            self.welcome_community_create.click_continue_button()
            self.welcome_final.click_start_button()
        with allure.step("Check that we at community home page"):
            self.dashboard.is_dashboard_page()
        with allure.step("Verify community name"):
            assert (
                person.community_name == self.dashboard.get_community_name()
            )  # in welcome title, check it
            assert person.community_name == self.dashboard.get_community_profile_title()
        with allure.step("Verify user role"):
            assert self.dashboard.is_admin_user_role()
        with allure.step("Check user data in profile menu"):
            assert person.display_name == self.dashboard.get_display_name()
            assert person.username == self.dashboard.get_user_name()
        time.sleep(10)
