import os
import platform

import pytest
import logging
from selenium import webdriver

from tests.page_model.manufacture_page import ManufacturePage

PATH_TO_WINDOWS_CHROME_DRIVER = os.path.abspath(r'./chromedriver/windows/chromedriver.exe')
PATH_TO_LINUX_CHROME_DRIVER = os.path.abspath(r'./chromedriver/linux/chromedriver')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@pytest.fixture(scope='function')
def browser(request):
    if platform.system().lower() == 'windows':
        logger.info('start browser in windows...')
        browser = webdriver.Chrome(executable_path=PATH_TO_WINDOWS_CHROME_DRIVER)
    elif platform.system().lower() == 'linux':
        logger.info('start browser in linux...')
        browser = webdriver.Chrome(executable_path=PATH_TO_LINUX_CHROME_DRIVER)
    else:
        logger.error('TEST IS NOT AVAILABLE IN THIS SYSTEM!')
        pytest.exit(msg='Tests can only be executed in Windows or Linux system', returncode=2)
    manufacture_page = ManufacturePage(browser)
    logger.info('opening manufacture page...')
    manufacture_page.open()
    logger.info('waiting for upload section in manufacture page...')
    manufacture_page.wait_for_upload_section()
    yield browser
    logger.info('quit browser...')
    browser.quit()
