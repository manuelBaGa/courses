# !/bin/bash
#Script to show how to write on  a file.
#Author: Manuel Balderrabano 

echo "Write on a file"

echo "Values writen with echo" >> $1

#Adding multiline
cat <<EOM >> $1
$2
EOM
