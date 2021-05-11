from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.locators.quote_page import QuotePageLocators
from tests.page_model.base_page import BasePage

TIMEOUT = 90


class QuotePage(BasePage):
    @property
    def base_url(self):
        return super(QuotePage, self).url + '/manufacture/order/'

    @property
    def price(self):
        return self.browser.find_element(*QuotePageLocators.TOTAL_PRICE)

    @property
    def error_messages(self):
        return self.browser.find_elements(*QuotePageLocators.ERROR_MESSAGE)

    @property
    def error_message_is_present(self):
        if self.error_messages:
            return True
        else:
            return False

    def close_intro_dialog(self):
        WebDriverWait(self.browser, TIMEOUT).until(
            expected_conditions.presence_of_element_located(QuotePageLocators.DIALOG_CLOSE_BUTTON)).click()
