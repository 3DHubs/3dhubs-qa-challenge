# 3dhubs-qa-challenge
## Description
The app tests uploading function of the page https://www.hubs.com/manufacture/

Test scenarios include:
- upload one file in correct type successfully
- upload multiple files in correct types successfully
- upload a file in non design type
- upload a file in stl type
- upload an assembly file
- upload a file of more than 128MB (not implemented as no available file is found)
- upload a file with size of more than 3000mm (not implemented as no available file is found)

## Running the test
### Prerequites
chrome browser and python3 is installed;

chromedriver.exe in chromedriver/windows is for windows chrome version 90, and chromedriver in chromerdriver/linux is 
for linux chrome version 89. Replace them with right version to match your chrome if needed.
### in Windows:
- $ python3 -m venv venv
- $ venv\Scripts\activate.bat
- $ pip install -r requirements.txt
- $ pytest --html=report.html
### in Linux:
- $ python3 -m venv venv
- $ source venv/bin/activate
- $ pip install -r requirements.txt
- $ pytest --html=report.html

All the commands should be executed in directory of the repo. A test report is generated after the test is finished.
