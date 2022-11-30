import allure

from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step
    def fill_in_credentials_and_submit(self, email, password):
        self.page.locator('//input[@type="email"]').fill(email)
        self.page.locator('//input[@type="password"]').fill(password)
        self.page.locator('//button[@type="submit"]').click()
