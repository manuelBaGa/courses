# !/bin/bash
#Script to show how to read on  a file.
#Author: Manuel Balderrabano 

echo "Read a file"
cat $1
echo -e "\nAlmacenar los valores en una variable"
valorCat=`cat $1`
echo "$valorCat"

# defining an internal field separator
echo -e "\nRead files line by line using while"
while IFS= read linea
do
	echo "$linea"
done < $1
