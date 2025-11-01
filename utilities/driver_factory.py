from selenium import webdriver


def get_driver(browser="chrome"):
    if browser.lower() == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)
        return driver
    else:
        raise Exception("Unsupported browser!")
