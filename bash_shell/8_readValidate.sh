# ! /bin/bash
# Program to show how to capture user information and validate it.
# Author: Manuel Balderrabano


option=0
backupName=""
key=""

echo "Postgres Utilities program"
#Acepts one character inputs
read -n1 -p "Enter and option:" option
echo -e "\n"
read -n10 -p "Enter backup file name:" backupName
echo -e "\n"
echo "Option: $option. backupName: $backupName"
read -s -p "Clave:" key
echo "Key: $key"
