from pages.components.basic_element import BasicElement
from pages.my_orders.my_orders_page_locators import MyOrdersPageLocators


class MyOrdersPage:

    def __init__(self, driver):
        self.driver = driver

    @property
    def account_button(self):
        return BasicElement(self.driver, MyOrdersPageLocators.ACCOUNT_BUTTON)