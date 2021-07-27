from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasicElement:

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.element = None

    @property
    def web_element(self):
        if not self.element:
            self.element = self.driver.find_element(*self.locator)
        return self.element

    def is_visible(self):
        try:
            element = self.web_element
            if element is not None:
                return True
            return False
        except Exception as e:
            return False

    def wait_for_element_to_be_visible(self, timeout=10, poll_frequency=0.5):
        wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency)
        element = wait.until(expected_conditions.visibility_of_element_located(self.locator))
        assert element
        self.element = element
