from playwright.sync_api import Page


def test_model_upload(page: Page, home, login, orders, manufacture, quote):
    email = 'leciva9604@sunetoa.com'
    password = '.@Xn8SUW6*Kcg9B'

    home.open_home_page()
    home.open_login_page()

    login.fill_in_credentials_and_submit(email, password)

    orders.close_walkthrough_popup()
    orders.click_new_quote()

    manufacture.select_sheet_metal()
    manufacture.select_file()
    manufacture.agree_with_policy()

    quote.close_walkthrough_popup()
    quote.assert_quote_is_created()
    page.screenshot(path='screenshot.png', full_page=True)
