import allure

from pages.base_page import BasePage


class HomePage(BasePage):
    @allure.step
    def open_home_page(self):
        self.page.goto('https://www.hubs.com/')

    @allure.step
    def open_login_page(self):
        self.page.locator('//span[@class="material-icons h3d-navbar__user-avatar"]').click()
        self.page.locator('//a[@href="/manufacture/login"]').click()

    @allure.step
    def get_instant_quote(self):
        self.page.locator('//div[@id="navbar__menu"]//a[@e2e="static_get_quote_header"]').click()
