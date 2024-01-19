'use strict'

/*
Programa que pida dos numeros y que nos diga cual es el mayor, el menor y si son iguales.
Si los numeros no son numeros o si son menores a 0 pide que ingrese los numeros nuevamente
*/

var numero1 = parseInt (prompt("Introduce el primer numero",0));
var numero2 = parseInt (prompt("Introduce el segundo numero",0));

while (numero1 <= 0 || numero2 <= 0 || isNaN(numero1) || isNaN(numero2)){
    var numero1 = parseInt (prompt("Introduce el primer numero",0));
    var numero2 = parseInt (prompt("Introduce el segundo numero",0));
}

if (numero1 == numero2 ){
    console.log("Los numeros son iguales")
}
else if (numero1 > numero2){
    console.log("El numero mayor es:", numero1)
}
else if (numero1 < numero2) {
    console.log("El numero mayor es:", numero2)
}else{
    console.log("Introduce numeros correctos")
}

