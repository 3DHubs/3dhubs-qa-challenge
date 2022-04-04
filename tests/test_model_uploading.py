from playwright.sync_api import Page, expect
import allure
from pages.pages import ModelUploadPage, QuotePage


@allure.feature("Model Uploading")
class TestModelUpload:
    @allure.title("User can upload model with UI")
    def test_user_can_upload_model_with_ui(
        self, page: Page, model_upload_page: ModelUploadPage, quote_page: QuotePage
    ):
        with allure.step("Open model upload page"):
            model_upload_page.navigate()
        with allure.step("Upload model"):
            model_upload_page.upload_file("example_files/Ventring.step")
            quote_page.popup_close_btn.click()
            with allure.step("Check that model is uploaded"):
                expect(quote_page.quote_price).to_have_text("Total: RFQ")
                expect(quote_page.lead_time_selector).to_be_visible()
                expect(quote_page.shipping_selector).to_be_visible()
                expect(quote_page.technology_selector).to_be_visible()
