#! /bin/bash
#Program to help postgress management.
#Author: Manuel Balderrabano

option=0

#Install postgress function
install_postgress() {
	echo -e "\nInstall Postgress..."

}


#Uninstall postgress function
uninstall_postgress() {
	echo-e "\nUninstall Postgress..."
}

#Crate backup function
create_backup() {
	echo -e "\nCreating backup..."
	echo -e "\nBackup location: $1"
}


#Restore backup function
restore_backup() {
	echo -e "\nBringing back files from backup..."
	echo -e "\nBackup location: $1"
}

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
		install_postgress
		sleep 3
		;;
		2)
		uninstall_postgress
		sleep 3
		;;
		3)
		read -p "Location to create backup:" directorioBackup
		create_backup $directorioBackup
		sleep 3
		;;
		4)
		read -p "Backup adress:" backupAdress
		restore_backup $backupAdress
		sleep 3
		;;
		5)
		echo "Exit .........."
		exit 0
		;;
	esac
done
