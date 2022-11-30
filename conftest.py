import pytest
from playwright.sync_api import Page

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.manufacture_page import ManufacturePage
from pages.orders_page import OrdersPage
from pages.quote_page import QuotePage


@pytest.fixture(scope="session", autouse=True)
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1536,
            "height": 754,
        }
    }


@pytest.fixture
def home(page: Page):
    return HomePage(page)


@pytest.fixture
def login(page: Page):
    return LoginPage(page)


@pytest.fixture
def orders(page: Page):
    return OrdersPage(page)


@pytest.fixture
def manufacture(page: Page):
    return ManufacturePage(page)


@pytest.fixture
def quote(page: Page):
    return QuotePage(page)
