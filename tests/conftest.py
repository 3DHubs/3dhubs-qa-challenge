import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_DIR = os.path.dirname(os.path.abspath('../hubs/'))
CHROME_DRIVER_PATH = os.path.join(BASE_DIR, 'chromedriver')


def pytest_addoption(parser):
    """ Receives arguments from the command line """
    parser.addoption("--env", action="store", help="input env")
    parser.addoption("--headless", action="store", help="input headless")

@pytest.fixture(scope="class")
def params(request):
    """ Assign the arguments from the command line to variables """
    params = {}

    params['env'] = request.config.getoption('--env')
    params['headless'] = request.config.getoption('--headless')

    request.cls.params = params


@pytest.fixture(scope="function")
def setup_and_tear_down(request):

    chrome_options = Options()
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')

    # Checks inputted arguments via command line
    if request.cls.params['headless'] == "true":
        chrome_options.add_argument("--headless")

    if request.cls.params['env'] == "prod":
        environment = "https://www.hubs.com/manufacture/"

    # Starts web driver
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, chrome_options=chrome_options)

    # Open the website
    driver.get(environment)
    driver.maximize_window()
    time.sleep(10)

    # Assign driver to test class
    request.cls.driver = driver

    yield

    driver.close()
