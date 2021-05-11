import logging
import os

import pytest

from tests.page_model.manufacture_page import ManufacturePage
from tests.page_model.quote_page import QuotePage

EMAIL = 'xxxxxx@gmail.com'
PATH_TO_XT_FILE = os.path.abspath(r'./uploaded_files/x_t_file.x_t')
PATH_TO_IGES_FILE = os.path.abspath(r'./uploaded_files/iges_file.IGES')
PATH_TO_STP_FILE = os.path.abspath(r'./uploaded_files/stp_file.STP')
PATH_TO_SLDPRT_FILE = os.path.abspath(r'./uploaded_files/sldprt_file.SLDPRT')
PATH_TO_3MD_FILE = os.path.abspath(r'./uploaded_files/3dm_file.3dm')
PATH_TO_IGS_FILE = os.path.abspath(r'./uploaded_files/igs_file.IGS')
PATH_TO_SAT_FILE = os.path.abspath(r'./uploaded_files/sat_file.SAT')
PATH_TO_STEP_FILE = os.path.abspath(r'./uploaded_files/step_file.STEP')
PATH_TO_MULTIPLE_FILES = PATH_TO_XT_FILE + ' \n ' + PATH_TO_IGES_FILE
PATH_TO_PNG_FILE = os.path.abspath(r'./uploaded_files/png_file.png')
PATH_TO_STL_FILE = os.path.abspath(r'./uploaded_files/stl_file.STL')
PATH_TO_ASSEMBLY_FILE = os.path.abspath(r'./uploaded_files/assembly.STP')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class TestUploadingFunction:
    @pytest.mark.parametrize('path', [PATH_TO_XT_FILE, PATH_TO_IGES_FILE, PATH_TO_STP_FILE,
                                      PATH_TO_SLDPRT_FILE, PATH_TO_3MD_FILE, PATH_TO_IGS_FILE,
                                      PATH_TO_SAT_FILE, PATH_TO_STEP_FILE])
    def test_upload_a_file_successfully(self, browser, path):
        """
        The method tests that one design file in correct type can be uploaded successfully. After uploading,
        browser will switch from manufacture page to the quote page, price will be shown, and there is no error message
         in quote page.
        :param browser: fixture
        :param path: pytest parameter, path to uploaded file
        :return: Optional[Any]
        """
        manufacture_page = ManufacturePage(browser)
        logger.info('uploading a design file...')
        manufacture_page.upload_file(path, EMAIL)

        quote_page = QuotePage(browser)
        quote_page.close_intro_dialog()

        assert quote_page.base_url in browser.current_url
        assert quote_page.price.is_displayed()
        assert not quote_page.error_message_is_present

    def test_upload_multiple_files_together_successfully(self, browser):
        """
        The method tests that multiple design files in correct types can be uploaded together successfully. After
        uploading, browser will switch from manufacture page to the quote page, price will be shown, and there is no
        error message in quote page.
        :param browser: fixture
        :return: None
        """
        manufacture_page = ManufacturePage(browser)
        logger.info('uploading multiple files...')
        manufacture_page.upload_file(PATH_TO_MULTIPLE_FILES, EMAIL)

        quote_page = QuotePage(browser)
        quote_page.close_intro_dialog()

        assert quote_page.base_url in browser.current_url
        assert quote_page.price.is_displayed()
        assert not quote_page.error_message_is_present

    def test_upload_file_in_non_design_type(self, browser):
        """
        This method tests that a file in non design type (e.g. png file) can not be uploaded successfully. The browser
        will stay in manufacture page and an error message is shown.
        :param browser: fixture
        :return: None
        """
        manufacture_page = ManufacturePage(browser)
        logger.info('uploading a png file...')
        manufacture_page.upload_file_in_non_design_type(PATH_TO_PNG_FILE)

        assert manufacture_page.upload_error_is_present
        assert browser.current_url == manufacture_page.url

    def test_upload_stl_file(self, browser):
        """
        The method tests that a stl file can not be uploaded successfully. After uploading, browser will switch from
        manufacture page to the quote page and there is error message in quote page.
        :param browser: fixture
        :return: None
        """
        manufacture_page = ManufacturePage(browser)
        logger.info('uploading a stl file...')
        manufacture_page.upload_file(PATH_TO_STL_FILE, EMAIL)

        quote_page = QuotePage(browser)
        quote_page.close_intro_dialog()

        assert quote_page.base_url in browser.current_url
        assert quote_page.error_message_is_present

    def test_upload_assembly_file(self, browser):
        """
        The method tests that an assembly design file in correct type can not be uploaded successfully. After
        uploading, browser will switch from manufacture page to the quote page and there is error message in quote page.
        :param browser: fixture
        :return: None
        """
        manufacture_page = ManufacturePage(browser)
        logger.info('uploading an assembly file...')
        manufacture_page.upload_file(PATH_TO_ASSEMBLY_FILE, EMAIL)

        quote_page = QuotePage(browser)
        quote_page.close_intro_dialog()

        assert quote_page.base_url in browser.current_url
        assert quote_page.error_message_is_present

    def test_upload_a_file_of_more_than_128mb(self, browser):
        """
        The method tests that a design file of more than 128MB can not be uploaded successfully. It is not implemented
        as design file of more than 128MB is not found. It can be tested in the same flow as methods above.
        :param browser: fixture
        :return: None
        """
        logger.info('not implemented yet...')
        pass

    def test_upload_a_file_with_size_of_more_than_3000mm(self, browser):
        """
        The method tests that a design file with size of more than 3000mm can not be uploaded successfully. It is not
        implemented as design file with size of more than 3000mm is not found. It can be tested in the same flow as
        methods above.
        :param browser: fixture
        :return: None
        """
        logger.info('not implemented yet...')
        pass
