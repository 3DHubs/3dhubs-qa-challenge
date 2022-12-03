import pytest
from base.base_driver import BaseDriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class LoginPage(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    #Login_information
    PASSWORD = "Test-Password-1"
    USER = "sahin.dirim@gmail.com"

    #Locator
    USER_MAIL_ADDRESS = "login-form__email"
    PASSWORD_INPUT = "login-form__password"
    LOG_IN_BUTTON = "//span[normalize-space()='Log in']"

    def get_mail_address_input_locator(self):
        return self.element_to_be_clickable(By.ID, self.USER_MAIL_ADDRESS)

    def get_password_input_locator(self):
        return self.element_to_be_clickable(By.ID, self.PASSWORD_INPUT)

    def get_log_in_button_locator(self):
        return self.element_to_be_clickable(By.XPATH, self.LOG_IN_BUTTON)

    def input_mail_adress_(self):
        self.get_mail_address_input_locator().send_keys(self.USER)

    def input_password(self):
        self.get_password_input_locator().send_keys(self.PASSWORD)

    def click_login_button(self):
        self.get_log_in_button_locator().click()