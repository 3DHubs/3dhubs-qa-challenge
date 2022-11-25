"""
This module defines common operations like find element, wait for element etc.
"""
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


class CommonOps:
    """
    This class defines all the common operations which can be inherited to
    any page objects and can be used.
    """

    def __init__(self, driver):
        """
        Defining driver instance and web driver wait objects.
        Default wait time is set as 10 secs.

        :param driver: web driver instance
        """
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 100)

    def wait_for(self, locator):
        """
        Waits for the given web element to appear on the web page.
        If element is found, returns True else returns False

        :param locator: Web element locator
        :return: True or False
        """
        return self._wait.until(ec.presence_of_element_located(locator))

    def find(self, locator) -> WebElement:
        """
        Returns web element object based on the given locator

        :param locator: Web element locator
        :return: Web element
        """
        return self.driver.find_element(*locator)
