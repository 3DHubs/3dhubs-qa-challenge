from playwright.sync_api import Page, expect


def test_model_upload(page: Page):
    email = 'ruff3110@gmail.com'
    password = 'XF@vhGZj98VK.y-'

    # open home page
    page.goto('https://www.hubs.com/')

    # open login page
    page.locator('//span[@class="material-icons h3d-navbar__user-avatar"]').click()
    page.locator('//a[@href="/manufacture/login"]').click()
    # type email and password and click Log in
    page.locator('//input[@type="email"]').fill(email)
    page.locator('//input[@type="password"]').fill(password)
    page.locator('//button[@type="submit"]').click()

    # on Orders page click popup
    page.locator('//button[@data-test="walkthrough-dialog-close-button"]').click()
    # Click New quote
    page.locator('//div[@data-test="h3d-navbar__new-quote"]').click()

    # select Sheet metal
    page.locator('//h3d-card[@data-test="technology-item-sheet-metal"]').click()
    # select file
    page.locator('//input[@id="file-btn"]').set_input_files('test_data/sheet_metal_sample.step')

    # Click Agree with Terms
    page.locator('//button[contains(@class, "agree-and-upload")]').click()

    # close popup
    page.locator('//button[@data-test="walkthrough-dialog-close-button"]').click()
    # assert quote is created
    expect(page.locator('//div[@data-test="order-toolbar-title"]')).to_have_text('Untitled quote', timeout=60000)
    expect(page.locator('//div[@class="line-items"]//h4')).to_have_text('Parts & specifications', timeout=60000)
    page.screenshot(path='screenshot.png', full_page=True)
