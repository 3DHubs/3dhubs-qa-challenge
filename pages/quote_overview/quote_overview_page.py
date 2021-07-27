from pages.components.basic_element import BasicElement
from pages.quote_overview.quote_overview_page_locators import QuoteOverviewPageLocators


class QuoteOverviewPage:

    def __init__(self, driver):
        self.driver = driver

    @property
    def page_title(self):
        return BasicElement(self.driver, QuoteOverviewPageLocators.PAGE_TITLE)

    @property
    def part_description_title(self):
        return BasicElement(self.driver, QuoteOverviewPageLocators.PART_DESCRIPTION_TITLE)
