# ! /bin/bash
# Program to show how to capture user information using read.
# Author: Manuel Balderrabano


option=0
backupName=""


echo "Postgres Utilities program"
read -p "Enter and option:" option
read -p "Enter backup file name:" backupName
echo "Option: $option. backupName: $backupName"
