# !/bin/bash
#Script to show how to work with files and directories.
#Author: Manuel Balderrabano 

echo "Files - Directories"

if [ $1 = "d" ] ; then
	mkdir -m 755 $2
	echo "Directory created succesfully"
	ls -la $2
elif [ $1 = "f" ] ; then
	touch $2
	echo "File created succesfully"
	ls -la $2
else
	echo "There is no option: $1"
fi

