import time
import pytest
from pages.manufacture_upload_page import UploadPage
from pages.order_page import OrderPage
from pages.login_page import LoginPage
from test_cases.test_data import FILE_TYPE_PNG
from test_cases.test_data import FILE_TYPE_STEP_2


@pytest.mark.usefixtures("setup")
class TestModelUploading():

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.up = UploadPage(self.driver, self.wait)
        self.odp = OrderPage(self.driver, self.wait)
        self.log = LoginPage(self.driver, self.wait)

    def test_login_operation(self):
        self.up.click_log_in_button()
        self.log.input_mail_adress_()
        self.log.input_password()
        self.log.click_login_button()
        self.odp.click_skip_button()
        self.odp.click_new_quote()

    def test_check_text(self):
        self.up.check_upload_text()
        self.up.check_select_technology_text()

    def test_check_buttons(self):
        self.up.check_the_quotes_button()
        self.up.check_the_orders_button()
        self.up.check_the_new_quote()

    def test_check_uploading_sheet_pass(self):
        self.up.click_sheet_metal()
        self.up.file_upload(FILE_TYPE_STEP_2)
        self.up.click_agree_button()
        time.sleep(45)
        self.odp.click_close_button()
        self.odp.check_place_order_button()
        self.odp.click_new_quote()
        self.odp.click_start_new_quote_button()

    def test_check_uploading_cnc_pass(self):
        # self.up.click_CNC_machining()
        self.up.file_upload(FILE_TYPE_STEP_2)
        time.sleep(45)
        self.odp.check_place_order_button()
        self.odp.check_place_order_button()
        self.odp.click_new_quote()
        self.odp.click_start_new_quote_button()

    def test_check_uploading_fail(self):
        self.up.file_upload(FILE_TYPE_PNG)
        self.up.check_png_fail()
        self.up.check_png_fail()
