# 3D Hubs QA Challenge
This application demonstrates following functionalities-
1. Developing basic web automation framework
2. Automating https://www.hubs.com/manufacture for file upload scenario
3. Reporting the test results in *TestReport.html* file, which can be found the project folder

## Implementation
- File upload in Manufacture page is automated using **Selenium** webdriver, **pytest** library.
  - To run pytest tests-
  - `pytest <3dhubs-qa-challenge> --html=TestReport.html` or 
  `pytest <test_hubs_manufacture.py fullpath> --html=TestReport.html` 
- Application has a following folder structure-
  - **3dhubs-qa-challenge** - Project folder
    - **pages** - contains all the page object models
      - **common.py** - contains all the common web interaction APIs
      - **home_page.py** - contains all the APIs specific to home page
      - **manufacture_page.py** - contains all the APIs specific to manufacture page
    - **test_data** - contains test data (3d models)
    - **conftest.py** - contains common text fixtures like (Web Driver instantiation and yielding it)
    - **manufacture_test_data.py** - contains test data like, filepaths.
    - **README.md** - read me file
    - **requirements.txt** - contains all the required python libraries
    - **test_hubs_manufacture.py** - contains pytest test scripts
    - **TestReport.html** - Test Report file

- Type checking has been performed using **mypy** library.
  - Command-
    `mypy <3dhubs-qa-challenge fullpath>` or `mypy <python moule fullpath>`
- Test scripts are currently feasible with Firefox browser, which can be run on other browsers as well. 
- API documentation can be found in *docs/build/html/index.html* file. This file is generated using sphinx documentation library.
- `pylint` library is used to ensure that coding standards are met and to detect if there are any hidden errors.

**Note:**
- `Selenium`, `pytest`, `pylint` and `mypy` libraries should be installed on the running PC.