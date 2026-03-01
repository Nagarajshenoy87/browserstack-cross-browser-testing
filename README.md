# Cross-Browser Testing using Selenium and BrowserStack

## Project Overview
This project demonstrates automated cross-browser testing of a login page using Selenium integrated with BrowserStack cloud testing platform.

The automation script tests the login functionality of a sample website to ensure it works correctly across different browsers.

## Tools Used
- Python
- Selenium WebDriver
- BrowserStack
- Chrome
- Microsoft Edge
- Mozilla Firefox

## Test Scenario
The automated test performs the following steps:

1. Open the login page
2. Enter username
3. Enter password
4. Click the login button
5. Verify successful login

Test Website:
https://practicetestautomation.com/practice-test-login/


## How to Run the Test

1. Install Selenium

pip install selenium

2. Add BrowserStack Credentials in the script

USERNAME = "your_browserstack_username"
ACCESS_KEY = "your_browserstack_access_key"

3. Run the test

python test_login.py

The test will run on BrowserStack cloud browsers.

## Test Results

Browser | OS | Result
------- | ------- | -------
Chrome | Windows 11 | Passed
Edge | Windows 11 | Passed
Firefox | Windows 11 | Passed

## Screenshots
Screenshots of BrowserStack Automate dashboard and test execution are included in the project.

## Learning Outcome
Through this project I learned:

- Selenium automation basics
- Cross-browser testing
- Running Selenium tests on BrowserStack cloud
- Testing web applications across different browsers

## Author
Software Testing Intern
