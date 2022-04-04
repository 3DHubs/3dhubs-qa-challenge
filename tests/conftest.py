import pytest
from playwright.sync_api import Page

from pages.pages import ModelUploadPage, QuotePage


@pytest.fixture(scope="function")
def model_upload_page(page: Page):
    return ModelUploadPage(page)


@pytest.fixture(scope="function")
def quote_page(page: Page):
    return QuotePage(page)
