# 3dhubs-qa-challenge
This is a repository for hubs.com autotests.

Test framework was built using pytest and Playwright.

## Set up interpreter inside pipenv

`pip install --user pipenv`

`pipenv sync` - to install dependencies from Pipfile.lock

`playwright install` - to install browser drivers

## Running tests
`pipenv run pytest` - to run tests

By default, Playwright runs tests in headless mode.
To run tests in headed mode, please use

`pipenv run pytest --headed`

## Allure reports

To use Allure as a report tool, install it following instructions from here:

https://docs.qameta.io/allure-report/

To collect logs for allure report and store them in `allurelogs`, please run

`pipenv run pytest --headed --alluredir=allurelogs`

To generate report with collected logs from `allurelogs`, please run

`allure generate allurelogs --clean`

You can find generated html-report in `allure-report/index.html`
