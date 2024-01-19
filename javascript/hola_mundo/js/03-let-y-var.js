'use strict'

//prueba con let y var

//Prueba con var
var numero = 40;
console.log(numero);

if(true){
    var numero = 50;
    console.log(numero); // valor 50
}

console.log(numero); // valor 50

//Prueba con let
var texto = "Curso JS";
console.log(texto); //valor js

if(true){
    let texto = "Curso JS con variable let";
    console.log(texto);
}
console.log(texto); //valor js
