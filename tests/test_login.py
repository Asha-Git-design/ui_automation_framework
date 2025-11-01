import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_login(driver):
    with open("testdata/credentials.yaml") as file:
        creds = yaml.safe_load(file)

    username = creds["username"]
    password = creds["password"]

    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # 🔸 give page time to load
    time.sleep(2)

    # 🔸 capture screenshot always
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    screenshot_path = os.path.join("reports", f"login_{timestamp}.png")
    driver.save_screenshot(screenshot_path)

    # 🔸 improved validation
    assert "Secure Area" in driver.page_source, "Login failed!"
