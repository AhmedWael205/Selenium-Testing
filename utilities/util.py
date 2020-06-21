class Util(object):

    def verifyTextContains(self, actualText, expectedText):
        if expectedText.lower() in actualText.lower():
            return True
        else:
            return False

    def verifyTextMatch(self, actualText, expectedText):
        if actualText.lower() == expectedText.lower():
            return True
        else:
            return False
