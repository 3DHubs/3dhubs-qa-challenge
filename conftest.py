import pytest
from playwright.sync_api import Page

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.manufacture_page import ManufacturePage
from pages.orders_page import OrdersPage
from pages.quote_page import QuotePage


@pytest.fixture(autouse=True)
def set_default_timeout_and_viewport_size(page):
    # pages often load slowly
    page.set_default_timeout(timeout=90000)
    # the closest size to maximized window
    page.set_viewport_size({"width": 1536, "height": 754})
    yield page


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
