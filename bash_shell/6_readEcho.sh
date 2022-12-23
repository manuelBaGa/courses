# ! /bin/bash
# Program to show how to capture user information using echo and read.
# Author: Manuel Balderrabano


option=0
backupName=""


echo "Postgres Utilities program"
echo -n "Enter and option:"
read
option=$REPLY
echo -n "Enter backup file name:"
read
backupName=$REPLY
echo "Option: $option. backupName: $backupName"
