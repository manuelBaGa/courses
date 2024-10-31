from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#Chrome Driver - Chrome Browser
#service_obj = Service()

#driver = webdriver.Chrome(service=service_obj)
#driver.get("https://www.rahulshettyacademy.com/")

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/")
print(driver.title)
print(driver.current_url)
driver.get("https://www.rahulshettyacademy.com/seleniumPractise/#/")
driver.back()
driver.refresh()
driver.forward()
driver.minimize_window()
driver.close()

