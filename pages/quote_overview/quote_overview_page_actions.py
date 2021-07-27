from pages.quote_overview.quote_overview_page import QuoteOverviewPage


class QuoteOverviewPageActions:
    def __init__(self, driver):
        self.driver = driver
        self.quote_overview_page = QuoteOverviewPage(driver)

    def wait_for_part_description_title(self):
        self.quote_overview_page.part_description_title.wait_for_element_to_be_visible(timeout=60, poll_frequency=1)

    def get_page_title_text(self):
        self.wait_for_part_description_title()
        return self.quote_overview_page.page_title.web_element.text

    def get_part_description_title_text(self):
        self.wait_for_part_description_title()
        return self.quote_overview_page.part_description_title.web_element.text
