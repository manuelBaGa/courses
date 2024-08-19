#!/bin/zsh
date
AUTOMATION_SEQUENCE=$1
appium --use-plugins=images --log-level=warn &
source <(grep = $COURSES_PATH/appium/config.ini) #$COURSES_PATH/appium/config.ini)
DEVICE_ID=$($ADB_DIR devices | grep device | awk 'FNR==2 {print $1}')
SCREEN_STATUS_LOCK=$($ADB_DIR -s $DEVICE_ID shell dumpsys power | grep -E "mHoldingWakeLockSuspendBlocker=true")
SCREEN_STATUS_DISPLAY=$($ADB_DIR -s $DEVICE_ID shell dumpsys power | grep -E "mHoldingDisplaySuspendBlocker=true")

#If the device display is off then turn it on, then verify if the device is locked, if yes, unlock it. 
if [[ -n $SCREEN_STATUS_DISPLAY ]]
then
    echo "La pantalla del dispositivo ya está activa"
else    
    echo "Encendiendo la pantalla del dispositivo"
    $ADB_DIR -s $DEVICE_ID shell input keyevent KEYCODE_POWER
fi

sleep 5

echo "Desbloqueando dispositivo"
$ADB_DIR -s $DEVICE_ID shell input keyevent 82
sleep 2
$ADB_DIR -s $DEVICE_ID shell input text $DEVICE_CODE
sleep 2

python3 -u $AUTOMATION_SCRIPT $COURSES_PATH $AUTOMATION_SEQUENCE #|| true

$ADB_DIR -s $DEVICE_ID shell input keyevent KEYCODE_POWER
NODEJS_PID=$(ps -e| grep "/opt/homebrew/bin/appium" | awk 'FNR==1 {print $1}')
kill $NODEJS_PID
sleep 5