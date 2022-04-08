from Hubs.ManufacturePage.elem_expected_props import ManufactureElementsExpectedProps
from Hubs.ManufacturePage.page import ManufacturePage


def upload_file_without_login(test_page: ManufacturePage, file_to_upload):
    web_button = test_page.button_select_files
    web_button.validate_elem(**ManufactureElementsExpectedProps.BUTTON_select_files)
    web_button.element.send_keys(file_to_upload)


def fill_email_form(test_page: ManufacturePage, email):
    web_input = test_page.input_email_wall
    web_input.validate_elem(**ManufactureElementsExpectedProps.INPUT_email_wall)
    web_input.element.send_keys(email)
    web_button = test_page.button_email_submit
    web_button.element.click()


def check_analyse_is_started(test_page: ManufacturePage):
    web_img = test_page.img_analyzing_parts
    web_img.validate_elem(**ManufactureElementsExpectedProps.IMG_analyzing_parts)


def check_if_error_file_type_div_is_shown(test_page: ManufacturePage, failure_expected: bool = False):
    try:
        web_div = test_page.div_error_file_unsupported
        web_div.validate_elem(**ManufactureElementsExpectedProps.DIV_error_file_unsupported)
    except Exception as e:
        if not failure_expected:
            assert web_div.is_found is True, 'error_file_type_div was not found by {}, {}'.format(web_div.locator, e)
