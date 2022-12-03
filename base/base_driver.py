from selenium.webdriver.support import expected_conditions as EC

class BaseDriver:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
    def element_to_be_clickable(self, locator_type, locator):
        element = self.wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element
