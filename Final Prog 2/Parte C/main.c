#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <string.h>
#include "funciones.h"

/*Trabajo Final Programacion 2 Sopa de Letras
    Parte C
    Alumno Jordi Sola DNI 43492078

    Este programa toma como entrada el nombre del lemario a leer
    y las caracteristicas de una Sopa de letras tales como la Dimension, Cantidad de Palabras y Complejidad
    y retorna un archivo del nombre "estructura.txt" conteniendo estas caracteristicas para construir una sopa de letras

    Por la naturaleza de la lectura de archivos y aleatoriedad del programa no pude hacer tests de las funciones
    Sin embargo Intente explicar mediante comentarios y ejemplos como este deberia funcionar
    Con la entrada
    nombre_lemario.txt
    10
    8
    3

    Retornara el archivo

    estructura.txt
    que contiene

    DIMENSION
    10
    PALABRAS
    sofaldar
    paja
    nuevoleones
    estadistica
    tarraga
    adnato
    multiplica
    rodeador
    COMPLEJIDAD
    3

    (Las palabras no seran las mismas que en el ejemplo) UwU
*/

//Incializacion del programa
int main()
{   //declaramos las variables que necesitaremos y a su vez activamos la aleatoriedad
    int dimension, complejidad = -1,cantidad;
    char **lista = NULL;
    char nombre_lemario[30];
    srand(time(NULL));

    //Pedimos al usuario el nombre del lemario, la dimension que tendra la sopa, la cantidad de palabras que contendra y su complejidad
    printf("Ingrese direccion del lemario:");
    scanf("%s",&nombre_lemario);

    printf("Ingrese la cantidad de filas y columnas que tendra la sopa de letras:");
    scanf("%d",&dimension);

    printf("Ingrese la cantidad de palabras que estaran en la sopa:");
    scanf("%d",&cantidad);

    //si la complejidad no esta en el rango posible se la pedira de nuevo
    while(complejidad < 0 || complejidad > 3)
    {
        printf("Ingrese La complejidad de la sopa de letras (0->3):");
        scanf("%d",&complejidad);
        if(complejidad < 0 || complejidad > 3)
            printf("La complejidad elejida es invalida, porfavor intentelo de nuevo\n");
    }

    //Insertamos en la lista la cantidad de palabras que necesitamos
    lista = seleccionar_palabras(nombre_lemario,cantidad);

    //escribimos el archivo estructura
    escribir_salida(lista,dimension,complejidad,cantidad);

    printf("El archivo se ha escrito correctamente en salida.txt");

    return 0;
}
