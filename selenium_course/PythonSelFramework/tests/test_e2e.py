import time

from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage

#@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):

        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        log.info("Getting all the card titles")
        products = checkOutPage.getCardTitles()
        for product in products:
            productName = product.text
            if productName == "Blackberry":
                checkOutPage.cardButton().click()

        checkOutPage.go_checkout().click()

        confirmpage = checkOutPage.checkoutItems()
        log.info("Entering country name")
        confirmpage.search_country_box().send_keys("ind")
        self.verifyLinkPresence("India")
        confirmpage.found_word().click()
        confirmpage.mark_checkbox()

        confirmpage.submit_button().click()
        successText = confirmpage.alert_result().text
        log.info("Text received from application is "+successText)
        assert "Success! Thank you!" in successText
        time.sleep(2)
