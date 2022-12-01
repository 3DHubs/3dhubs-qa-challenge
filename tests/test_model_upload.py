import pytest
from playwright.sync_api import Page


@pytest.mark.parametrize('technology', ['cnc_machining', 'sheet_metal'])
def test_model_upload_with_login(page: Page, home, login, orders, manufacture, quote, technology):
    email = 'leciva9604@sunetoa.com'
    password = '.@Xn8SUW6*Kcg9B'

    home.open_home_page()
    home.open_login_page()

    login.fill_in_credentials_and_submit(email, password)

    orders.close_walkthrough_popup()
    orders.click_new_quote()

    manufacture.select_technology(technology=technology)
    manufacture.select_file(technology=technology)
    manufacture.agree_with_policy()

    quote.close_walkthrough_popup()
    quote.assert_quote_is_created()
    page.screenshot(path=f'screenshots/model_upload_with_login_{technology}.png', full_page=True)


@pytest.mark.parametrize('technology', ['cnc_machining', 'sheet_metal'])
def test_model_upload_without_login(page: Page, home, manufacture, quote, technology):
    home.open_home_page()
    home.get_instant_quote()

    manufacture.select_technology(technology=technology)
    manufacture.select_file(technology=technology)
    manufacture.fill_in_email_in_popup()

    quote.close_walkthrough_popup()
    quote.assert_quote_is_created()
    page.screenshot(path=f'screenshots/model_upload_without_login_{technology}.png', full_page=True)


def test_model_upload_with_wrong_format(page: Page, home, manufacture):
    home.open_home_page()
    home.get_instant_quote()

    manufacture.select_wrong_format_file()
    manufacture.expect_wrong_format_error()
    page.screenshot(path=f'screenshots/model_upload_with_wrong_format.png', full_page=True)
