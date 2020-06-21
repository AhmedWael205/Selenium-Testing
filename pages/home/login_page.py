from pages.home.navigation_page import NavigationPage
from base.basepage import BasePage
import time


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _login_link = "//a[contains(text(),'Sign In')]"
    _login_link_locator = "xpath"
    _email_field = "//div[@class='text-center zen-login']//input[@id='email']"
    _email_locator = "xpath"
    _password_field = "//input[@id='password']"
    _password_locator = "xpath"
    _login_button = "//input[@value='Login']"
    _login_button_locator = "xpath"
    _logout_button = "//a[contains(text(),'Logout')]"
    _logout_button_locator = "xpath"
    _user_settings_icon = "//img[@src='/images/default-user-profile-pic.png']"
    _user_settings_icon_locator = "xpath"
    _after_login_title = "All Courses"
    _invalid_login = "//div[contains(@class,'error')]/span[contains(text(),'Your username or password is invalid.')]"
    _invalid_login_locator = "xpath"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType=self._login_link_locator)

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType=self._email_locator)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType=self._password_locator)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType=self._login_button_locator)

    def login(self, email="", password=""):
        if self.isElementPresent(locator=self._user_settings_icon, locatorType=self._user_settings_icon_locator):
            return
        self.clickLoginLink()
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        self.waitForElement(self._user_settings_icon, locatorType=self._user_settings_icon_locator)
        result = self.isElementPresent(locator=self._user_settings_icon, locatorType=self._user_settings_icon_locator)
        return result

    def verifyLoginFailed(self):
        return self.isElementPresent(locator=self._invalid_login, locatorType=self._invalid_login_locator)

    def verifyLoginTitle(self):
        return self.verifyPageTitle(self._after_login_title)

    def logout(self):
        if self.nav.navigateToUserSettings():
            time.sleep(1)
            logoutLinkElement = self.waitForElement(locator=self._logout_button, locatorType=self._logout_button_locator)
            self.elementClick(element=logoutLinkElement)
            return True
        else:
            return False

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field, locatorType=self._email_locator)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field, locatorType=self._password_locator)
        passwordField.clear()
