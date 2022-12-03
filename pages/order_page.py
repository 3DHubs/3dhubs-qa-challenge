import time
import pytest
from base.base_driver import BaseDriver
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class OrderPage(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    # Locators
    SKIP_BUTTON = ".h3d-button.order-review-walkthrough-dialog__secondary-btn.h3d-button--s.h3d-button--grey"
    NEW_QUOTE = "button[theme='dark'] span[class='h3d-button-wrapper']"
    PLACE_ORDER_BUTTON = "button[class='h3d-button h3d-button--m h3d-button--purple ng-star-inserted'] span[" \
                         "class='h3d-button-wrapper'] "
    CLOSE_BUTTON = "//button[@data-test='walkthrough-dialog-close-button']"
    START_NEW_QUOTE = "//button[@h3dtrackclick='qb-new-quote-dialog__start-new']"

    def get_start_new_quote_locator(self):
        return self.element_to_be_clickable(By.XPATH, self.START_NEW_QUOTE)

    def get_skip_button_locator(self):
        return self.element_to_be_clickable(By.CSS_SELECTOR, self.SKIP_BUTTON)

    def get_new_quote_locator(self):
        return self.element_to_be_clickable(By.CSS_SELECTOR, self.NEW_QUOTE)

    def get_place_order_button_locator(self):
        return self.element_to_be_clickable(By.CSS_SELECTOR, self.PLACE_ORDER_BUTTON)

    def get_close_button(self):
        return self.element_to_be_clickable(By.XPATH, self.CLOSE_BUTTON)

    def click_skip_button(self):
        self.get_skip_button_locator().click()

    def click_new_quote(self):
        self.get_new_quote_locator().click()

    def check_place_order_button(self):
        assert self.get_place_order_button_locator().is_enabled()

    def click_close_button(self):
        self.get_close_button().click()

    def click_start_new_quote_button(self):
        self.get_start_new_quote_locator().click()
        time.sleep(5)

