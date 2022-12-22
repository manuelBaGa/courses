# ! /bin/bash
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
