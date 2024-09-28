//PUNTO N° 3: Prácticar Estructuras de Control:
//Primer ejercicio: condicionales complejos........................................
let pregunta = prompt("¿Eres culpable?");
let respuesta1 = "si"
let respuesta2 = "no"
let otraRespuesta = "la documentación por favor"

if(pregunta==respuesta1) {
console.log("irás a la carcel")
} else if (pregunta == respuesta2) {
    console.log("¡irás a casa!")
} else {
    console.log("la documentación por favor")
}

// Segundo ejercicio: realizar un Switch............................................
let siHay = "Perfecto, ¡ya te lo traigo! :)";
const topping = prompt("Ingresa el topping de helado que deseas: ");

switch (topping.toLocaleLowerCase()) {
    case "oreo":
        siHay = "Perfecto, ¡te traigo el topping de Oreo!"; 
        break;
    case "frutos rojos":
        siHay = "Perfecto, ¡te traigo el topping de frutos rojos!";
        break;
    case "brownie":
        siHay = "Perfecto, ¡te traigo el topping de brownie!";
        break;
    case "fresa":
        siHay = "Perfecto, ¡te traigo el topping de fresa!";
        break;
    default:
        alert("No tenemos ese topping. Lo sentimos.");
        break;
}

alert(siHay);

// Tercer ejercicio usando el operador ternario............................................
let haceSol = true;
let mensaje = (haceSol)?"Hace un dia soleado":"No está nublado";
console.log(mensaje);

