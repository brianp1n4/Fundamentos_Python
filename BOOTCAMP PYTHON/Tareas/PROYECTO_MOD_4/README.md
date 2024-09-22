Esta es el proyecto entregable del modulo #4 del bootcamp Fundamentos de Python con Ucamp.
///////////////////////////////////////////////////////////////
En este proyecto se solicito realizar una Pokedex, haciendo uso de la API: https://pokeapi.co

En el codigo se importan distintas librerias para el desarrollo del programa
Se hace uso de las librerias:

-REQUESTS Para realizar peticiones a una API
-JSON Para trabajar con archivos json
-OS Para trabajar con directorios y archivos dentro del sistema operativos
-TKINTER Es una libreria que nos permite trabajar con interfaces graficas simples
-PILLOW Es una libreria nativa de python que permite trabajar con imagenes

El programa define varias funciones para su legibilidad y optimizacion

Pide al usuario el nombre de un pokemon mediante la presentacion de una interfaz, se incluye un boton de busqueda o en su defecto se ligo el evento de la tecla enter para realizar la busqueda. La busqueda hace una consulta por el metodo GET a la API que definimos
Se manejan excepeciones de acuerdo a los codigos de respuesta de la API para evitar errores.

Al obtener respuesta de la API se obtiene la informacion sobre sus movimientos y habilidades mediante una funcion que integra un ciclo for para recorrer el objeto que contiene
El resto de valores se almacenan en variables para su presentacion posterior y llamada en funciones consecuentes

Una vez con la informacion se genera un archivo JSON que es almacenado en una carpeta en el mismo nivel de donde se aloja el programa, en caso de no existir esta carpeta la crea bajo el nombre de "pokedex"

La presentacion al usuario con el uso de la librera TKINTER, muestra una ventana con los datos recabados asi como la imagen del pokemon consultado, en el JSON la imagen se incluye con la URL unicamente.

Se agrega un boton de LIMPIAR para realizar otra busqueda.
Para finalizar el programa basta con cerrar la ventana que se ejecuta.


///////////////////////////////////////////////////////////////

Este programa es la culminacion del bootcamp de fundamentos de python, el uso previo de librerias como NUMPY o MATPLOTLIB en proyectos pasados, desperto mi curiosidad en otro tipo de librerias que estan al alcance, de manera paralela me di a la tarea de revisar su funcionamiento y buscar otros ejercicios para poder ejecutarlos y llevarlos a este proyecto. Me siento como utilizando estructuras de control y funciones a un nivel intermedio, esto me facilita el entendimiento de otras librerias y su integracion. Me siento con un nivel intermedio en el lenguaje y continuare mi aprendizaje buscando ejercicios o proyectos similares para practicarlos.