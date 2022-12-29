# !/bin/bash
#Script to show how to work with for loop
#Author: Manuel Balderrabano 

numbersArray=(1 2 3 4 5 6)
echo "Iterate numbers' list"
for num in ${numbersArray[*]}
do
	echo "Number: $num"
done

echo -e "\nIterate strings' list"
for name in "Marco" "Pedro" "Luis" "Daniela"
do
	echo "Names: $name"
done

echo -e "\nIterate files"
for file in *
do
	echo "Files Names: $file"
done

echo -e "\nIterate using a command"
for command in $(ls)
do
	echo "Files Names: $command"
done

echo -e "\nIterate using traditional format"
for ((i=1; i<10; i++))
do
	echo "Number: $i"
done
