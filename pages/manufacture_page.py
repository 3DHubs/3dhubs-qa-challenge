"""
This module follows page object model and defines helper methods to identify the web elements in
the manufacture page.
"""
from os import path

import pyautogui    # type: ignore
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from manufacture_test_data import ManufactureTestData
from .common import CommonOps


class ManufacturePage(CommonOps):
    """
    This class inherits CommonOps class and defines locators and methods specific
    to the manufacture page.
    """

    START_A_NEW_QUOTE = (By.XPATH, "xpath=//h5[contains(text(),'Start a new quote')]")
    START_NEW_QUOTE = (By.XPATH,
                       "//span[@class='h3d-button-wrapper' and text()='Start new quote']")
    SELECT_TECHNOLOGY = (By.XPATH,
                         "//section[@class='container "
                         "new-quote-request__section new-quote-request__technology-selector']/h4")
    DDD_PRINTING = (By.XPATH,
                    "//h3d-wide-technology-selector[@class='ng-star-inserted']/"
                    "div[@class='wide-technology-selector']/div")
    SHEET_METAL = (By.XPATH,
                   "//h3d-wide-technology-selector[@class='ng-star-inserted']/"
                   "div[@class='wide-technology-selector']/div/following-sibling::h3d-card[2]")
    INDUSTRIAL_SLA = (By.XPATH,
                      "//*[@class='process-list-item__title' and text()=' Industrial SLA ']")
    SELECT_FILES = (By.XPATH,
                    "//input[@id='file']/following-sibling::button/span[text()='Select files']")
    WELCOME_TO_HUBS_POPUP = (By.XPATH,
                             "//*[text()='Welcome to Hubs']/following-sibling::p[contains(text(), "
                             "'To view your quo')]")
    EMAIL = (By.XPATH,
             "//form[@id='emailWallForm']/div/div/label[text()='Your work email']/"
             "following-sibling::input[@id='email']")
    GO_TO_YOUR_QUOTE = (By.XPATH, "//*[text()='Go to your quote']/parent::button")
    VIEW_DFM_ANALYSIS = (By.XPATH, "//button[@title='View DFM analysis']")
    HOW_TO_CHANGE_LEAD_TIME = (By.XPATH,
                               "//span[text()=' How to change lead time ']/parent::button")
    HOW_TO_CUSTOMISE_PARTS = (By.XPATH, "//span[text()=' How to customise parts ']/parent::button")
    CONTINUE_TO_YOUR_QUOTE = (By.XPATH, "//span[text()=' Continue to your quote ']/parent::button")

    def check_for_start_new_quote_popup(self):
        """
        Checks the Start_a_new_window popup window.

        :return: True, if popUp is found else False
        """
        try:
            self.wait_for(self.START_A_NEW_QUOTE)
            return True
        except TimeoutException:
            return False

    def click_on_start_new_quote_btn(self):
        """
        Clicks on start_new_quote button.

        :return: None
        """
        self.find(self.START_NEW_QUOTE).click()

    def check_for_select_technology_lbl(self):
        """
        Checks the select_technology title text.

        :return: True, if popUp is found else False
        """
        try:
            self.wait_for(self.SELECT_TECHNOLOGY)
            return True
        except TimeoutException:
            return False

    def click_on_three_d_printing_link(self):
        """
        Clicks on 3D Printing link or option.

        :return: None
        """
        self.find(self.DDD_PRINTING).click()

    def click_on_sheet_metal_link(self):
        """
        Clicks on Sheet Metal link or option.

        :return: None
        """
        self.find(self.SHEET_METAL).click()

    def select_industrial_sla_link(self):
        """
        Selects Industrial SLA option

        :return: None
        """
        self.find(self.INDUSTRIAL_SLA).click()

    def click_on_select_files_link(self):
        """
        Clicks on Select Files link or option.

        :return: None
        """
        self.find(self.SELECT_FILES).click()

    @staticmethod
    def upload_a_three_d_file():
        """
        Uploads a 3D printing file

        :return: None
        """
        if path.exists(ManufactureTestData.THREE_D_HORSE):
            pyautogui.typewrite(str(ManufactureTestData.THREE_D_HORSE), interval=0.01)
            pyautogui.press('enter')
            print(f"File: {ManufactureTestData.THREE_D_HORSE} has been uploaded.")
        else:
            print(f"FILE NOT FOUND: {ManufactureTestData.THREE_D_HORSE}")

    def check_for_welcome_to_hubs_popup(self):
        """
        Checks the welcome_to_hubs text in a popup.

        :return: True, if popUp is found else False
        """
        try:
            self.wait_for(self.WELCOME_TO_HUBS_POPUP)
            return True
        except TimeoutException:
            return False

    def enter_email_txt(self):
        """
        Enters the email to email textbox
        :return: None
        """
        self.find(self.EMAIL).send_keys('nag.rolli123@gmail.com')

    def click_on_go_to_your_quote_btn(self):
        """
        Clicks on GO_TO_YOUR_QUOTE button
        :return: None
        """
        self.find(self.GO_TO_YOUR_QUOTE).click()

    def check_for_view_dfm_analysis_btn(self):
        """
        Checks the view_dfm_analysis button.

        :return: True, if popUp is found else False
        """
        try:
            self.wait_for(self.VIEW_DFM_ANALYSIS)
            return True
        except TimeoutException:
            return False

    def check_for_parts_and_specification_popup(self):
        """
        Checks the Start_a_new_window popup window.

        :return: True, if popUp is found else False
        """
        try:
            self.wait_for(self.HOW_TO_CHANGE_LEAD_TIME)
            return True
        except TimeoutException:
            return False

    def click_on_parts_and_specification_popup_btn(self):
        """
        Clicks on the parts and specification popup button to come out of it.

        :return: None
        """
        assert self.check_for_parts_and_specification_popup() is True
        if self.check_for_parts_and_specification_popup():
            self.find(self.HOW_TO_CHANGE_LEAD_TIME).click()
            self.find(self.HOW_TO_CUSTOMISE_PARTS).click()
            self.find(self.CONTINUE_TO_YOUR_QUOTE).click()
