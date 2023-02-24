#! /bin/bash
#Program to help postgress management.
#Author: Manuel Balderrabano

option=0

#Install postgress function
install_postgress() {
	echo -e "\n Verifying if postgress is already installed..."
	verifyinstall=$(echich psql)
	if [ $? -eq 0 ]; then
		echo -e "\nPostgress is already installed"
	else
		read -s -p "Enter sudo password:" password
		read -s -p "Enter postgress password" passwordPostgress
		echo "$password" | sudo -S apt update
		echo "$password" | sudo -S apt-get -y install postgresql-contrib
		sudo -u postgres psql -c "ALTER USER postgres WITH PASSWORD '{$passwordPostgress}';"
		echo "$password" | sudo -S systemctl enable postgresql.service
		echo "$password" | sudo -S systemctl start postgresql.service
	fi
	read -n 1 -s -r -p "PRESS a key to continue..."
}


#Uninstall postgress function
uninstall_postgress() {
	read -s -p "Enter sudo password:" password
	echo -e "\n"
	echo "$password" | sudo -S systemctl stop postgresql.service
	echo "$password" | sudo -S apt-get -y --purge remove postgresql\*
	echo "$password" | sudo -S rm -r /etc/postgresql
	echo "$password" | sudo -S rm -r /etc/postgresql-common
	echo "$password" | sudo -S rm -r /var/lib/postgresql
	echo "$password" | sudo -S userdel -r postgres /etc/postgresql
	echo "$password" | sudo -S groupdel postgresql
	read -n 1 -s -r -p "PRESS a key to continue..."	
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
