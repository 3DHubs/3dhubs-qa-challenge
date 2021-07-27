from pages.components.basic_element import BasicElement
from pages.login.login_page_locators import LoginPageLocators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    @property
    def email_input(self):
        return BasicElement(self.driver, LoginPageLocators.EMAIL_INPUT)

    @property
    def password_input(self):
        return BasicElement(self.driver, LoginPageLocators.PASSWORD_INPUT)

    @property
    def login_button(self):
        return BasicElement(self.driver, LoginPageLocators.LOGIN_BUTTON)
