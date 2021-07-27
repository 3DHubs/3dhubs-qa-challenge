from pages.my_orders.my_orders_page import MyOrdersPage


class MyOrdersPageActions:
    def __init__(self, driver):
        self.driver = driver
        self.my_orders_page = MyOrdersPage(driver)

    def wait_for_account_button_visible(self, timeout=10, poll_frequency=0.5):
        self.my_orders_page.account_button.wait_for_element_to_be_visible(timeout, poll_frequency)
