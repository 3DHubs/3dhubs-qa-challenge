from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.utils import LONG_WAIT


class QuoteOverviewPage:

    def __init__(self, driver):
        self.driver = driver

        self.save_quote_button = "//*[contains(@data-test,'quote-action-submit__save')]"
        self.start_production_button = "//*[contains(@data-test,'quote-action-submit__pay')]"
        self.total_price = "//*[contains(@class,'h3d-actions__total-price')]//span[@class='u-text-tnum ng-star-inserted']"

    def verify_quote_overview_page_displayed(self):
        WebDriverWait(self.driver, LONG_WAIT) \
            .until(expected_conditions.presence_of_element_located((By.XPATH, self.total_price)))

    def verify_total_price_displayed(self):
        WebDriverWait(self.driver, LONG_WAIT) \
            .until(expected_conditions.presence_of_element_located((By.XPATH, self.total_price)))
        print("total price is : " + self.driver.find_element_by_xpath(self.total_price).text)

    def verify_start_production_button_displayed(self):
        WebDriverWait(self.driver, LONG_WAIT) \
            .until(expected_conditions.presence_of_element_located((By.XPATH, self.start_production_button)))

    def verify_save_quote_button_displayed(self):
        WebDriverWait(self.driver, LONG_WAIT) \
            .until(expected_conditions.presence_of_element_located((By.XPATH, self.start_production_button)))
