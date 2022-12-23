# ! /bin/bash
# Program to show how to send options with or without parameters.
# Author: Manuel Balderrabano

echo "Options program"
echo "Option 1 sent: $1"
echo "Option 2 sent: $2"
echo "Options sent: $3"
echo -e "\n"
echo "Retrieve values"
while [ -n "$1" ]
do
case "$1" in
-a) echo "-a used option";;
-b) echo "-b used option";;
-c) echo "-c used option";;
*) echo "$1 is not an option";;
esac
shift
done
