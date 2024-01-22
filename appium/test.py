import base64
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
import time

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    adbExecTimeout=90000
)

appium_server_url = 'http://localhost:4723'

with open(r".\images\enter_btn.png", "rb") as image_file:
    image_base64 = base64.b64encode(image_file.read()).decode("utf-8")

with open(r".\images\close_btn.png", "rb") as image_file:
    close_btn_img = base64.b64encode(image_file.read()).decode("utf-8")


driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
driver.update_settings({"getMatchedImageResult": True})
wait = WebDriverWait(driver,40)

TouchAction(driver).tap(None,1613, 1401,1).perform()
wait.until(lambda x: x.find_element(by=AppiumBy.IMAGE, value=image_base64))
print("Ya encontré el elemento")
TouchAction(driver).tap(None,809, 2329,1).perform()
close_btn = wait.until(lambda x: x.find_element(by=AppiumBy.IMAGE, value=close_btn_img))
print("Ya encontré el boton de cerrar")
close_btn.click()

driver.quit()