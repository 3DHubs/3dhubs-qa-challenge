import allure

from pages.base_page import BasePage


class OrdersPage(BasePage):
    @allure.step
    def close_walkthrough_popup(self):
        self.page.locator('//button[@data-test="walkthrough-dialog-close-button"]').click()

    @allure.step
    def click_new_quote(self):
        self.page.locator('//div[@data-test="h3d-navbar__new-quote"]').click()
