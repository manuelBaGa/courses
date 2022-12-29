# !/bin/bash
# Script to show how to work with conditional expressions
# Author: Manuel Balderrabano

age=0
country=""
filePath=""

read -p "Write your age: " age
read -p "Write your country: " country
read -p "Write your file path: " filePath

echo -e "\nConditional expressions with numbers"
if [ $age -lt 10 ]; then
	echo "This person is a child"
elif [ $age -ge 10 ] && [ $age -le 17 ]; then
	echo "This person is a teeneger"
else
	echo "This person is and adult"
fi


echo -e "\nConditional expressions with strings"
if [ $country = "USA" ]; then
	echo "This person is a American"
elif [ $country = "Ecuator" ] || [ $country = "Colmbia" ]; then
	echo "This person is from South-America"
else
	echo "Unknown nationality"
fi

echo -e "\nConditional expressions with files"
if [ -d $filePath ]; then
	echo "The adress file $filePath exists"
else
	echo "The adress file $filePath doesn't exist"
fi
