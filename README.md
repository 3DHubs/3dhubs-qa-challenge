# 3dhubs-qa-challenge
Manual for automation tests (windows env)
The tests are for files upload for 'CNC machining'.

* You need to have installed: python, pycharm, chrome browser.

1.Download the project to a directory with "git clone <the project here>"

2.In pycharm configure to use pytest.

3.In pycharm create a new virtual env.

4.In pycharm terminal run the  next command "pip install -r requirements.txt" to install all required packages.

*Note: If the downloaded chrome driver(in the root directory) compatible with your chrome browser version then 
you can download a new chrome driver and replace it with the existing chrom driver
Firstly check the chrome browser version, you can download it from here:

https://chromedriver.chromium.org/downloads

Command to run the testes for example, to check multiple files upload:

In pycharm terminal go to -> tests directory and run the following command:

pytest upload_multiple_files_test.py --env="prod" --headless="false"

--env var is on what environment do you want to run the tests and --headless env determines if you want run the tests on the background(True) or not(False).

