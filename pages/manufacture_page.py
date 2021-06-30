from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.quote_overview_page import QuoteOverviewPage
from utils.utils import SHORT_WAIT, LONG_WAIT


class ManufacturesPage:

    def __init__(self, driver):
        self.driver = driver

        self.select_your_files_link_id = "file-btn"
        self.email = "email"
        self.email_submit = "//*[@data-test='email-wall-submit']"
        self.error_msg_for_jpg_image_upload = "//*[@class='part-upload-area__errors ng-star-inserted']"

    def verify_manufacturepage_displyed(self):
        WebDriverWait(self.driver, LONG_WAIT) \
            .until(expected_conditions.presence_of_element_located((By.ID, self.select_your_files_link_id)))

    def upload_the_given_file_successfully_to_get_quotes(self, file_path):
        self.driver.find_element_by_id(self.select_your_files_link_id) \
            .send_keys(file_path)
        WebDriverWait(self.driver, SHORT_WAIT) \
            .until(expected_conditions.presence_of_element_located((By.ID, self.email)))

    def upload_multiple_files_successfully_to_get_quotes(self, multiple_file1, multiple_file2):
        self.driver.find_element_by_id(self.select_your_files_link_id) \
            .send_keys(multiple_file1 + "\n" + multiple_file2)
        WebDriverWait(self.driver, SHORT_WAIT) \
            .until(expected_conditions.presence_of_element_located((By.ID, self.email)))

    def enter_email_to_receive_quote(self, email_id):
        self.driver.find_element_by_id(self.email) \
            .send_keys(email_id)
        self.driver.find_element_by_xpath(self.email_submit) \
            .click()
        quote_overview_page = QuoteOverviewPage(self.driver)
        quote_overview_page.verify_quote_overview_page_displayed()
        quote_overview_page.verify_total_price_displayed()

    def try_to_upload_invalid_file_and_verify_error_message(self, invalid_file_path):
        self.driver.find_element_by_id(self.select_your_files_link_id) \
            .send_keys(invalid_file_path)
        WebDriverWait(self.driver, SHORT_WAIT) \
            .until(expected_conditions.presence_of_element_located((By.XPATH, self.error_msg_for_jpg_image_upload)))
