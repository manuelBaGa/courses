# !/bin/bash
# Script to show how to work with nested if else conditionals
# Author: Manuel Balderrabano

classScore=0


echo "Example If -else"
read -n1 -p "Write your note (1-9):" classScore
echo -e "\n"

if [ $classScore -ge 7 ]; then
	echo "The student pass the subject"
	read -p "The student will continue studying? (y/n):" continueVar
	if [ $continueVar = "y" ]; then
		echo "Welcome to the next level"
	else
		echo "Thank you for working with us, good luck!"
	fi
else
	echo "The student fails the subject"
fi
