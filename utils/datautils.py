import os
import platform

TEST_EMAIL = "test@gmail.com"

BASE_PATH = os.path.abspath('.')


def get_path(path):
    if platform.system() == "Windows":
        return path
    else:
        return path.replace("\\", "/")


# FILE PATHS
STEP_FILE_PATH = get_path(BASE_PATH + "\\data\\stepfile\\Cushioneer-1in stroke.STEP")
SAT_FILE_PATH = get_path(BASE_PATH + "\\data\\satfile\\Cushioneer-1in stroke.SAT")
X_T_FILE_PATH = get_path(BASE_PATH + "\\data\\x_t_file\\Cushioneer-1in stroke.x_t")
STP_FILE_PATH = get_path(BASE_PATH + "\\data\\stpfile\\Cushioneer-1in stroke.STP")
SLDPRT_FILE_PATH = get_path(BASE_PATH + "\\data\\sldprtfile\\Cushioneer-1in stroke.SLDPRT")
IGS_FILE_PATH = get_path(BASE_PATH + "\\data\\igsfile\\Cushioneer-1in stroke.IGS")
FILE_PATH_3DM = get_path(BASE_PATH + "\\data\\3dmfile\\Cushioneer-1in stroke.3DM")
INVALID_FILE_JPG_PATH = get_path(BASE_PATH + "\\data\\invalidfile\\bird.jpg")
INVALID_FILE_DOCX_PATH = get_path(BASE_PATH + "\\data\\invalidfile\\invalid.docx")
MULTIPLE_FILE1_PATH = get_path(BASE_PATH + "\\data\\multiplefiles\\file1.SLDPRT")
MULTIPLE_FILE2_PATH = get_path(BASE_PATH + "\\data\\multiplefiles\\file2.SLDPRT")

# not used yet
# LARGE_SIZE_FILE_PATH = get_path(BASE_PATH + "\\data\\largesizefile\\largesize.STP")
# LARGE_PART_SIZE_FILE_PATH = get_path(BASE_PATH + "\\data\\largesizefile\\largepartsize.STP")
