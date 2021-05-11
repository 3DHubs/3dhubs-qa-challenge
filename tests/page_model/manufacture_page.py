from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.locators.manufacture_page import ManufacturePageLocators
from tests.page_model.base_page import BasePage

TIMEOUT = 90


class ManufacturePage(BasePage):
    @property
    def url(self):
        return super(ManufacturePage, self).url + '/manufacture/'

    @property
    def upload_error(self):
        return self.browser.find_element(*ManufacturePageLocators.UPLOAD_ERROR)

    @property
    def upload_error_is_present(self):
        if self.upload_error:
            return True
        else:
            return False

    def wait_for_upload_section(self):
        WebDriverWait(self.browser, TIMEOUT).until(
            expected_conditions.presence_of_element_located(ManufacturePageLocators.UPLOAD_SECTION))

    def upload_file(self, element_abspath, email):
        self.browser.find_element(*ManufacturePageLocators.UPLOAD_SECTION).send_keys(element_abspath)
        WebDriverWait(self.browser, TIMEOUT).until(
            expected_conditions.presence_of_element_located(ManufacturePageLocators.EMAIL)).send_keys(email)
        self.browser.find_element(*ManufacturePageLocators.CONTINUE_BUTTON).click()

    def upload_file_in_non_design_type(self, element_abspath):
        self.browser.find_element(*ManufacturePageLocators.UPLOAD_SECTION).send_keys(element_abspath)

