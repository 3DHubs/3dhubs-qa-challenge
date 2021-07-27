from pages.new_quote.dialog_page import DialogPage
from pages.quote_overview.quote_overview_page_actions import QuoteOverviewPageActions


class DialogPageActions:
    def __init__(self, driver):
        self.driver = driver
        self.dialog_page = DialogPage(driver)

    def wait_for_email_dialog_form(self):
        self.dialog_page.email_dialog_form.wait_for_element_to_be_visible()

    def is_email_dialog_form_visible(self):
        self.wait_for_email_dialog_form()
        return self.dialog_page.email_dialog_form.is_visible()

    def is_info_login_link_visible(self):
        return self.dialog_page.info_login_link.is_visible()

    def is_email_input_visible(self):
        return self.dialog_page.email_input.is_visible()

    def get_welcome_text(self):
        return self.dialog_page.welcome_header.web_element.text

    def get_paragraph_text(self):
        return self.dialog_page.info_paragraph.web_element.text

    def click_data_dialog_agree_button_if_visible(self):
        if self.dialog_page.agree_data_button.is_visible():
            self.dialog_page.agree_data_button.web_element.click()
        return QuoteOverviewPageActions(self.driver)
