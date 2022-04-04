from playwright.sync_api import Page


class ModelUploadPage:
    def __init__(self, page: Page):
        self.page = page
        self.file_upload_input = page.locator(
            '[data-test="upload-form-file-input-btn"]'
        )

    def navigate(self, url: str = "https://www.hubs.com/manufacture/"):
        self.page.goto(url)

    def upload_file(self, file_path: str):
        self.file_upload_input.set_input_files(file_path)
        self.page.locator('[data-test="email-wall-input"]').fill("random@gmail.com")
        self.page.locator('[data-test="email-wall-submit"]').click()


class QuotePage:
    def __init__(self, page: Page):
        self.page = page
        self.popup_close_btn = page.locator(
            '[data-test="walkthrough-dialog-close-button"]'
        )
        self.technology_selector = page.locator('[data-test="qb-technology-selector"]')
        self.lead_time_selector = page.locator('[data-test="qb-lead_time_selector"]')
        self.shipping_selector = page.locator('[data-test="qb-shipping_selector"]')
        self.quote_price = page.locator('[data-test="quote-actions__total-price"]')
