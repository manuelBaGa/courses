from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
# Getting the list of products names
driver.get("https://www.rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(4)

results = driver.find_elements(By.XPATH, "//div[@class='products']/div") #list[]
count = len(results)
actualList = []
expectedList = ['Cucumber - 1 kg', 'Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
assert count > 0
for result in results:
    actualList.append(result.find_element(By.XPATH,"h4").text)
    result.find_element(By.XPATH,"div/button").click()

assert expectedList == actualList

# Sum validations
prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
total_sum = 0
for price in prices:
    total_sum = total_sum + int(price.text)

print(total_sum)
totalAmount = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert total_sum == totalAmount

#Apply promotion code
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

# Explicit wait
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

discountedAmount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
assert totalAmount > discountedAmount

driver.close()