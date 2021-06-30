# PythonAutomationFramework
This is a project for 3D HUBS QA chanllenge. Project is using Selenium, Python, HTML reports and page object model. 
This automates the official website of  3D HUBS https://www.hubs.com/

# How to install it
* Make sure you have python installed on your machine by typing in console "python --version" if not go to https://realpython.com/installing-python/#step-1-download-the-python-3-installer.
* Clone the repository to any local path.
* Run below command in CMD
  - `pip install -r requirements.txt`

# How to run it
enter the following command in cmd being located in the folder path
  - python -m pytest 
* Optional parameters
  - --html=reports/report1.html For Pytest html reporting
  - --browser <firefox, chrome> To choose different browser, default is chrome
  
* Example: `python -m pytest --html=reports/report1.html --browser=chrome`
   

# Technologies usedg
* Python 3.
* Selenium Package.
* Chromedriver.exe and geckodriver.exe for Chrome and Firefox web drivers respectively(These are installed on the fly using the Webdriver manager).
* Pytest in order to have test cases, init and tear down.
