# !/bin/bash
# Script to show how to work with if else conditionals
# Author: Manuel Balderrabano

classScore=0
age=0

echo "Example If -else"
read -n1 -p "Write your note (1-9):" classScore
echo -e "\n"

if (( $classScore >= 7 )); then
	echo "Student will pass the subject"
else
	echo "Student will fail the subject"
fi

read -p "Write your age: " age

if [ $age -le 18 ]; then
	echo "This person can't vote yet"
else
	echo "This person can vote!"
fi
