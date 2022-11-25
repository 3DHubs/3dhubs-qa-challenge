"""
This module defines pytest fixtures which can be accessed by all the tests which are defined within
the same folder.
"""
import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def get_driver():
    """
    Instantiates a firefox driver and launches the browser.
    It also maximizes the browser window and yields driver instance.

    :return: Web Driver instance (firefox)
    """
    url = 'https://www.hubs.com/'
    driver = webdriver.Firefox()
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.close()
