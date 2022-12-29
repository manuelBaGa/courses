# !/bin/bash
# Script to show how to work with case
# Author: Manuel Balderrabano

option=""

echo "Example case instance"
read  -p "Write one option from A - Z:" option
echo -e "\n"

case $option in
	"A") echo -e "\nSave option";;
	"B") echo "Delete option";;
	[C-E]) echo "There is no option implemented";;
	*) echo "Incorrect option";;
esac
