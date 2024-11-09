*** Settings ***

Library        SeleniumLibrary
Library        SikuliLibrary    mode=NEW
Suite Setup    Start Sikuli Process
Suite Teardown    Stop Remote Server


*** Variables ***
${game_link}    https://www.nutaku.net/games/presidents-ambition-r/play/
${home}         https://www.nutaku.net/home/
${user}        ma_baga@outlook.com
${password}    mabg271195nn
${IMAGE_DIR}      ${CURDIR}${/}images
${image}          bulletin_board.png

${lnd_login_main_btn}              //div/span[text()="Login"]
${lnd_login_email}                 //input[@name="email"]
${lnd_login_password}              //input[@name="password" and not(@autocomplete="new-password")]
${lnd_login_secondary_btn}         //button/span[text()="Login"]
${lnd_rewards_calendar_icon}       //div[@data-modal="daily-rewards-calendar"]
${lnd_claim_reward_btn}            //button[text()=" Claim Reward "]


*** Test Cases ***
Login Test

    ${options}=    Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys, selenium.webdriver
    Call Method    ${options}    add_argument    incognito
    Create WebDriver    Chrome    options=${options}
    Go To    ${home}
    #Click on Log In button
    SeleniumLibrary.Click Element    ${lnd_login_main_btn}
    SeleniumLibrary.Input Text    ${lnd_login_email}    ${user}
    SeleniumLibrary.Input Password    ${lnd_login_password}    ${password}
    SeleniumLibrary.Click Element    ${lnd_login_secondary_btn}
    Sleep    10

Finding Image
    
    Add Image Path    ${IMAGE_DIR}
    Log To Console    ${IMAGE_DIR}
    ${options}=    Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys, selenium.webdriver
    Call Method    ${options}    add_argument    incognito
    Create WebDriver    Chrome    options=${options}
    Go To    ${home}
    Maximize Browser Window
    #Click on Log In button
    SeleniumLibrary.Click Element    ${lnd_login_main_btn}
    SeleniumLibrary.Input Text    ${lnd_login_email}    ${user}
    SeleniumLibrary.Input Password    ${lnd_login_password}    ${password}
    SeleniumLibrary.Click Element    ${lnd_login_secondary_btn}
    Sleep    5
    Go To    ${game_link}
    Wait Until Screen Contain    ${IMAGE_DIR}${/}${image}    15

        #Wait For    bulletin_board
*** Keywords ***