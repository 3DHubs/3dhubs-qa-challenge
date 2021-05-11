from selenium.webdriver.common.by import By


class QuotePageLocators:
    TOTAL_PRICE = By.CSS_SELECTOR, "div.h3d-actions__total-price"
    DIALOG_CLOSE_BUTTON = By.CLASS_NAME, "h3d-button.new-feature-walkthrough-dialog__close-button"
    ERROR_MESSAGE = By.CSS_SELECTOR, "div.h3d-notification-inline__content"
