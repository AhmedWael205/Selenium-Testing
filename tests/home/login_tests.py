from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG, loggerName="LoginTests")

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.log.info("test_invalidLogin started\n")
        self.lp.logout()
        self.lp.login("test@email.com", "abcabcabc")
        result = self.lp.verifyLoginFailed()
        self.log.info("test_invalidLogin ended\n\n")
        assert result == True

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.log.info("test_validLogin started\n")
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title Verification")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login Verification")
        self.log.info("test_validLogin ended\n\n")