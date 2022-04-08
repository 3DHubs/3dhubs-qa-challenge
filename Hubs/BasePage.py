import logging


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.base_url = url

        self.expected_title = None
        self.unexpected_page_contents = None
        self.logger = logging.getLogger('Webpage')

    def load(self):
        return self.driver.get(self.base_url)
