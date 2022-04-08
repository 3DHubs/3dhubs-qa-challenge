from selenium.webdriver.common.by import By


class ManufactureLocators:
    BUTTON_select_files = (By.XPATH, "//input[@id='file-btn']")
    INPUT_email_wall = (By.XPATH, "//input[@data-test='email-wall-input']")
    BUTTON_email_submit = (By.XPATH, "//button[@data-test='email-wall-submit']")
    IMAGE_analyzing_parts = (By.XPATH, "//img[@alt='Analyzing parts']")
    DIV_error_file_unsupported = (By.XPATH, "//div[contains(@class, 'part-upload-area__errors')]")
