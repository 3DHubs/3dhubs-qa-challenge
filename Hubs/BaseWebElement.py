import logging

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from config import DriveParams, TestBehaviour


class BaseWebElement:

    def __init__(self, driver, locator, expected_condition=None,
                 explicitly_wait_timeout=DriveParams.explicitly_wait_timeout, ignore_exceptions: bool = False,
                 poll_frequency=DriveParams.poll_frequency, ignored_exceptions=DriveParams.wait_ignored_exceptions):

        self.logger = logging.getLogger()
        self.driver = driver
        self.locator = locator
        self.expected_condition = expected_condition
        self.ignore_exceptions = ignore_exceptions
        self._elem = None
        self.is_found = False
        self.found_without_wait = None

        self.wait = WebDriverWait(self.driver, timeout=explicitly_wait_timeout,
                                  poll_frequency=poll_frequency)
        self.wait_ignore_exceptions = WebDriverWait(self.driver, timeout=explicitly_wait_timeout,
                                                    poll_frequency=poll_frequency,
                                                    ignored_exceptions=ignored_exceptions)

    @property
    def element(self):
        if self._elem is None:
            self._elem = self.find_element(self.locator)
        return self._elem

    def find_element(self, locator):
        try:
            elem = self.driver.find_element(*locator)
            self.found_without_wait = True
            return elem
        except NoSuchElementException as e:
            if self.expected_condition is not None:
                self.logger.warning(
                    'Element was not found by locator: {}, waiting by provided conditions'.format(self.locator))

                elem = self.wait_for_element(self.locator, self.expected_condition,
                                             ignore_exceptions=self.ignore_exceptions)
                return elem
            else:
                raise NoSuchElementException('Element was not found by locator {}, error: {}'.format(self.locator, e))

    def wait_for_element(self, locator, expected_condition, ignore_exceptions=False):
        assert expected_condition in [ec.presence_of_element_located,
                                      ec.presence_of_all_elements_located,
                                      ec.visibility_of_element_located,
                                      ec.visibility_of_all_elements_located], \
            'Test failure: expected_condition is not supported'

        if ignore_exceptions:
            return self.wait_ignore_exceptions.until(expected_condition(locator),
                                                     message="Can't find element by locator {0}".format(locator))
        return self.wait.until(expected_condition(locator),
                               message="Can't find element by locator {0}".format(locator))

    def validate_elem(self, expected_aria_role, is_displayed: bool = True, text=None, **kwargs):
        self.validate_aria_role(expected_aria_role)
        self.validate_if_is_visible(is_displayed)
        self.validate_elem_text(text)
        self.logger.info('ElementID: {} is found, is_enabled: {}, is_visible: {}'.format(self.element.id,
                                                                                         self.element.is_enabled(),
                                                                                         self.element.is_displayed()))
        self.validate_custom_elem_props(**kwargs)

    def validate_custom_elem_props(self, **kwargs):
        for key, value in kwargs.items():
            try:
                assert getattr(self.element, key) == value, 'Element.{} is "{}", expected "{}"'.format(
                    key, getattr(self.element, key), value)
            except AttributeError:
                self.logger.warning('Requested custom element prop {} was not found'.format(key))

    def validate_elem_text(self, text):
        if text is not None:
            assert text in self.element.text, 'Element text is "{}", expected "{}"'.format(self.element.text, text)

    def validate_if_is_visible(self, is_displayed: bool = True):
        if is_displayed:
            if TestBehaviour.FAIL_ON_ELEM_DISPLAY_MISMATCH:
                assert self.element.is_displayed() is True, 'Element is expected to be visible (displayed)'
            else:
                if not self.element.is_displayed():
                    self.logger.warning('Ignoring wrong elem visibility, expected: {}, got: {}'.format(
                        is_displayed, self.element.is_displayed()))
        else:
            if TestBehaviour.FAIL_ON_ELEM_DISPLAY_MISMATCH:
                assert self.element.is_displayed() is False, 'Element is expected to be invisible (not displayed)'
            else:
                if self.element.is_displayed():
                    self.logger.warning('Ignoring wrong elem visibility, expected: {}, got: {}'.format(
                        is_displayed, self.element.is_displayed()))

    def validate_aria_role(self, expected_aria_role):
        if TestBehaviour.FAIL_ON_ELEM_ARIA_MISMATCH:
            assert self.element.aria_role == expected_aria_role, 'Wrong elem aria role, expected: {}, got: {}'.format(
                expected_aria_role, self.element.aria_role)
        else:
            if self.element.aria_role != expected_aria_role:
                self.logger.warning('Ignoring wrong elem aria role, expected: {}, got: {}'.format(
                    expected_aria_role, self.element.aria_role))

    '''
    @property
    def get_prop_prefix(self):
        return str(sys._getframe(1)).split(',')[3].replace('code ', '').split('_')[0].strip()
    '''
