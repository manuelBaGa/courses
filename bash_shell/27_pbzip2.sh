# !/bin/bash
#Script to show how package a file with pbzip2
#Author: Manuel Balderrabano 

echo "Pack all scripts from course folder"
tar -cvf shellCourse.tar *.sh
pbzip2 -f shellCourse.tar

echo -e "\nPack a folder with tar and pbzip2"
tar -cf *.sh -c > shellCourseDos.tar.bz2
