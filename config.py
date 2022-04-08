import os

from selenium.common.exceptions import *


class DriveParams:
    explicitly_wait_timeout = 20
    implicitly_wait_timeout = 1
    wait_ignored_exceptions = [ElementNotVisibleException, ElementNotSelectableException,
                               ElementNotInteractableException]
    poll_frequency = 0.5


class TestParams:
    TEST_PAGE = 'https://www.hubs.com/manufacture/'
    EMAIL_USERNAME = 'some@gmail.com'
    TEST_FILE_LOCATION = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_files')
    STATIC_VALID_TEST_FILE = '1-1x-6._electronic_enclosure_v11_original-original.step'
    BAD_TEST_FILE = 'some.txt'


class TestBehaviour:
    FAIL_ON_ELEM_ARIA_MISMATCH = False
    FAIL_ON_ELEM_DISPLAY_MISMATCH = False
