#! /bin/bash
#Program to help postgress management.
#Author: Manuel Balderrabano

option=0

while :
do
	#Clear screen
	clear
	#Diplay options menu
	echo "___________________________________"
	echo "_______Postgress Management________"
	echo "___________________________________"
	echo "___________Main screen_____________"
	echo "___________________________________"
	echo "1. Install Postgress"
	echo "2. Uninstall Postgress"
	echo "3. Create Backup"
	echo "4. Restore Backup"
	echo "5. Exit"

	#Read user data
	read -n1 -p "Insert an option [1-5]:" option

	#Validate entered option
	case $option in
		1)
		echo -e "\nInstall postgress.........."
		sleep 3
		;;
		2)
		echo -e "\nUninstall postgress.........."
		sleep 3
		;;
		3)
		echo -e "\nCreate Backup.........."
		sleep 3
		;;
		4)
		echo -e "\nRestore Backup.........."
		sleep 3
		;;
		5)
		echo "Exit .........."
		exit 0
		;;
	esac
done
