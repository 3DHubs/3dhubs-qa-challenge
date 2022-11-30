import allure
from playwright.sync_api import expect

from pages.base_page import BasePage


class QuotePage(BasePage):
    @allure.step
    def close_walkthrough_popup(self):
        self.page.locator('//button[@data-test="walkthrough-dialog-close-button"]').click(timeout=60000)

    @allure.step
    def assert_quote_is_created(self):
        expect(self.page.locator('//div[@data-test="order-toolbar-title"]'))\
            .to_have_text('Untitled quote')
        expect(self.page.locator('//div[@class="line-items"]//h4'))\
            .to_have_text('Parts & specifications')
