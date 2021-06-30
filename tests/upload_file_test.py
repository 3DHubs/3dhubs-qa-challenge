import os
from decimal import Decimal
import pytest
from pages.upload_file_page import UploadFilePage

BASE_DIR = os.path.dirname(os.path.abspath('../files/Rack_and_Pinion.STEP'))
STEP_FILE = os.path.join(BASE_DIR, 'Rack_and_Pinion.STEP')
SLDPRT_FILE = os.path.join(BASE_DIR, 'lower_right.SLDPRT')


@pytest.mark.parametrize('file_path', [STEP_FILE, SLDPRT_FILE])
@pytest.mark.usefixtures("params", "setup_and_tear_down")
class TestUploadFile():


    def test_upload_file(self, file_path):
        """
        Performs file upload test for different format of files.
        In the following test are used only 2 formats of file, possible to add all formats.
        """
        try:
            # Files list
            files_list = [file_path]
            number_of_parts = len(files_list)

            # Order info dict - all info will be taken in 'Quote overview' page, and after it will be tested
            order_info = {"total price": "", "shipped date": "", "delivery date": "",
                           "technology": "", "shipping price": "", "subtotal price": "", "total buy price": ""}

            # Parts info dict - all info will be taken in 'Quote overview' page, and after it will be tested
            parts_info = []
            for part in range(number_of_parts):
                parts_info.append({"price": "", "quantity": "", "price per part": "", "details": "",
                               "material row 1": "", "material row 2": "", "material row 3": "", "name of part": "",
                               "size of part": "", "image src": ""})

            # Initiates upload file page object
            upload_file_page = UploadFilePage(self.driver)

            # Upload a file
            upload_file_page.click_upload_file(files_list)

            # Takes values that should be tested
            order_info, parts_info = upload_file_page.takes_values_to_test(order_info, parts_info, number_of_parts)

            # Verifies total price has numeric value
            assert order_info["total price"] != "", "The total price doesn't exist"
            assert type(order_info["total price"]) == Decimal, "The total price is not displayed as number"

            for num_of_part in range(number_of_parts):
                # Verifies price has numeric value
                assert parts_info[num_of_part]["price"] != "", "The price doesn't exist"
                assert type(parts_info[num_of_part]["price"]) == Decimal, "The price is not displayed as number"

                # Verifies quantity has numeric value
                assert parts_info[num_of_part]["quantity"] != "", "The quantity doesn't exist"
                assert type(parts_info[num_of_part]["quantity"]) == int, "The quantity is not displayed as number"

                # Verifies price per part has numeric value
                assert parts_info[num_of_part]["price per part"] != "", "Price per part doesn't exist"
                assert type(parts_info[num_of_part]["price per part"]) == Decimal, "The price per part is not displayed as number"

                # Verifies details of the part exists
                assert parts_info[num_of_part]["details"] != "", "Details don't exist"

                # Verifies material of the part exists
                assert parts_info[num_of_part]["material row 1"] != "", "Material row 1 doesn't exist"
                assert parts_info[num_of_part]["material row 2"] != "", "Material row 2 doesn't exist"
                assert parts_info[num_of_part]["material row 3"] != "", "Material row 3 doesn't exist"

                # Verifies name and size of the part are exist
                assert parts_info[num_of_part]["name of part"] != "", "Name of part doesn't exist"
                assert parts_info[num_of_part]["size of part"] != "", "Size of part doesn't exist"

                # Verifies image is presented
                assert parts_info[num_of_part]["image src"] != "", "Image is not presented"

            # Verifies shipped date exists
            assert order_info["shipped date"] != "", "Shipped date doesn't exist"

            # Verifies Delivery date exists
            assert order_info["delivery date"] != "", "Delivery date doesn't exist"

            # Verifies technology exists
            assert order_info["technology"] != "", "Technology date doesn't exist"

            # Verifies shipping price exists
            assert order_info["shipping price"] != "", "The shipping price doesn't exist"
            assert type(order_info["shipping price"]) == Decimal, "The shipping price is not displayed as number"

            # Verifies subtotal price exists
            assert order_info["subtotal price"] != "", "The subtotal price doesn't exist"
            assert type(order_info["subtotal price"]) == Decimal, "The subtotal price is not displayed as number"

            # Verifies total buy price exists
            assert order_info["total buy price"] != "", "The total buy price doesn't exist"
            assert type(order_info["total buy price"]) == Decimal, "The total buy price is not displayed as number"


        except AssertionError as error:
            # Output Errors.
            print(error)
            assert False

        except Exception as exception:
            # Output  Exceptions.
            print(exception)
            assert False