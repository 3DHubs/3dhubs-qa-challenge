import logging
import os

import pytest

from Hubs.FileUploadFeatures import FileUploadFeature
from Hubs.ManufacturePage import page_actions
from Hubs.ManufacturePage.page import ManufacturePage
from config import TestParams

logger = logging.getLogger(__name__)


class TestHubsManufacturePage:
    file_samples_lib = FileUploadFeature()

    @pytest.fixture()
    def test_page(self, driver):
        page = ManufacturePage(driver, url=TestParams.TEST_PAGE)
        page.load()
        yield self.validate_page_is_loaded(page)

    @staticmethod
    def validate_page_is_loaded(page):
        assert page.expected_title in page.driver.title, \
            'Cannot load {}, unexpected title: {}'.format(TestParams.TEST_PAGE, page.driver.title)
        for x in page.unexpected_page_contents:
            assert x not in page.driver.page_source, 'Cannot load {}, unexpected page_source: {}'.format(
                TestParams.TEST_PAGE, page.driver.page_source)
        return page


    @pytest.mark.parametrize("file_to_upload", file_samples_lib.valid_existing_files)
    def test_manufacture_upload_file_good_path_all_valid_file_types(self, test_page: ManufacturePage, file_to_upload):
        page_actions.upload_file_without_login(test_page=test_page,
                                               file_to_upload=file_to_upload)
        page_actions.check_if_error_file_type_div_is_shown(test_page=test_page, failure_expected=True)
        page_actions.fill_email_form(test_page=test_page, email=TestParams.EMAIL_USERNAME)
        page_actions.check_analyse_is_started(test_page=test_page)

    @pytest.mark.parametrize("file_to_upload", file_samples_lib.wrong_types_existing_files)
    def test_manufacture_upload_file_bad_path_all_wrong_file_types(self, test_page: ManufacturePage, file_to_upload):
        page_actions.upload_file_without_login(test_page=test_page,
                                               file_to_upload=file_to_upload)
        page_actions.check_if_error_file_type_div_is_shown(test_page=test_page, failure_expected=False)
