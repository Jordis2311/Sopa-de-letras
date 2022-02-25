#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <string.h>
#include "funciones.h"

char **seleccionar_palabras(char nombre[30],int cant_palabras)
{
    int i,n,j,MAX = 255;
    char buffer[MAX];
    FILE *lemario;
    char **lista;
    //Comprobamos que el lemario esta escrito correctamente
    lemario = fopen(nombre,"r+");
    if(lemario == NULL){
        perror("No se encontro el lemario");
        exit(EXIT_FAILURE);
    }

    lista = malloc(cant_palabras*sizeof(char *));

    //Primero se completa la lista con la cantidad de palabras que necesitamos
    for(n = 1;n < cant_palabras ;n++){
        fgets(buffer,MAX,lemario);
        if(buffer == NULL){
            exit(EXIT_FAILURE);
        }
        lista[n-1] = strdup(buffer);
    }
    //Luego se reemplazan los elementos gradualmente reduciendo la probabilidad
    for(i=n+1;fgets(buffer,MAX,lemario);i++){
        j = rand() % i;
            if(j < cant_palabras){
                free(lista[j]);
                lista[j] = strdup(buffer);
            }
    }
    // De esta manera todos los objetos de la lista tienen una probabilidad de cant_palabras/cantidad_lemario
    fclose(lemario);
    return lista;
}

void escribir_salida(char **lista,int dim,int comp,int cantidad){
    int i;
    FILE *estructura = fopen("estructura.txt","w+");
    fprintf(estructura,"DIMENSION\n");
    fprintf(estructura,"%i\n",dim);
    fprintf(estructura,"PALABRAS\n");
    for(i = 0;i<cantidad;i++){
        fputs(lista[i],estructura);
        free(lista[i]);
    }
    free(lista);
    fprintf(estructura,"COMPLEJIDAD\n");
    fprintf(estructura,"%i",comp);
    fclose(estructura);
}
