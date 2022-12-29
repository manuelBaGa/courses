# !/bin/bash
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
