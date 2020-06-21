from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.select import Select
import utilities.custom_logger as cl
import logging
import time
import os


class SeleniumDriver():

    logging = cl.customLogger(logging.DEBUG, loggerName="SeleniumDriver")

    def __init__(self, driver):
        self.driver = driver

    def screenShot(self, resultMessage):
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.logging.info("Screenshot save to directory: " + destinationFile)
        except:
            self.logging.error("Exception Occurred when taking screenshot")

    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "plink":
            return By.PARTIAL_LINK_TEXT
        else:
            self.logging.error("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.logging.info("Element found with locator: " + locator + " and  locatorType: " + locatorType)
        except:
            self.logging.error("Element not found with locator: " + locator + " and  locatorType: " + locatorType)
        return element

    def getElementList(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.logging.info("Element list found with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.logging.error("Element list not found with locator: " + locator + " and locatorType: " + locatorType)
        return element

    def elementClick(self, locator="", locatorType="id", element=None):
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                element.click()
                self.logging.info("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
            else:
                self.logging.warning("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.logging.error("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)

    def sendKeys(self, data, locator="", locatorType="id", element=None, click=False, enter=False, waitTime=0.10):
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)

            if element is not None:
                if click:
                    element.click()
                    time.sleep(0.5)
                    self.logging.info("Clicked on element with locator: " + locator + " and locatorType: " + locatorType)
                if waitTime != 0:
                    for i in range(0, len(data)):
                        element.send_keys(data[i])
                        time.sleep(0.10)
                else:
                    element.send_keys(data)

                if enter:
                    time.sleep(0.5)
                    element.send_keys(Keys.ENTER)

                self.logging.info("Sent data on element with locator: " + locator + " and locatorType: " + locatorType)
            else:
                self.logging.error("Cannot send data on the element with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.logging.error("Cannot send data on the element with locator: " + locator + " and locatorType: " + locatorType)

    def clearField(self, locator="", locatorType="id"):
        element = self.getElement(locator, locatorType)
        if element is not None:
            element.clear()
            self.logging.info("Clear field with locator: " + locator + " and locatorType: " + locatorType)

    def getText(self, locator="", locatorType="id", element=None, info=""):
        try:
            if locator: # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.logging.info("Getting text on element :: " + info)
                self.logging.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.logging.warning("Failed to get text on element " + info)
            text = None
        return text

    def isElementPresent(self, locator="", locatorType="id", element=None):
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.logging.info("Element present with locator: " + locator + " and locatorType: " + locatorType)
                return True
            else:
                self.logging.warning("Element not present with locator: " + locator + " and locatorType: " + locatorType)
                return False
        except:
            self.logging.warning("Element not found")
            return False

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        isDisplayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.logging.info("Element is displayed")
            else:
                self.logging.info("Element not displayed")
            return isDisplayed
        except:
            self.logging.warning("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.logging.info("Element present with locator: " + locator + " and locatorType: " + str(byType))
                return True
            else:
                self.logging.warning("Element not present with locator: " + locator + " and locatorType: " + str(byType))
                return False
        except:
            self.logging.warning("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id", timeout=3, pollFrequency=0.5):
        element = None
        byType = self.getByType(locatorType)
        try:
            self.logging.info("Waiting for maximum " + str(timeout) + " seconds for element to be clickable")
            ignored_exceptions = [NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException]
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency, ignored_exceptions=ignored_exceptions)
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.logging.info("Element appeared on the web page with locator: " + locator + " and locatorType: " + str(byType))
        except:
            self.logging.warning("Element not appeared on the web page with locator: " + locator + " and locatorType: " + str(byType))
        return element

    def webScroll(self, direction=None, pixels=600):
        if direction == "up":
            self.driver.execute_script("window.scrollBy(0, " + str(-1*pixels) + ");")
        else:
            self.driver.execute_script("window.scrollBy(0, " + str(pixels) + ");")

    def selectFromList(self,locator, locatorType="xpath", index=None, value=None, text=None):
        element = self.getElement(locator=locator, locatorType=locatorType)
        try:
            sel = Select(element)

            if index is not None:
                sel.select_by_index(index)
                self.logging.info("Select using index: " + str(index) + " from Elements with locator: " + locator + " and locatorType: " + locatorType)
                return
            if value is not None:
                sel.select_by_value(value)
                self.logging.info("Select using value: " + value + " from Elements with locator: " + locator + " and locatorType: " + locatorType)
                return
            if text is not None:
                sel.select_by_visible_text(text)
                self.logging.info("Select using text: " + text + " from Elements with locator: " + locator + " and locatorType: " + locatorType)
                return
            self.logging.warning("Select Elements no method given with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.logging.error("Select Elements not present with locator: " + locator + " and locatorType: " + locatorType)

    def switchToIframe(self,index=None,name=None):
        try:
            if name is not None:
                self.driver.switch_to.frame(name)
                self.logging.info("Switch to iframe with name: " + name)
                return
            if index is not None:
                self.driver.switch_to.frame(index)
                self.logging.info("Switch to iframe with index: " + str(index))
                return
            self.logging.warning("Failed to switch to iframe no argument were given")
        except:
            self.logging.error("Failed to switch to iframe")

    def switchToDefault(self):
        try:
            self.driver.switch_to.default_content()
            self.logging.info("Switch to default content")
        except:
            self.logging.error("Failed to switch to default content")
