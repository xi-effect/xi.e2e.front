import logging

import pytest
from _pytest.fixtures import SubRequest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--headed", action="store_true")


@pytest.fixture(scope="function", autouse=True)
def driver(request: SubRequest):
    browser_name = request.config.getoption("--browser").lower()
    headed_option = request.config.getoption("--headed")
    logging.info(f"Options {request.config}")

    match browser_name:
        case "chrome":
            chrome_options = webdriver.ChromeOptions()
            if not headed_option:
                chrome_options.add_argument("--headless")
            driver = webdriver.Chrome(options=chrome_options)
        case "firefox":
            firefox_options = webdriver.FirefoxOptions()
            if not headed_option:
                firefox_options.headless = True
            driver = webdriver.Firefox()
        case _:
            raise ValueError(f"Unknown browser {browser_name}")
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()
