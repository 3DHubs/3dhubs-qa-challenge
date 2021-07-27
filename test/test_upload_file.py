import pytest
from selenium.webdriver import Chrome
from pages.new_quote.new_quote_page_actions import NewQuotePageActions
from pages.login.login_page_actions import LoginPageActions
import time
import config.config as config
import pytest_check as check


class TestUploadFile:

    @pytest.fixture(autouse=True)
    def browser(self):
        driver = Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        yield driver
        driver.quit()

    @pytest.fixture()
    def load_page(self, browser):
        self.new_quote_page_actions = NewQuotePageActions(browser)
        self.new_quote_page_actions.load()

    @pytest.fixture()
    def login(self, browser):
        self.login_page_actions = LoginPageActions(browser)
        self.login_page_actions.load()
        self.login_page_actions.fill_email_input(config.TEST_USERNAME)
        self.login_page_actions.fill_password_input(config.TEST_PASSWORD)
        self.my_order_page_actions = self.login_page_actions.click_login_button()
        self.my_order_page_actions.wait_for_account_button_visible()

    @staticmethod
    def verify_dialog_elements_and_texts(self):
        check.is_true(self.dialog_page_actions.is_email_dialog_form_visible(),
                      "Check if email dialog form is displayed")
        check.is_in(config.DIALOG_WELCOME_STRING, self.dialog_page_actions.get_welcome_text(), "Check if welcome text "
                                                                                               "has proper string")
        check.is_in(config.DIALOG_PARAGRAPH_STRING, self.dialog_page_actions.get_paragraph_text(), "Check if "
                                                                                                   "paragraph has "
                                                                                                   "proper string")
        check.is_true(self.dialog_page_actions.is_info_login_link_visible(), "Check if login link is visible")
        check.is_true(self.dialog_page_actions.is_email_input_visible(), "Check if email input is visible")

    @staticmethod
    def verify_validation_message(self):
        check.is_in(config.NOT_SUPPORTED_MESSAGE, self.new_quote_page_actions.get_validation_error_text(), "Check "
                                                                                                           "validation "
                                                                                                           "error "
                                                                                                           "message")

    @staticmethod
    def verify_overview_page_titles(self, file):
        check.is_in(config.QUOTE_OVERVIEW_TITLE, self.quote_overview_page_actions.get_page_title_text())
        check.is_in(file, self.quote_overview_page_actions.get_part_description_title_text())

    # --- TESTS  ---
    @pytest.mark.parametrize("file", [config.STEP_FILE])
    def test_upload_file_without_login(self, load_page, file):
        self.dialog_page_actions = self.new_quote_page_actions.send_file(file)
        self.verify_dialog_elements_and_texts(self)

    @pytest.mark.parametrize("file", [config.JPG_FILE])
    def test_upload_unsupported_file(self, load_page, file):
        self.new_quote_page_actions.send_file(file)
        self.verify_validation_message(self)

    @pytest.mark.parametrize("file", [config.STEP_FILE, config.IGES_FILE, config.SAT_FILE, config.DXF_FILE])
    def test_upload_file_with_login(self, login, load_page, file):
        self.dialog_page_actions = self.new_quote_page_actions.send_file(file)
        self.quote_overview_page_actions = self.dialog_page_actions.click_data_dialog_agree_button_if_visible()
        self.verify_overview_page_titles(self, file)
