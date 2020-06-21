import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _home = "//a[contains(text(),'HOME')]"
    _all_courses = "//a[contains(text(),'ALL COURSES')]"
    _user_settings_icon = "//img[@src='/images/default-user-profile-pic.png']"


    def navigateToAllCourses(self):
        self.elementClick(locator=self._all_courses, locatorType="xpath")

    def navigateToHome(self):
        self.elementClick(locator=self._home, locatorType="xpath")

    def navigateToUserSettings(self):
        userSettingsElement = self.waitForElement(locator=self._user_settings_icon,locatorType="xpath", pollFrequency=1)
        if userSettingsElement is None:
            return False
        self.elementClick(element=userSettingsElement)
        return True
