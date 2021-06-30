import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from enum import Enum


class UploadFileElements(Enum):
    UPLOAD_FILES_BUTTON = "/html/body/h3d-root/ng-component/h3d-page/main/div/h3d-new-quote-request/div/div/section[2]/div/h3d-part-upload-area/div/h3d-upload-area/div/div[1]/input"
    EMAIL = "//*[@name='email']"
    CONTINUE_BUTTON = "//*[text()=' Continue to your instant quote ']"
    DIALOG_CLOSE_BUTTON = "//mat-dialog-container//i"
    TOTAL_PRICE = "//h3d-quote-actions//span"
    PRICE = "//div[2]/div[5]/h3d-quote-part-price/span"
    QUANTITY = "//div[2]/div[4]"
    PRICE_PER_PART = "//div[2]/div[3]/h3d-quote-part-price/span"
    DETAILS = "//h3d-part-general-tolerance"
    MATERIAL_ROW1 = "//h3d-quote-part-specs//li[1]/span"
    MATERIAL_ROW2 = "//h3d-quote-part-specs/ul/li[2]"
    MATERIAL_ROW3 = "//h3d-quote-part-specs/ul/li[3]"
    NAME_OF_PART = "//h3d-quote-part-description/div/div[3]/div[1]"
    SIZE_OF_PART = "//h3d-quote-part-description/div/div[3]/div[2]"
    IMAGE = "//h3d-viewer-thumb/img"
    SHIPPED_DATE = "//h3d-quote-requirements-editor/div/div[1]/div[1]/div[2]/div[2]"
    DELIVER_DATE = "//h3d-quote-requirements-editor/div/div[2]/div[1]/div[2]/div[2]"
    TECHNOLOGY = "//h3d-quote-requirements-editor/div/div[3]/div[1]/div[2]/div[2]"
    SHIPPING_PRICE = "//h3d-quote-parts-table/div/div[3]/div[1]/div[2]/h3d-quote-part-price/span"
    SUBTOTAL_PRICE = "//h3d-quote-parts-table/div/div[3]/div[2]/h3d-quote-part-price/span"
    TOTAL_BUY_PRICE = "//h3d-quote-parts-table/div/div[3]/div[3]/h3d-quote-total-price/h3d-quote-part-price/span"
    ADD_ADDITIONAL_FILE = "//h3d-order-part-uploader/div/input"
    WRONG_FORMAT_MESSAGAE = "//div/h3d-part-upload-area/div/div[contains(text(), 'Please upload your parts in one of the following formats')]"
    BIG_SIZE_OF_FILE_MESSAGE = "//div/h3d-part-upload-area/div/div[contains(text(), 'This file is too large. We support files up to 128 MB.')]"



def find_element_explicit(driver, element):
    """ Explicit wait, finds element by xpath """

    try:
        element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, element))
        )

        return element
    except TimeoutException:

        print("Cannot find element")
        return None


def find_element(driver, element):
    try:
        time.sleep(5)
        element = driver.find_element(By.XPATH, element)

        return element

    except TimeoutException:

        print("Cannot find element")
        return None

def take_part_info(driver, element, part_number):
    """ find part info by part number """

    part_info_path = f"//h3d-quote-parts-table/div/div[2]/div[{part_number}]" + element

    try:
        element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, part_info_path))
        )

        return element
    except TimeoutException:

        print("Cannot find element")
        return None