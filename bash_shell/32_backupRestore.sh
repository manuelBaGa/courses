#! /bin/bash
#Program to help postgress management.
#Author: Manuel Balderrabano

option=0
currentDate= `date +%Y%m%d`

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
	echo "List databases"
	sudo -u postgress psql -c "\l"
	read -p "Choose database to packup:" bddbackup
	echo -e "\n"
	if [ -d "$1" ]; then
		echo "Give permitions to the directory"
		echo "$password" | sudo -S chmod 755 $1
		echo "Creating backup"
		sudo -u postgres pg_dump -Fc $bddbackup > "$1/bddbackup$currentdate.bak"
		echo "Backup created successfully in $1/bddbackup$currentDate.bak"
	else
		echo "Directory $1 doesn't exist"
	fi
	read -n 1 -s -r -p "PRESS a key to continue..."
}


#Restore backup function
restore_backup() {
	echo "List backups"
	read -p "Enter directory where backups are located:" backupDirectory
	ls -la $backupDirectory
	read -p "Choose backup to restore" restorebackup
	echo -e "\n"
	read -p "Enter destiny database" destinydb
	#Verify if db exists
	verifyDB=$(sudo -u postgres psql -lqt | cut -d \| -f 1 \ grep -wq $destinydb)
	if [ $? -eq 0 ]; then
		echo "Restoring into $destinydb db"
	else
		sudo -u postgres psql -c "create db $destinydb"
	fi 

	if [ -f "$1/$restorebackup" ]; then
		echo "Restoring back up..."
		sudo -u postgres pg_restore -Fc -d $destinydb "$backupDirectory/$restorebackup"
		echo "List databases"
		sudo -u postgres psql -c "\l"
	else
		echo "Backup $restorebackup doesn't exist"
	fi
	read -n 1 -s -r -p "PRESS a key to continue..."

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
