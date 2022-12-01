from uuid import uuid4

import allure
from playwright.sync_api import expect

from pages.base_page import BasePage


class ManufacturePage(BasePage):
    @allure.step
    def select_technology(self, technology):
        if technology == 'cnc_machining':
            locator = '//h3d-card[@data-test="technology-item-cnc-machining"]'
            # cnc is selected by default
            if 'h3d-card--selected' not in self.page.locator(locator).get_attribute('class'):
                self.page.locator(locator).click()
        elif technology == 'sheet_metal':
            locator = '//h3d-card[@data-test="technology-item-sheet-metal"]'
            self.page.locator(locator).click()
        else:
            raise Exception('Unexpected technology type')

    @allure.step
    def select_file(self, technology):
        if technology == 'cnc_machining':
            path = 'test_data/cnc_machining_sample.3dm'
        elif technology == 'sheet_metal':
            path = 'test_data/sheet_metal_sample.step'
        else:
            raise Exception('Unexpected technology type')
        self.page.locator('//input[@id="file-btn"]').set_input_files(path)

    @allure.step
    def agree_with_policy(self):
        self.page.locator('//button[contains(@class, "agree-and-upload")]').click()

    @allure.step
    def fill_in_email_in_popup(self):
        self.page.locator('//input[@type="email"]').fill(f'{str(uuid4())[:8]}@gmail.com')
        self.page.locator('//button[@data-test="email-wall-submit"]').click()

    @allure.step
    def select_wrong_format_file(self):
        self.page.locator('//input[@id="file-btn"]').set_input_files('test_data/image.jpg')

    @allure.step
    def expect_wrong_format_error(self):
        expect(self.page.locator('//div[@class="part-upload-area__errors ng-star-inserted"]'))
