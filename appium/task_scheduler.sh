#!/bin/bash
source <(grep = $COURSES_PATH/appium/config.ini)
DEVICE_ID=$($ADB_DIR devices | grep device | awk 'FNR==2 {print $1'})
$ADB_DIR -s $DEVICE_ID shell input keyevent KEYCODE_POWER
sleep 2
$ADB_DIR -s $DEVICE_ID shell input swipe 400 1200 400 100 
sleep 2
$ADB_DIR -s $DEVICE_ID shell input text $DEVICE_CODE
sleep 2
py -u $AUTOMATION_SCRIPT $COURSES_PATH $AUTOMATION_SEQUENCE_HOUR || true
$ADB_DIR -s $DEVICE_ID shell input keyevent KEYCODE_POWER
