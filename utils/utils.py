import inspect

# CONSTANTS
import os

import moment

URL_3DS = "https://www.3dhubs.com/manufacture/"
URL = "https://opensource-demo.orangehrmlive.com/"
USERNAME = "Admin"
PASSWORD = "admin123"
SHORT_WAIT = 15
LONG_WAIT = 60


# FUNCTIONS
def get_current_function():
    return inspect.stack()[1][3]


def save_screenshot(driver, test_name):
    currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
    screenshotName = test_name + "_screenshot_" + currTime + "png"
    # save screenshot
    print("screenshotpath=>" + os.path.abspath('.') + "/screenshots/" +
          screenshotName + ".png")
    driver.save_screenshot(os.path.abspath('.') + "/screenshots/" +
                           screenshotName + ".png")
