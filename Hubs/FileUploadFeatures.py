import os.path
import random
import string
from dataclasses import dataclass
from os import path, listdir

from config import TestParams


@dataclass
class FileSamples:
    file_type: str
    valid_sample_available: bool
    valid_sample_path: os.PathLike
    corrupted_sample_available: bool
    corrupted_sample_path: os.PathLike


class FileUploadFeature:
    SUPPORTED_FILE_TYPES = [
        'STL', 'OBJ', 'STEP', 'STP', 'IGES', 'IGS', 'SLDPRT', '3DM', 'SAT', 'X_T', 'DXF'
    ]
    TEST_FILE_LOCATION = TestParams.TEST_FILE_LOCATION

    def __init__(self):
        self.samples_lib = self.populate_samples_lib()
        self.valid_existing_files = [x.valid_sample_path for x in self.samples_lib.values()
                                     if x.valid_sample_available is True]
        self.corrupted_existing_files = [x.corrupted_sample_path for x in self.samples_lib.values()
                                         if x.corrupted_sample_available is True]
        self.wrong_types_existing_files = self.populate_wrong_file_types_samples()

    def populate_wrong_file_types_samples(self):
        res = []
        files = [f for f in listdir(self.TEST_FILE_LOCATION) if path.isfile(path.join(self.TEST_FILE_LOCATION, f))]
        for file in files:
            extension = os.path.splitext(file)[1][1:]
            if extension.upper() not in self.SUPPORTED_FILE_TYPES:
                res.append(self.get_full_sample_path(file))
        return res

    def populate_samples_lib(self):
        res = dict()
        for file_type in self.SUPPORTED_FILE_TYPES:
            valid_path = self.get_full_sample_path("valid_sample.{}".format(file_type))
            cor_path = self.get_full_sample_path("corrupted_sample.{}".format(file_type))
            res.update({
                file_type: FileSamples(file_type,
                                       True if path.exists(valid_path) else False,
                                       valid_path,
                                       True if path.exists(cor_path) else False,
                                       cor_path)
            })
        return res

    @staticmethod
    def generate_file_name(file_ext, length):
        name = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length))
        return '{}.{}'.format(name, file_ext)

    @staticmethod
    def get_full_sample_path(file) -> os.PathLike:
        file_path = path.join(TestParams.TEST_FILE_LOCATION, file)
        return file_path
