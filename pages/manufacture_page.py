import allure

from pages.base_page import BasePage


class ManufacturePage(BasePage):
    @allure.step
    def select_sheet_metal(self):
        self.page.locator('//h3d-card[@data-test="technology-item-sheet-metal"]').click()

    @allure.step
    def select_file(self):
        self.page.locator('//input[@id="file-btn"]').set_input_files('test_data/sheet_metal_sample.step')

    @allure.step
    def agree_with_policy(self):
        self.page.locator('//button[contains(@class, "agree-and-upload")]').click()
