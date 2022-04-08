class ManufactureElementsExpectedProps:
    BUTTON_select_files = {
        'is_displayed': True,
        'expected_aria_role': 'button'
    }
    DIV_error_file_unsupported = {
        'is_displayed': True,
        'expected_aria_role': 'div',
        'text': 'files are not supported. Please upload your parts in one of the following formats: STL, OBJ, '
                'STEP, STP, IGES, IGS, SLDPRT, 3DM, SAT, X_T or DXF.'
    }
    INPUT_email_wall = {
        'is_displayed': True,
        'expected_aria_role': 'input'
    }
    IMG_analyzing_parts = {
        'is_displayed': True,
        'expected_aria_role': 'img'
    }

