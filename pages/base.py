from typing import Any

from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import allure


class BasePage:

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(driver, 20, poll_frequency=0.1)

    def go_to_page(self, url: str | None = None) -> None:
        if url is None:
            url = self.page_url
        with allure.step(f"Go to {url=!s}"):
            self.driver.get(url)

    def is_page_opened(self):
        with allure.step(f"Page {self.page_url=!s} is opened"):
            self.wait.until(EC.url_to_be(self.page_url))

    def make_screenschot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG,
        )

    @allure.step("Get text from element")
    def get_element_text(self, locator: str) -> str:
        element = self.get_element_by(locator)
        return element.text

    @staticmethod
    def generate_locator(locator_value: str, find_by: str = "xpath") -> tuple[Any, str]:
        """
        Generates a locator for finding an element on the web page.

        :param locator_value: The value of the locator (e.g., XPath expression).
        :param find_by: The type of the locator. Defaults to 'xpath'.
        :return: A tuple containing the By object and the locator value.
        :raises ValueError: If the provided locator type is unknown.
        """
        find_by = find_by.lower()
        locating = {
            "css": By.CSS_SELECTOR,
            "xpath": By.XPATH,
            "class_name": By.CLASS_NAME,
            "id": By.ID,
            "link_text": By.LINK_TEXT,
            "name": By.NAME,
            "partial_link_text": By.PARTIAL_LINK_TEXT,
            "tag_name": By.TAG_NAME,
        }
        try:
            by_type = locating[find_by]

        except KeyError:
            raise ValueError(f"Unknown locator type: {find_by}")
        result = by_type, locator_value
        return result

    def get_element_by(self, locator: str, find_by: str = "xpath") -> WebElement:
        """
        Finds an element on the web page using the specified locator
        and returns it once it's visible.

        :param locator: The value of the locator (e.g., CSS selector
                        or XPath expression).
        :param find_by: The type of the locator. Defaults to 'xpath'.
        :return: The located WebElement.
        :raises ValueError: If the provided locator type is unknown.
        """
        find_by = find_by.lower()
        locating = {
            "css": By.CSS_SELECTOR,
            "xpath": By.XPATH,
            "class_name": By.CLASS_NAME,
            "id": By.ID,
            "link_text": By.LINK_TEXT,
            "name": By.NAME,
            "partial_link_text": By.PARTIAL_LINK_TEXT,
            "tag_name": By.TAG_NAME,
        }

        try:
            by_type = locating[find_by]
        except KeyError:
            raise ValueError(f"Unknown locator type: {find_by}")
        element = self.wait.until(
            EC.visibility_of_element_located((by_type, locator))
        )  # to be visible
        return element

    def send_keys(self, locator: str, value: str) -> None:
        element = self.get_element_by(locator)
        self.wait.until(EC.element_to_be_clickable(element)).send_keys(value)

    def click(self, locator: str) -> None:
        element = self.get_element_by(locator)
        self.wait.until(EC.element_to_be_clickable(element)).click()
