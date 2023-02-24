# !/bin/bash
#Script to show how package a file with gzip.
#Author: Manuel Balderrabano 

echo "Pack all scripts from course folder"
tar -cvf shellCourse.tar *.sh

#When you use gzip the las package is deleted
gzip shellCourse.tar

echo "Pack single file, with a 9 ratio"
gzip -9 9_options.sh

