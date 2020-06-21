import time
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage


class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG, "RegisterCoursesPage")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators
    _search_box = "//input[contains(@placeholder,'Search')]"
    _search_box_locator = "xpath"
    _course = "//div/h4[contains(text(),'{0}')]"
    _course_locator = "xpath"
    _enroll_button = "//div/button[contains(text(),'Enroll')]"
    _enroll_button_locator = "xpath"
    _cc_num_iframe_name = "__privateStripeFrame5"
    _cc_num = "//input[@placeholder='Card Number']"
    _cc_num_locator = "xpath"
    _cc_exp_iframe_name = "__privateStripeFrame7"
    _cc_exp = "//input[@placeholder='MM / YY']"
    _cc_exp_locator = "xpath"
    _cc_cvv_iframe_name = "__privateStripeFrame6"
    _cc_cvv = "//input[@placeholder='CVC']"
    _cc_cvv_locator = "xpath"
    _country_field = "//select[@name='country-list']"
    _country_field_locator = "xpath"
    _submit_enroll = "//button[@class='zen-subscribe sp-buy btn btn-default btn-lg btn-block btn-gtw btn-submit checkout-button dynamic-button']"
    _submit_enroll_locator = "xpath"
    _enroll_error_message = "//span[contains(text(),'invalid') or contains(text(),'incorrect')]"
    _enroll_error_message_locator = "xpath"

    ############################
    ### Element Interactions ###
    ############################

    def enterCourseName(self, name):
        self.sendKeys(name, locator=self._search_box, locatorType=self._search_box_locator, enter=True)

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locator=self._course.format(fullCourseName), locatorType=self._course_locator)

    def clickOnEnrollButton(self):
        self.elementClick(locator=self._enroll_button,locatorType=self._enroll_button_locator)

    def enterCardNum(self, num):
        self.switchToIframe(name=self._cc_num_iframe_name)
        self.sendKeys(num, locator=self._cc_num, locatorType=self._cc_num_locator, click=True, waitTime=0)
        self.switchToDefault()

    def enterCardExp(self, exp):
        self.switchToIframe(name=self._cc_exp_iframe_name)
        self.sendKeys(exp, locator=self._cc_exp, locatorType=self._cc_exp_locator, click=True)
        self.switchToDefault()

    def enterCardCVV(self, cvv):
        self.switchToIframe(name=self._cc_cvv_iframe_name)
        self.sendKeys(cvv, locator=self._cc_cvv, locatorType=self._cc_cvv_locator, click=True)
        self.switchToDefault()

    def selectCountry(self,country):
        self.selectFromList(locator=self._country_field, locatorType=self._country_field_locator, text=country)

    def clickEnrollSubmitButton(self):
        self.elementClick(locator=self._submit_enroll, locatorType="xpath")

    def enterCreditCardInformation(self, num, exp, cvv, country):
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)
        self.selectCountry(country)
        self.enterCardNum(num)

    def enrollCourse(self, num="", exp="", cvv="", country="Egypt"):
        self.clickOnEnrollButton()
        time.sleep(5)
        self.webScroll(direction="down", pixels=600)
        self.enterCreditCardInformation(num, exp, cvv, country)
        self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        messageElement = self.waitForElement(self._enroll_error_message, locatorType=self._enroll_error_message_locator)
        result = self.isElementDisplayed(element=messageElement)
        return result

    def login(self):
        lp = LoginPage(self.driver)
        lp.login("test@email.com", "abcabc")

    def logout(self):
        lp = LoginPage(self.driver)
        lp.logout()
