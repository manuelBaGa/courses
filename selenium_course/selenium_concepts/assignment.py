import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://www.rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CSS_SELECTOR,".blinkingText").click()
browserWindows = driver.window_handles
driver.switch_to.window(browserWindows[1])
email = driver.find_element(By.XPATH,"//p[@class='im-para red']/strong/a").text
driver.switch_to.window(browserWindows[0])
driver.find_element(By.ID,"username").send_keys(email)
driver.find_element(By.ID,"password ").send_keys("mytestpassword")
driver.find_element(By.ID,"signInBtn").click()
wait = WebDriverWait(driver,5)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)


time.sleep(2)
driver.close()