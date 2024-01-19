"use strict"

// Condicionales if
// So A es igual a B entonces haz algo

var edad1 = 30;
var edad2 = 12;

// Si pasa esto
if (edad1 > edad2) {
    //Ejecuta esto
    console.log("Edad 1 es mayor que edad 2")
}else{
    console.log("Edad 2 es mayor que edad 1")
}

var edad = 24;
var nombre = "David Suarez";

if (edad >= 18 ){
    console.log(nombre+" Es mayor de edad");

    if (edad <= 33){
        console.log("Todavia eres milenial");
    }
    else if(edad >= 70 ){
        console.log("Eres Anciano")
    }
    else{
        console.log("Ya no eres milenial");
    }
}
else{
    console.log(nombre+ " Es menor de edad");
}
 
/*
OPERADORES LOGICOS
AND: &&
OR: ||
NOT: !
*/

//negacion
var year = 2018;
if (year != 2016){
    console.log("El año no es 2016, es: "+ year)
}

//AND
if(year >= 2000 && year <= 2020 ){
    console.log("Estamos en la era actual");
}
else{
    console.log("Estamos en la era post moderna");
}

//OR 

if(year == 2008 || (year >= 2018 && year <= 2028)){
    console.log("El año acaba en 8");
}
else{
    console.log("Año no registrado")
}