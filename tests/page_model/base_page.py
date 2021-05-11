class BasePage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def url(self):
        return 'https://www.hubs.com'

    def open(self):
        self.browser.get(self.url)