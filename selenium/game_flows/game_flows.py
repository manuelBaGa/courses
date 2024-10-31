from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
import configparser
import time

config = configparser.ConfigParser()
config.read('./config.ini')

##get from configfile
email = config['ACCOUNT']['EMAIL']
password = config['ACCOUNT']['PASSWORD']

service_obj = Service()
chrome_options_obj = Options()
chrome_options_obj.add_argument("--incognito")
driver = webdriver.Chrome( service = service_obj, options = chrome_options_obj)
wait = WebDriverWait(driver, 10)

driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://www.nutaku.net/games/aeons-echo/play")
wait.until(EC.presence_of_element_located((By.XPATH, "//header//span[text()='Login']")))
driver.find_element(By.XPATH, "//header//span[text()='Login']").click()
wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='modal-box signup-login rounded js-modal-box open']")))

driver.find_element(By.XPATH, "//input[@name='email']").send_keys(email)
driver.find_element(By.XPATH, "//div[@class='flx content-login js-content-login']//input[@name='password']").send_keys(password)
driver.find_element(By.XPATH, "//button/span[text()='Login']").click()

time.sleep(3)
wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
driver.find_element(By.XPATH, "//button[@type='submit']").click()



time.sleep(10)
driver.close()

