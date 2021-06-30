import os
import pytest
from pages.upload_file_page import UploadFilePage

BASE_DIR = os.path.dirname(os.path.abspath('../files/Rack_and_Pinion.STEP'))
JPEG_FILE = os.path.join(BASE_DIR, 'flowers.jpg')


@pytest.mark.parametrize('file_path', [JPEG_FILE])
@pytest.mark.usefixtures("params", "setup_and_tear_down")
class TestUploadFile():

    def test_upload_file_wrong_format(self, file_path):
        """
         Performs file upload with wrong format and checks that appropriate message was received - negative test
        """
        try:
            # Files list
            files_list = [file_path]
            number_of_parts = len(files_list)

            # Initiates upload file page object
            upload_file_page = UploadFilePage(self.driver)

            # Upload a file with a wrong format
            wrong_format_message = upload_file_page.click_upload_file_wrong_format(files_list)

            # Verifies wrong format message was received
            assert wrong_format_message == "JPG files are not supported. Please upload your parts in one of the following formats: STEP, IGES, SLDPRT, 3DM, SAT or X_T."



        except AssertionError as error:
            # Output Errors.
            print(error)
            assert False

        except Exception as exception:
            # Output  Exceptions.
            print(exception)
            assert False