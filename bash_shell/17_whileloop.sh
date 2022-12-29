# !/bin/bash
#Script to show how to work with while loop
#Author: Manuel Balderrabano 

number=1

while [ $number -ne 10 ]
do 
	echo "Print $number times"
	number=$(( number + 1 ))
done
