from pages.new_quote.new_quote_page import NewQuotePage
import config.config as config
from helpers.file_path_helper import FilePathHelper
from pages.new_quote.dialog_page_actions import DialogPageActions


class NewQuotePageActions:
    def __init__(self, driver):
        self.driver = driver
        self.new_quote_page = NewQuotePage(driver)
        self.file_path_helper = FilePathHelper

    def load(self):
        self.driver.get(config.UPLOAD_PAGE)

    def send_file(self, file):
        file_path = self.file_path_helper.get_file_absolute_path(self, file)
        self.new_quote_page.select_your_files_button.web_element.send_keys(file_path)
        return DialogPageActions(self.driver)

    def wait_for_validation_text(self):
        self.new_quote_page.validation_error_message.wait_for_element_to_be_visible()

    def get_validation_error_text(self):
        self.wait_for_validation_text()
        return self.new_quote_page.validation_error_message.web_element.text
