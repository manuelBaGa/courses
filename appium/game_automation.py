import sys
import configparser
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.wait import WebDriverWait
from game.gameflow import gameflow as gmf

repo_path = sys.argv[1]
game_flow = sys.argv[2]
config = configparser.ConfigParser()
config.read(repo_path+'/appium/config.ini')

## config capabilites 
cfg_platformName = config['CAPABILITIES']['PLATFORM_NAME']
cfg_automationName = config['CAPABILITIES']['AUTOMATION_NAME']
cfg_deviceName = config['CAPABILITIES']['DEVICE_NAME']
cfg_adbExecTimeout = config['CAPABILITIES']['ADB_EXEC_TIMEOUT']
cfg_newCommandTimeout = config['CAPABILITIES']['NEW_COMMAND_TIMEOUT']
cfg_fullReset = eval(config['CAPABILITIES']['FULL_RESET'])
cfg_noReset = eval(config['CAPABILITIES']['NO_RESET'])

# config APPIUM server 
appium_server_url = config['APPIUM']['SERVER_URL']
web_driver_wait_val = config['APPIUM']['WEB_DRIVER_WAIT']
package_name = config['APPIUM']['APP_PACKAGE_NAME']

# Game mode
number_of_battles = config['GAME_MODE']['NUMBER_OF_BATTLES']

capabilities = dict(
    platformName=cfg_platformName,
    automationName=cfg_automationName,
    deviceName=cfg_deviceName,
    adbExecTimeout=cfg_adbExecTimeout,
    newCommandTimeout=cfg_newCommandTimeout,
    fullReset=cfg_fullReset,
    noReset=cfg_noReset
    )


driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
driver.update_settings({"getMatchedImageResult": True})
wait = WebDriverWait(driver, web_driver_wait_val)
my_gmf = gmf(driver, wait, repo_path)

### Game flows
if game_flow == 'event':    
    my_gmf.open_app(package_name)
    my_gmf.close_initial_game_announcements()
    my_gmf.get_event_energy()
    my_gmf.close_game(package_name)
elif game_flow == 'daily':
    my_gmf.open_app(package_name)
    my_gmf.close_initial_game_announcements()
    my_gmf.get_resources_daily_missions()
    my_gmf.get_resources_arena()
    my_gmf.get_resources_fragments()
    my_gmf.start_invasion_mission()
    my_gmf.grand_arena_battles(number_of_battles)
    my_gmf.close_game(package_name)
elif game_flow == 'arena':
    my_gmf.open_app(package_name)
    my_gmf.close_initial_game_announcements()    
    my_gmf.arena_battles()
    my_gmf.close_game(package_name)
elif game_flow == 'test':
    my_gmf.open_app(package_name)
    