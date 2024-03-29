11_ifElse.sh                                                                                        0000700 0001752 0001001 00000000704 14351222073 013205  0                                                                                                    ustar   mabalder                        UsersGrp                                                                                                                                                                                                               # !/bin/bash
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
                                                            12_nestedIfs.sh                                                                                     0000700 0001752 0001001 00000001004 14351222633 013717  0                                                                                                    ustar   mabalder                        UsersGrp                                                                                                                                                                                                               # !/bin/bash
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
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            13_conditionalExpressions.sh                                                                        0000700 0001752 0001001 00000001603 14353133674 016557  0                                                                                                    ustar   mabalder                        UsersGrp                                                                                                                                                                                                               # !/bin/bash
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
                                                                                                                             14_case.sh                                                                                          0000700 0001752 0001001 00000000530 14353134652 012720  0                                                                                                    ustar   mabalder                        UsersGrp                                                                                                                                                                                                               # !/bin/bash
# Script to show how to work with case
# Author: Manuel Balderrabano

option=""

echo "Example case instance"
read  -p "Write one option from A - Z:" option
echo -e "\n"

case $option in
	"A") echo -e "\nSave option";;
	"B") echo "Delete option";;
	[C-E]) echo "There is no option implemented";;
	*) echo "Incorrect option";;
esac
                                                                                                                                                                        15_arrays.sh                                                                                        0000755 0001752 0001001 00000001514 14353214202 013312  0                                                                                                    ustar   mabalder                        UsersGrp                                                                                                                                                                                                               # !/bin/bash
#Script to show how to work with arrays
#Author: Manuel Balderrabano 

numbersArray=(1 2 3 4 5 6)
stringsArray=(Marco, Antonio, Pedro, Susana)
rangesArray=({A..Z} {10..20})

#Print all values
echo "Numbers array: ${numbersArray[*]}"
echo "Strings array: ${stringsArray[*]}"
echo "Ranges array: ${rangesArray[*]}"

#Print arrays sizes 
echo "Numbers array size: ${#numbersArray[*]}"
echo "Strings array size: ${#stringsArray[*]}"
echo "Ranges array size: ${#rangesArray[*]}"

#Print position 3 from arrays 
echo "Position 3, Numbers array: ${numbersArray[3]}"
echo "Position 3, strings array: ${stringsArray[3]}"
echo "Position 3, ranges array: ${rangesArray[3]}"

#Add and delete values from and array
numbersArray[7]=20
unset numbersArray[0]
echo "Numbers array: ${numbersArray[*]}"
echo "Numbers array size: ${#numbersArray[*]}"
                                                                                                                                                                                    16_forloop.sh                                                                                       0000755 0001752 0001001 00000001102 14353217405 013473  0                                                                                                    ustar   mabalder                        UsersGrp                                                                                                                                                                                                               # !/bin/bash
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
                                                                                                                                                                                                                                                                                                                                                                                                                                                              17_whileloop.sh                                                                                     0000755 0001752 0001001 00000000272 14353217675 014036  0                                                                                                    ustar   mabalder                        UsersGrp                                                                                                                                                                                                               # !/bin/bash
#Script to show how to work with while loop
#Author: Manuel Balderrabano 

number=1

while [ $number -ne 10 ]
do 
	echo "Print $number times"
	number=$(( number + 1 ))
done
                                                                                                                                                                                                                                                                                                                                      18_nestedLoops.sh                                                                                   0000755 0001752 0001001 00000000307 14361652057 014327  0                                                                                                    ustar   mabalder                        UsersGrp                                                                                                                                                                                                               # !/bin/bash
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
                                                                                                                                                                                                                                                                                                                         19_breakContinue.sh                                                                                 0000700 0001752 0001001 00000000504 14375303553 014606  0                                                                                                    ustar   mabalder                        UsersGrp                                                                                                                                                                                                               # !/bin/bash
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
                                                                                                                                                                                            20_optionsMenu.sh                                                                                   0000755 0001752 0001001 00000001604 14375301404 014332  0                                                                                                    ustar   mabalder                        UsersGrp                                                                                                                                                                                                               #! /bin/bash
#Program to help postgress management.
#Author: Manuel Balderrabano

option=0

while :
do
	#Clear screen
	clear
	#Diplay options menu
	echo "___________________________________"
	echo "_______Postgress Management________"
	echo "___________________________________"
	echo "___________Main screen_____________"
	echo "___________________________________"
	echo "1. Install Postgress"
	echo "2. Uninstall Postgress"
	echo "3. Create Backup"
	echo "4. Restore Backup"
	echo "5. Exit"

	#Read user data
	read -n1 -p "Insert an option [1-5]:" option

	#Validate entered option
	case $option in
		1)
		echo -e "\nInstall postgress.........."
		sleep 3
		;;
		2)
		echo -e "\nUninstall postgress.........."
		sleep 3
		;;
		3)
		echo -e "\nCreate Backup.........."
		sleep 3
		;;
		4)
		echo -e "\nRestore Backup.........."
		sleep 3
		;;
		5)
		echo "Exit .........."
		exit 0
		;;
	esac
done
                                                                                                                            21_filesAndDirectories.sh                                                                           0000700 0001752 0001001 00000000520 14375302313 015717  0                                                                                                    ustar   mabalder                        UsersGrp                                                                                                                                                                                                               # !/bin/bash
#Script to show how to work with files and directories.
#Author: Manuel Balderrabano 

echo "Files - Directories"

if [ $1 = "d" ] ; then
	mkdir -m 755 $2
	echo "Directory created succesfully"
	ls -la $2
elif [ $1 = "f" ] ; then
	touch $2
	echo "File created succesfully"
	ls -la $2
else
	echo "There is no option: $1"
fi

                                                                                                                                                                                22_writeFile.sh                                                                                     0000700 0001752 0001001 00000000274 14375303313 013737  0                                                                                                    ustar   mabalder                        UsersGrp                                                                                                                                                                                                               # !/bin/bash
#Script to show how to write on  a file.
#Author: Manuel Balderrabano 

echo "Write on a file"

echo "Values writen with echo" >> $1

#Adding multiline
cat <<EOM >> $1
$2
EOM
                                                                                                                                                                                                                                                                                                                                    23_readFile.sh                                                                                      0000700 0001752 0001001 00000000515 14375561244 013530  0                                                                                                    ustar   mabalder                        UsersGrp                                                                                                                                                                                                               # !/bin/bash
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
                                                                                                                                                                                   24_filesOperations.sh                                                                               0000700 0001752 0001001 00000000531 14375561716 015166  0                                                                                                    ustar   mabalder                        UsersGrp                                                                                                                                                                                                               # !/bin/bash
#Script to show how file operations.
#Author: Manuel Balderrabano 

echo "File Operations"
mkdir -m 755 backupScripts

echo -e "\nCopy files into a new directory"
cp *.* backupScripts/
ls -la backupScripts/

echo -e "\nMove backupScriptfile to another location: $HOME"
mv backupScripts $HOME

echo -e "\nDelete files .txt"
rm *.txt
                                                                                                                                                                       25_tar.sh                                                                                           0000700 0001752 0001001 00000000242 14375562766 012614  0                                                                                                    ustar   mabalder                        UsersGrp                                                                                                                                                                                                               # !/bin/bash
#Script to show how package a file with tar.
#Author: Manuel Balderrabano 

echo "Pack all scripts from course folder"
tar -cvf shellCourse.tar *.sh
                                                                                                                                                                                                                                                                                                                                                              26_gzip.sh                                                                                          0000700 0001752 0001001 00000000446 14375563267 013003  0                                                                                                    ustar   mabalder                        UsersGrp                                                                                                                                                                                                               # !/bin/bash
#Script to show how package a file with gzip.
#Author: Manuel Balderrabano 

echo "Pack all scripts from course folder"
tar -cvf shellCourse.tar *.sh

#When you use gzip the las package is deleted
gzip shellCourse.tar

echo "Pack single file, with a 9 ratio"
gzip -9 9_options.sh

                                                                                                                                                                                                                          27_pbzip2.sh                                                                                        0000700 0001752 0001001 00000000426 14375563572 013236  0                                                                                                    ustar   mabalder                        UsersGrp                                                                                                                                                                                                               # !/bin/bash
#Script to show how package a file with pbzip2
#Author: Manuel Balderrabano 

echo "Pack all scripts from course folder"
tar -cvf shellCourse.tar *.sh
pbzip2 -f shellCourse.tar

echo -e "\nPack a folder with tar and pbzip2"
tar -cf *.sh -c > shellCourseDos.tar.bz2
                                                                                                                                                                                                                                          3_tipoOperadores.sh                                                                                 0000700 0001752 0001001 00000001636 14351135357 014733  0                                                                                                    ustar   mabalder                        UsersGrp                                                                                                                                                                                                               # ! /bin/bash
#Operators types
#Author: Manuel Balderrabano

numA=10
numB=4

echo "Aritmethic operators"
echo "Numbers: A=$numA and B=$numB"
echo "Add A + B =" $((numA + numB))
echo "Substract A - B =" $((numA - numB))
echo "Multiply A * B =" $((numA * numB))
echo "Divide A / B =" $((numA / numB))
echo "Residue A % B =" $((numA % numB))


echo  -e "\nRelational operators"
echo "Numbers: A=$numA and B=$numB"
echo "A > B =" $((numA > numB))
echo "A < B =" $((numA < numB))
echo "A >= B =" $((numA >= numB))
echo "A >= B =" $((numA >= numB))
echo "A == B =" $((numA == numB))
echo "A != B =" $((numA != numB))


echo  -e "\n Assignation Operators"
echo "Numbers: A=$numA and B=$numB"
echo "Add A += B =" $((numA += numB))
echo "Substract A -= B =" $((numA -= numB))
echo "Multiply A *= B =" $((numA *= numB))
echo "Divide A /= B =" $((numA /= numB))
echo "Residue A %= B =" $((numA %= numB))
                                                                                                  4_arguments.sh                                                                                      0000700 0001752 0001001 00000000347 14351135357 013740  0                                                                                                    ustar   mabalder                        UsersGrp                                                                                                                                                                                                               # ! /bin/bash
# Script to exemply Arguments use

courseName=$1
courseHour=$2

echo "Course Name is $courseName that is taught at $courseHour"
echo "The number of sended parameters are: $#"
echo "Sended parameters are: $*"
                                                                                                                                                                                                                                                                                         5_substituteCommand.sh                                                                              0000700 0001752 0001001 00000000415 14351202505 015430  0                                                                                                    ustar   mabalder                        UsersGrp                                                                                                                                                                                                               # ! /bin/bash
# Program to review how to execute commands and save the results in a variable for a later execution.
# Author: Manuel Balderrabano
location=`pwd`
infoKernel=$(uname -a)

echo "The current location is: $location"
echo "Kernel information is: $infoKernel"
                                                                                                                                                                                                                                                   6_readEcho.sh                                                                                       0000700 0001752 0001001 00000000510 14351202512 013423  0                                                                                                    ustar   mabalder                        UsersGrp                                                                                                                                                                                                               # ! /bin/bash
# Program to show how to capture user information using echo and read.
# Author: Manuel Balderrabano


option=0
backupName=""


echo "Postgres Utilities program"
echo -n "Enter and option:"
read
option=$REPLY
echo -n "Enter backup file name:"
read
backupName=$REPLY
echo "Option: $option. backupName: $backupName"
                                                                                                                                                                                        7_read.sh                                                                                           0000700 0001752 0001001 00000000447 14351202700 012635  0                                                                                                    ustar   mabalder                        UsersGrp                                                                                                                                                                                                               # ! /bin/bash
# Program to show how to capture user information using read.
# Author: Manuel Balderrabano


option=0
backupName=""


echo "Postgres Utilities program"
read -p "Enter and option:" option
read -p "Enter backup file name:" backupName
echo "Option: $option. backupName: $backupName"
                                                                                                                                                                                                                         8_readValidate.sh                                                                                   0000700 0001752 0001001 00000000633 14351204301 014304  0                                                                                                    ustar   mabalder                        UsersGrp                                                                                                                                                                                                               # ! /bin/bash
# Program to show how to capture user information and validate it.
# Author: Manuel Balderrabano


option=0
backupName=""
key=""

echo "Postgres Utilities program"
#Acepts one character inputs
read -n1 -p "Enter and option:" option
echo -e "\n"
read -n10 -p "Enter backup file name:" backupName
echo -e "\n"
echo "Option: $option. backupName: $backupName"
read -s -p "Clave:" key
echo "Key: $key"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     