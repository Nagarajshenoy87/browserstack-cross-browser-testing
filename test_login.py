from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

USERNAME = "nagrajshenoy_aeqkNX"
ACCESS_KEY = "3spqxxyv9NAzCswvuzaY"

url = "https://practicetestautomation.com/practice-test-login/"

options = Options()

options.set_capability("browserName", "Chrome")
options.set_capability("browserVersion", "latest")

options.set_capability("bstack:options", {
    "os": "Windows",
    "osVersion": "11",
    "sessionName": "Chrome Login Test"
})

driver = webdriver.Remote(
    command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub",
    options=options
)

driver.get(url)

driver.find_element(By.ID,"username").send_keys("student")
driver.find_element(By.ID,"password").send_keys("Password123")

driver.find_element(By.ID,"submit").click()

time.sleep(5)

driver.quit()