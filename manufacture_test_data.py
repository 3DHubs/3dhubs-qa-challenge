"""
This module supplies the test data for Manufacture Page Object
"""
import os
from pathlib import Path
from dataclasses import dataclass


@dataclass
class ManufactureTestData:
    """
    Class that defines the test data like, files and filepaths
    """
    test_data_path = Path(os.getcwd()) / 'test_data'

    THREE_D_HORSE = test_data_path / 'Horse_Nuetral.obj'
    SHEET_METAL = test_data_path / 'FilamentClip.stl'
    BUILDING = test_data_path / 'Building.obj'


if __name__ == '__main__':
    print(ManufactureTestData.test_data_path / ManufactureTestData.THREE_D_HORSE)
