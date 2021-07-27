from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.TAG_NAME, "button")

