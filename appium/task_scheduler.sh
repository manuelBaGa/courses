#!/bin/bash
AUTOMATION_SEQUENCE=$1
appium --use-plugins images &
source <(grep = $COURSES_PATH/appium/config.ini)
DEVICE_ID=$($ADB_DIR devices | grep device | awk 'FNR==2 {print $1'})
$ADB_DIR -s $DEVICE_ID shell input keyevent KEYCODE_POWER
sleep 2
$ADB_DIR -s $DEVICE_ID shell input swipe 400 1200 400 100 
sleep 2
$ADB_DIR -s $DEVICE_ID shell input text $DEVICE_CODE
sleep 2
py -u $AUTOMATION_SCRIPT $COURSES_PATH $AUTOMATION_SEQUENCE || true
$ADB_DIR -s $DEVICE_ID shell input keyevent KEYCODE_POWER
NODEJS_PID=$(ps | grep nodejs | awk {'print $1'})
kill $NODEJS_PID
sleep 5
