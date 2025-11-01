import os
from datetime import datetime


def capture_screenshot(driver, test_name):
    screenshots_dir = "reports/screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)
    file_path = os.path.join(
        screenshots_dir, f"{test_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
    driver.save_screenshot(file_path)
    return file_path
