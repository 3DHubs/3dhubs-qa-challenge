import time
from decimal import Decimal

from elements.upload_file_elements import UploadFileElements, find_element, find_element_explicit, take_part_info
from pages.base_page import BasePage
wait_upload_file = 30

class UploadFilePage(BasePage):
    """ Upload file page object """

    def __init__(self, driver):
        self.driver = driver
        super(UploadFilePage, self).__init__()

    def click_upload_file(self, files_list):
        """
        Method uploads a file
        """
        try:

            find_element(self.driver, UploadFileElements.UPLOAD_FILES_BUTTON.value)\
                .send_keys(files_list[0])

            # Write email
            find_element_explicit(self.driver, UploadFileElements.EMAIL.value).send_keys('yakovtakser@gmail.com')

            # Click on continue
            find_element_explicit(self.driver, UploadFileElements.CONTINUE_BUTTON.value).click()

            # Wait until the file is uploaded
            time.sleep(wait_upload_file)

            # Close dialog window
            find_element_explicit(self.driver, UploadFileElements.DIALOG_CLOSE_BUTTON.value).click()
            time.sleep(1)

        except Exception as exception:
            # Output unexpected Exceptions.
            raise Exception(exception)

    def click_add_additional_files(self, files_list):
        """
        Method adds additional file, starts from the second file in the files_list
        :param 1: file_list a List with all files that should be uploaded
        """
        try:
            num_of_file = 1
            while num_of_file < len(files_list):

                find_element(self.driver, UploadFileElements.ADD_ADDITIONAL_FILE.value) \
                    .send_keys(files_list[num_of_file])

                time.sleep(wait_upload_file)
                num_of_file += 1


        except Exception as exception:
            # Output unexpected Exceptions.
            raise Exception(exception)

    def takes_values_to_test(self, order_info, parts_info, number_of_parts):
        """
        Method takes values that should be tested in the scope of the test
        :param 1: test_values Dict variable, stores all values that should be tested
        :return Dict of all values that should be tested
        """
        try:

            # Takes total price
            order_info["total price"] = find_element_explicit(self.driver, UploadFileElements.TOTAL_PRICE.value).text
            # Remove ',' chars to make a number that possible to work with
            order_info["total price"] = order_info["total price"].replace(',', '')
            # takes only number and convert it to Decimal number
            order_info["total price"] = Decimal(order_info["total price"][3:])

            for num_of_part in range(number_of_parts):
                # Takes price, takes only number from price and convert it to Decimal number
                parts_info[num_of_part]["price"] = take_part_info(self.driver, UploadFileElements.PRICE.value,
                                                                               num_of_part+1).text

                # Remove ',' chars to make a number that possible to work with
                parts_info[num_of_part]["price"] = parts_info[num_of_part]["price"].replace(',', '')

                # takes only number and convert it to Decimal number
                parts_info[num_of_part]["price"] = Decimal(parts_info[num_of_part]["price"][3:])

                # Takes quantity, convert quantity to int
                parts_info[num_of_part]["quantity"] = take_part_info(self.driver, UploadFileElements.QUANTITY.value,
                                                                                  num_of_part+1).text

                parts_info[num_of_part]["quantity"] = int(parts_info[num_of_part]["quantity"])

                # Takes price per part, takes only number from price per part and convert it to Decimal number
                parts_info[num_of_part]["price per part"] = take_part_info(self.driver,
                                                                                  UploadFileElements.PRICE_PER_PART.value,
                                                                                  num_of_part+1).text

                # Remove ',' chars to make a number that possible to work with
                parts_info[num_of_part]["price per part"] = parts_info[num_of_part]["price per part"].replace(',', '')

                # takes only number and convert it to Decimal number
                parts_info[num_of_part]["price per part"] = Decimal(parts_info[num_of_part]["price per part"][3:])

                # Takes details of the part
                parts_info[num_of_part]["details"] = take_part_info(self.driver, UploadFileElements.DETAILS.value,
                                                                    num_of_part+1).text

                # Takes material of the part
                parts_info[num_of_part]["material row 1"] = take_part_info(self.driver,
                                                                                  UploadFileElements.MATERIAL_ROW1.value,
                                                                                  num_of_part+1).text

                parts_info[num_of_part]["material row 2"] = take_part_info(self.driver,
                                                                                  UploadFileElements.MATERIAL_ROW2.value,
                                                                                  num_of_part+1).text

                parts_info[num_of_part]["material row 3"] = take_part_info(self.driver,
                                                                                  UploadFileElements.MATERIAL_ROW3.value,
                                                                                  num_of_part+1).text

                # Takes name and size of the part
                parts_info[num_of_part]["name of part"] = take_part_info(self.driver,
                                                                                UploadFileElements.NAME_OF_PART.value,
                                                                                num_of_part+1).text

                parts_info[num_of_part]["size of part"] = take_part_info(self.driver,
                                                                                UploadFileElements.SIZE_OF_PART.value,
                                                                                num_of_part+1).text

                # Takes image
                parts_info[num_of_part]["image src"] = take_part_info(self.driver,
                                                                             UploadFileElements.SIZE_OF_PART.value,
                                                                             num_of_part+1).get_attribute("src")
            # Takes shipped date
            order_info["shipped date"] = find_element_explicit(self.driver,
                                                               UploadFileElements.SHIPPED_DATE.value).text

            # Takes delivery date
            order_info["delivery date"] = find_element_explicit(self.driver,
                                                                UploadFileElements.SHIPPED_DATE.value).text

            # Takes technology
            order_info["technology"] = find_element_explicit(self.driver,
                                                             UploadFileElements.TECHNOLOGY.value).text

            # Takes shipping price, takes only number from shipping price and convert it to Decimal number
            order_info["shipping price"] = find_element_explicit(self.driver,
                                                                 UploadFileElements.SHIPPING_PRICE.value).text
            # Remove ',' chars to make a number that possible to work with
            order_info["shipping price"] = order_info["shipping price"].replace(',', '')
            # takes only number and convert it to Decimal number
            order_info["shipping price"] = Decimal(order_info["shipping price"][3:])

            # Takes subtotal price, takes only number from subtotal price and convert it to Decimal number
            order_info["subtotal price"] = find_element_explicit(self.driver,
                                                                 UploadFileElements.SUBTOTAL_PRICE.value).text
            # Remove ',' chars to make a number that possible to work with
            order_info["subtotal price"] = order_info["subtotal price"].replace(',', '')
            # takes only number and convert it to Decimal number
            order_info["subtotal price"] = Decimal(order_info["subtotal price"][3:])

            # Takes total buy price, takes only number from total buy price and convert it to Decimal number
            order_info["total buy price"] = find_element_explicit(self.driver,
                                                                  UploadFileElements.TOTAL_BUY_PRICE.value).text
            # Remove ',' chars to make a number that possible to work with
            order_info["total buy price"] = order_info["total buy price"].replace(',', '')
            # takes only number and convert it to Decimal number
            order_info["total buy price"] = Decimal(order_info["total buy price"][3:])

            return order_info, parts_info

        except Exception as exception:
            # Output  Exceptions.
            print(exception)
            assert False

    def click_upload_file_wrong_format(self, files_list):
        """Takes wrong format message"""
        try:
            find_element(self.driver, UploadFileElements.UPLOAD_FILES_BUTTON.value) \
                .send_keys(files_list[0])



            # Wait until the file is uploaded
            time.sleep(wait_upload_file)

            wrong_format_message = find_element_explicit(self.driver, UploadFileElements.WRONG_FORMAT_MESSAGAE.value).text

            return wrong_format_message
        except Exception as exception:
            # Output unexpected Exceptions.
            raise Exception(exception)

    def click_upload_file_big_size(self, files_list):
        """Takes file is too large message"""
        try:
            find_element(self.driver, UploadFileElements.UPLOAD_FILES_BUTTON.value) \
                .send_keys(files_list[0])

            # Wait until the file is uploaded
            time.sleep(wait_upload_file)

            large_file_message = find_element_explicit(self.driver,
                                                         UploadFileElements.BIG_SIZE_OF_FILE_MESSAGE.value).text

            print('ewfewfewfwef00')
            print(large_file_message)

            return large_file_message


        except Exception as exception:
            # Output unexpected Exceptions.
            raise Exception(exception)