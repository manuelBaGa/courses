# !/bin/bash
#Script to show how to work break and Continue
#Author: Manuel Balderrabano 

echo "Break and Continue instances"
for fill in $(ls)
do
	for name in {1..4}
	do
		if [ $fill == "10_download.sh" ]; then
			break;
		elif [[ $fill == 4* ]]; then
			continue;
		else
			echo "File Name:$fill _ $name"
		fi
	done
done
