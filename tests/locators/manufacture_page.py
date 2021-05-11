from selenium.webdriver.common.by import By


class ManufacturePageLocators:
    UPLOAD_SECTION = (By.CSS_SELECTOR, "input[id='file-btn']")
    EMAIL = (By.CSS_SELECTOR, "input[id='email']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "button.h3d-button.h3d-button--primary.u-margin-top-1.u-flex-1")
    UPLOAD_ERROR = (By.CSS_SELECTOR, "div.part-upload-area__errors.ng-star-inserted")
