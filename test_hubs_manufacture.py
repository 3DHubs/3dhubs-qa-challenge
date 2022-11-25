"""
Test module, defines all the tests for hubs.com/manufacture
"""
from time import sleep

from pages.manufacture_page import ManufacturePage
from pages.home_page import HomePage


def test_upload_a_three_d_file(get_driver):
    """
    This test will valid upload the 3d file and verifies the successful upload.

    :param get_driver: Web driver instance
    :return: None
    """
    driver = get_driver
    home_page = HomePage(driver)
    assert home_page.check_for_get_instant_quote() is True
    home_page.click_get_instant_quote()
    manufacture_page = ManufacturePage(driver)
    assert manufacture_page.check_for_select_technology_lbl() is True
    manufacture_page.click_on_three_d_printing_link()
    sleep(2)
    manufacture_page.select_industrial_sla_link()
    manufacture_page.click_on_select_files_link()
    sleep(2)
    ManufacturePage.upload_a_three_d_file()
    # assert manufacture_page.check_for_welcome_to_hubs_popup() is True
    if manufacture_page.check_for_welcome_to_hubs_popup():
        manufacture_page.enter_email_txt()
        manufacture_page.click_on_go_to_your_quote_btn()
        sleep(4)
    manufacture_page.click_on_parts_and_specification_popup_btn()
    sleep(2)
    assert manufacture_page.check_for_view_dfm_analysis_btn() is True
