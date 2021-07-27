from pages.components.basic_element import BasicElement
from pages.new_quote.new_quote_page_locators import UploadPageLocators, EmailDialogLocators, DataDialogLocators


class DialogPage:

    def __init__(self, driver):
        self.driver = driver

    @property
    def welcome_header(self):
        return BasicElement(self.driver, EmailDialogLocators.WELCOME_HEADER)

    @property
    def info_paragraph(self):
        return BasicElement(self.driver, EmailDialogLocators.INFO_PARAGRAPH)

    @property
    def info_login_link(self):
        return BasicElement(self.driver, EmailDialogLocators.INFO_LOGIN_LINK)

    @property
    def email_dialog_form(self):
        return BasicElement(self.driver, EmailDialogLocators.EMAIL_DIALOG_FORM)

    @property
    def email_input(self):
        return BasicElement(self.driver, EmailDialogLocators.EMAIL_INPUT)

    @property
    def agree_data_button(self):
        return BasicElement(self.driver, DataDialogLocators.AGREE_BUTTON)
