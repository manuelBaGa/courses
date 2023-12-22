from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import ConfirmPage
class CheckOutPage:

    def __init__(self,driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    cardFooter = (By.XPATH, "div/h4/a")
    cardButton = (By.XPATH, "div/button")
    checkOut = (By.CSS_SELECTOR, "button[class*='btn-success']")
    go_checkOut_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")


    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_element(*CheckOutPage.cardFooter)

    def getCardButton(self):
        return self.driver.find_element(*CheckOutPage.cardButton)

    def go_checkout(self):
        return self.driver.find_element(*CheckOutPage.go_checkOut_button)

    def checkoutItems(self):
        self.driver.find_element(*CheckOutPage.checkOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage

