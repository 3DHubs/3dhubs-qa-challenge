import os
import pytest
from pages.upload_file_page import UploadFilePage

BASE_DIR = os.path.dirname(os.path.abspath('../files/Rack_and_Pinion.STEP'))
BIG_SIZE_FILE = os.path.join(BASE_DIR, 'big.SLDPRT')


@pytest.mark.parametrize('file_path', [BIG_SIZE_FILE])
@pytest.mark.usefixtures("params", "setup_and_tear_down")
class TestUploadFile():


    def test_upload_file_big_file(self, file_path):
        """
        Performs file upload with a big size of file and checks that appropriate message was received - negative test
        """
        try:
            # Files list
            files_list = [file_path]
            number_of_parts = len(files_list)

            # Initiates upload file page object
            upload_file_page = UploadFilePage(self.driver)

            # Upload a file with a wrong format
            large_file_message = upload_file_page.click_upload_file_big_size(files_list)

            # Verifies wrong format message was received
            assert large_file_message == "This file is too large. We support files up to 128 MB."



        except AssertionError as error:
            # Output Errors.
            print(error)
            assert False

        except Exception as exception:
            # Output  Exceptions.
            print(exception)
            assert False