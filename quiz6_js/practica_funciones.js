//PUNTO N° 1: Prácticar funciones.

//Primer ejercicio: funciones que realizan cálculos simples............................
const sumar = (a,b)=> a+b;
console.log("El resultado de la suma es: " + sumar(2,2));

const resta = (a,b)=> a-b;
console.log("El resultado de la resta es: " + resta(2,1));

const multiplicando = (a,b)=> a*b;
console.log("El resultado de la multiplicación es: " + multiplicando(4,4));

//Segundo ejercicio: funciones que manipulan cadena de texto y arrays.....................
function convertirEnMayuscula(cadena){
const convierteMayus = cadena.toUpperCase();
return convierteMayus;
}
  
console.log(convertirEnMayuscula("mariposa"));
  
  function eliminarUltimaLetra(){
    const palabraMayus = convertirEnMayuscula("mariposa");
    const palabraSinUltimaLetra = palabraMayus.split("");
    palabraSinUltimaLetra.pop();
    return palabraSinUltimaLetra.join("");
  }
  
  const resultado = eliminarUltimaLetra();
  console.log(resultado);