# !/bin/bash
#Script to show how to work with nested loops
#Author: Manuel Balderrabano 

echo "Nested Loops"
for fill in $(ls)
do
	for name in {1..4}
	do
		echo "File Name:$fill _ $name"
	done
done
