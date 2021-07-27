import os


class FilePathHelper:
    def __init__(self):
        pass

    @staticmethod
    def get_file_absolute_path(self, filename):
        return os.path.abspath(os.path.join(os.getcwd(), "..\\files", filename))
