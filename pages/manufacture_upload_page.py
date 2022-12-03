from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.Utils import Utils
from test_cases.test_data import EXP_SELECT_TECHNOGLY_TEXT, EXP_UPLOAD_TEXT, EXP_PNG_FILES_TEXT , EXP_ORDERS_TITLE , EXP_QUOTES_TITLE


class UploadPage(BaseDriver):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait
        self.ut = Utils

    # Locators
    UPLOAD_TEXT = "//h4[contains(text(),'Upload your files to get an instant quote and DFM ')]"
    SELECT_TECHNOLOGY_TEXT = " //h4[normalize-space()='Select technology']"
    SELECT_FILE_BUTTON = "file-btn"
    DRAG_AND_DROP_FILE = '#file'
    LOG_IN_BUTTON = "//div[@class='h3d-navbar__item-text']"
    CNC_BUTTON = "//h3d-card[@data-test='technology-item-cnc-machining']"
    SHEET_METAL_BUTTON = "//h3d-card[@data-test='technology-item-sheet-metal']"
    PRINTING_3D_BUTTON = ".card__content[xpath = '1']"  # There is no 3D button on 12/01/2022
    PRINTING_3D_BUTTON_MJF = "//h5[normalize-space()='MJF']"
    PRINTING_3D_BUTTON_SLS = "//h5[normalize-space()='SLS']"
    PRINTING_3D_BUTTON_SLA = "//h5[normalize-space()='SLA']"
    PRINTING_3D_BUTTON_INDUSTRIAL_SLA = "//h5[normalize-space()='Industrial SLA']"
    PRINTING_3D_BUTTON_INDUSTRIAL_FDM = "//h5[normalize-space()='Industrial FDM']"
    # ANALYZING_YOUR_PARTS = "div[class='ng-star-inserted'] h5"
    QUOTES_BUTTON = "//a[@data-test='h3d-navbar__quotes']"  # check the title
    ORDERS_BUTTON = "//a[@data-test='h3d-navbar__orders']"
    NEW_QUOTE = "//span[normalize-space()='New quote']"
    FILE_TYPES = "body h3d-root b:nth-child(1)"
    FILE_SIZE = "body h3d-root b:nth-child(1)"
    PART_SIZE = "body h3d-root b:nth-child(1)"
    AGREE_BUTTON = '.h3d-button.agree-and-upload.h3d-button--m.h3d-button--purple'
    CLOSE_BUTTON = "//button[@data-test='walkthrough-dialog-close-button']"
    PNG_FILES_FAIL_TEXT = ".part-upload-area__errors.ng-star-inserted"

    def get_png_files_fail_text(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.PNG_FILES_FAIL_TEXT)

    def get_close_button(self):
        return self.element_to_be_clickable(By.XPATH, self.CLOSE_BUTTON)

    def get_cnc_button_locator(self):
        return self.driver.find_element(By.XPATH, self.CNC_BUTTON)

    def get_sheet_metal_locator(self):
        return self.driver.find_element(By.XPATH, self.SHEET_METAL_BUTTON)

    def get_3d_button_locator(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.PRINTING_3D_BUTTON)

    def get_3d_button_mjs_locator(self):
        return self.driver.find_element(By.XPATH, self.PRINTING_3D_BUTTON_MJF)

    def get_3d_button_sls_locator(self):
        return self.driver.find_element(By.XPATH, self.PRINTING_3D_BUTTON_SLS)

    def get_3d_button_sla_locator(self):
        return self.driver.find_element(By.XPATH, self.PRINTING_3D_BUTTON_SLA)

    def get_3d_button_ind_sla_locator(self):
        return self.driver.find_element(By.XPATH, self.PRINTING_3D_BUTTON_INDUSTRIAL_SLA)

    def get_3d_button_ind_fdm_locator(self):
        return self.driver.find_element(By.XPATH, self.PRINTING_3D_BUTTON_INDUSTRIAL_FDM)

    def get_upload_text_locator(self):
        return self.element_to_be_clickable(By.XPATH, self.UPLOAD_TEXT)

    def get_select_technology_text_locator(self):
        return self.element_to_be_clickable(By.XPATH, self.SELECT_TECHNOLOGY_TEXT)

    def get_select_file_button_locator(self):
        return self.element_to_be_clickable(By.ID, self.SELECT_FILE_BUTTON)

    def get_drag_and_drop_file_locator(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.DRAG_AND_DROP_FILE)

    def get_log_in_button_locator(self):
        return self.element_to_be_clickable(By.XPATH, self.LOG_IN_BUTTON)

    def get_quotes_button_locator(self):
        return self.driver.find_element(By.XPATH, self.QUOTES_BUTTON)

    def get_orders_button_locator(self):
        return self.driver.find_element(By.XPATH, self.ORDERS_BUTTON)

    def get_new_quote_button_locator(self):
        return self.driver.find_element(By.XPATH, self.NEW_QUOTE)

    def get_agree_button_locator(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.AGREE_BUTTON)

    def click_close_button(self):
        self.get_close_button().click()

    def file_upload(self, file_path):
        upload_file = self.get_drag_and_drop_file_locator()
        upload_file.send_keys(file_path)

    def click_agree_button(self):
        self.get_agree_button_locator().click()

    def check_upload_text(self):
        upload_text = self.get_upload_text_locator().text
        self.ut.assert_element(upload_text, EXP_UPLOAD_TEXT)

    def check_select_technology_text(self):
        select_technology_text = self.get_select_technology_text_locator().text
        self.ut.assert_element(select_technology_text, EXP_SELECT_TECHNOGLY_TEXT)

    def check_png_fail(self):
        png_files_text = self.get_png_files_fail_text().text
        self.ut.assert_element(png_files_text, EXP_PNG_FILES_TEXT)

    def click_log_in_button(self):
        self.get_log_in_button_locator().click()

    def check_the_quotes_button(self):
        quotes_title = self.get_quotes_button_locator().get_attribute('title')
        self.ut.assert_element(quotes_title, EXP_QUOTES_TITLE )

    def check_the_orders_button(self):
        orders_title = self.get_orders_button_locator().get_attribute('title')
        self.ut.assert_element(orders_title, EXP_ORDERS_TITLE )

    def check_the_new_quote(self):
        self.get_quotes_button_locator().is_enabled()

    def click_CNC_machining(self):
        self.get_cnc_button_locator().click()

    def click_3d_printing(self):
        pass

    def click_sheet_metal(self):
        self.get_sheet_metal_locator().click()
