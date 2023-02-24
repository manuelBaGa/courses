# !/bin/bash
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
