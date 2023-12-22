import pytest

from testData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):

        log = self.getLogger()
        homepage = HomePage(self.driver)

        log.info("first name is "+getData["name"])
        homepage.getName().send_keys(getData["name"])
        homepage.getEmail().send_keys(getData["email"])
        homepage.getPassword().send_keys("123456")

        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(),getData["gender"])

        homepage.submitForm().click()
        message = homepage.getSuccessMessage().text

        print(message)
        assert "Success" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase1"))
    def getData(self,request):
        return request.param
