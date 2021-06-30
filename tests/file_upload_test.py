import pytest

from pages.manufacture_page import ManufacturesPage
from utils import datautils as pathdata
from utils import utils as environment
from utils.datautils import TEST_EMAIL


@pytest.mark.usefixtures("test_setup")
class TestModelUploading:
    """
    Below  functions tests file uploading module in manufature page.

    test_step_file_successful_upload test checks file uploading module with the following file-
    types : .x_t, .iges, .stp, .sldprt, .3dm, .igs, .sat, .step
    """

    @pytest.mark.parametrize("path_to_file", [pathdata.STEP_FILE_PATH, pathdata.SAT_FILE_PATH,
                                              pathdata.X_T_FILE_PATH, pathdata.STP_FILE_PATH,
                                              pathdata.SLDPRT_FILE_PATH, pathdata.IGS_FILE_PATH, ])
    def test_step_file_successful_upload(self, path_to_file):
        driver = self.driver
        driver.get(environment.URL_3DS)
        try:
            manufacturesPage = ManufacturesPage(driver)
            manufacturesPage.verify_manufacturepage_displyed()
            manufacturesPage.upload_the_given_file_successfully_to_get_quotes(path_to_file)
            manufacturesPage.enter_email_to_receive_quote(TEST_EMAIL)
        except:
            print("There was an exception")
            environment.save_screenshot(self.driver, environment.get_current_function())
            # the raise is to show it as a failure
            raise
        else:
            print("No exceptions occurred")
            print("file uploading module in manufacture page tested with the "
                  "following file-types - { .x_t, .iges, .stp, .sldprt, .3dm, .igs, .sat, .step}")
        finally:
            print("Inside finally block")

    """
    test_invalid_file_upload test checks file uploading module with the following file-
    types : .jpg,.docx
    """

    @pytest.mark.parametrize("path_to_format_invalid_file",
                             [pathdata.INVALID_FILE_JPG_PATH, pathdata.INVALID_FILE_DOCX_PATH, ])
    def test_invalid_file_upload(self, path_to_format_invalid_file):

        driver = self.driver
        driver.get(environment.URL_3DS)
        try:
            manufacturesPage = ManufacturesPage(driver)
            manufacturesPage.verify_manufacturepage_displyed()
            manufacturesPage.try_to_upload_invalid_file_and_verify_error_message(path_to_format_invalid_file)
        except:
            print("There was an exception")
            environment.save_screenshot(self.driver, environment.get_current_function())
            # the raise is to show it as a failure
            raise
        else:
            print("No exceptions occurred")
            print("file uploading module in manufacture page tested with the "
                  "following file-types - { .jpg,.docx}. Error message is verified")
        finally:
            print("Inside finally block")

    # test_multiple_file_successful_upload checks multiple file uploading.

    def test_multiple_file_successful_upload(self):
        driver = self.driver
        driver.get(environment.URL_3DS)
        try:
            manufacturesPage = ManufacturesPage(driver)
            manufacturesPage.verify_manufacturepage_displyed()
            manufacturesPage.upload_multiple_files_successfully_to_get_quotes(pathdata.MULTIPLE_FILE1_PATH,
                                                                              pathdata.MULTIPLE_FILE2_PATH)
            manufacturesPage.enter_email_to_receive_quote("brijithlooka@gmail.com")
        except:
            print("There was an exception")
            environment.save_screenshot(self.driver, environment.get_current_function())
            # the raise is to show it as a failure
            raise
        else:
            print("No exceptions occurred")
            print("multiple file uploading tested in manufacture page")
        finally:
            print("Inside finally block")

    '''
    
    Below method ,"test_large_size_file_upload" ,  tests that  design file with size greater than 128mb
    and part size greater than 3000*3000*3000 cannot be uploaded.
    Below function is not implemented yet since design file with large size and large part size is not available.
  
    
   @pytest.mark.parametrize("invalid_size_file_path",[pathdata.LARGE_SIZE_FILE_PATH,pathdata.LARGE_PART_SIZE_FILE_PATH,])
   def test_invalid_size_file_upload(self,invalid_size_file_path):

       driver = self.driver
       driver.get(environment.URL_3DS)
       try:
           manufacturesPage = ManufacturesPage(driver)
           manufacturesPage.click_select_your_files_button()
           # manufacturesPage.try_to_upload_invalid_size_file_and_verify_error_message(invalid_size_file_path)
           logger.info('this method is not implemented')
       except:
           print("There was an exception")
           environment.save_screenshot(self.driver, environment.get_current_function())
           # the raise is to show it as a failure
           raise
       else:
           print("No exceptions occurred")
       finally:
           print("Inside finally block")

    '''
