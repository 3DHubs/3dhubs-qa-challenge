"""
This module follows page object model and defines helper methods to identify
the web elements in the home page.
"""
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from .common import CommonOps


class HomePage(CommonOps):
    """
    This class inherits CommonOps class and defines locators and methods specific to the home page.
    """

    GET_INSTANT_QUOTE = (By.XPATH, "//div[@id='navbar__menu']/div/div/div[2]/a[contains(@href, "
                                   "'/manufacture/?technology=cnc-machining')]")

    def check_for_get_instant_quote(self) -> bool:
        """
        Checks get_instant_quote button present on the home page.

        :return: True or False
        """
        try:
            self.wait_for(self.GET_INSTANT_QUOTE)
            return True
        except TimeoutException:
            return False

    def click_get_instant_quote(self) -> None:
        """
        Clicks the GET INSTANT QUOTE button.

        :return:
        """
        self.find(self.GET_INSTANT_QUOTE).click()
