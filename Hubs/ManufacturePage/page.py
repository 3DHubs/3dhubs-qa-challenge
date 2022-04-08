from selenium.webdriver.support import expected_conditions as ec

from Hubs.BasePage import BasePage
from Hubs.BaseWebElement import BaseWebElement
from Hubs.ManufacturePage.locators import ManufactureLocators


class ManufacturePage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

        self.expected_title = 'Get instant CNC machining, 3D printing & sheet metal fabrication quotes - Hubs'
        self.unexpected_page_contents = ["Oops, something went wrong"]

    @property
    def button_select_files(self) -> BaseWebElement:
        return BaseWebElement(self.driver, ManufactureLocators.BUTTON_select_files, ec.presence_of_element_located)

    @property
    def div_error_file_unsupported(self) -> BaseWebElement:
        return BaseWebElement(self.driver, ManufactureLocators.DIV_error_file_unsupported,
                              ec.presence_of_element_located, explicitly_wait_timeout=2)

    @property
    def input_email_wall(self) -> BaseWebElement:
        return BaseWebElement(self.driver, ManufactureLocators.INPUT_email_wall,
                              ec.presence_of_element_located)

    @property
    def button_email_submit(self) -> BaseWebElement:
        return BaseWebElement(self.driver, ManufactureLocators.BUTTON_email_submit, ec.presence_of_element_located)

    @property
    def img_analyzing_parts(self) -> BaseWebElement:
        return BaseWebElement(self.driver, ManufactureLocators.IMAGE_analyzing_parts, ec.presence_of_element_located)
