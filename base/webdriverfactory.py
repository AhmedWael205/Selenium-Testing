from selenium import webdriver


class WebDriverFactory():

    def __init__(self, browser, private=False, baseURL="https://courses.letskodeit.com"):
        self.browser = browser
        self.private = private
        self.baseURL = baseURL

    def getWebDriverInstance(self):

        if self.browser == "firefox":
            profile = webdriver.FirefoxProfile()
            if self.private:
                profile.set_preference("browser.privatebrowsing.autostart", True)

            driver = webdriver.Firefox(firefox_profile=profile)

        elif self.browser == "chrome":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("useAutomationExtension", False)
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            if self.private:
                chrome_options.add_argument("--incognito")

            driver = webdriver.Chrome(options=chrome_options)
        else:
            driver = webdriver.Firefox()
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(self.baseURL)
        return driver

    def gotoBaseURL(self, your_driver):
        your_driver.get(self.baseURL)
