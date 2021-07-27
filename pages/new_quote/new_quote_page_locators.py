from selenium.webdriver.common.by import By


class UploadPageLocators:
    SELECT_FILES_BUTTON = (By.ID, "file-btn")
    VALIDATION_MESSAGE = (By.XPATH, "//div[contains(@class, 'part-upload-area__errors')]")
    LOGIN_BUTTON = (By.XPATH, "")


class EmailDialogLocators:
    WELCOME_HEADER = (By.XPATH, "//*[@id='mat-dialog-0']//h4")
    INFO_PARAGRAPH = (By.XPATH, "//*[@id='mat-dialog-0']//p")
    INFO_LOGIN_LINK = (By.XPATH, "//*[@id='mat-dialog-0']//p//a")
    EMAIL_DIALOG_FORM = (By.ID, "emailWallForm")
    EMAIL_INPUT = (By.ID, "email")


class DataDialogLocators:
    AGREE_BUTTON = (By.XPATH, "//*[@id='mat-dialog-0']//button")
