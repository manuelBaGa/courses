from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ConfirmPage:


    def __init__(self,driver):
        self.driver = driver

    input_country = (By.ID, "country")
    word_to_search = (By.LINK_TEXT, "India")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit = (By.CSS_SELECTOR, "input[type='submit']")
    alert = (By.CLASS_NAME, "alert-success")
    def search_country_box(self):
        return self.driver.find_element(*ConfirmPage.input_country)

    def found_word(self):
        return self.driver.find_element(*ConfirmPage.word_to_search)

    def mark_checkbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def submit_button(self):
        return self.driver.find_element(*ConfirmPage.submit)

    def alert_result(self):
        return self.driver.find_element(*ConfirmPage.alert)