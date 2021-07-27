from pages.components.basic_element import BasicElement
from pages.new_quote.new_quote_page_locators import UploadPageLocators


class NewQuotePage:

    def __init__(self, driver):
        self.driver = driver

    @property
    def select_your_files_button(self):
        return BasicElement(self.driver, UploadPageLocators.SELECT_FILES_BUTTON)

    @property
    def validation_error_message(self):
        return BasicElement(self.driver, UploadPageLocators.VALIDATION_MESSAGE)
