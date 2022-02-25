
/*  seleccionar_palabras: Char, Int -> Char**
    Seleccionar palabras recorre el archivo lemario y utilizando el algorito Reservoir Sampling
    Mas especificamente utilizo su version llamada Algorimo R de Alan Waterman
    este algorimo toma la cantidad de palabras pedidas de manera aleatoria y las ingresa en una lista dada
    Link del algoritmo: https://en.wikipedia.org/wiki/Reservoir_sampling */
char **seleccionar_palabras(char nombre[30],int cant_palabras);


/*  escribir_salida: Char**,Int,Int,Int
    escribir_salida dadas la lista de palabras escogida la dimension complejidad y la cantidad de palabras elegidas
    escribe el archivo estructura que sera utilizado por el programa de python para hacer la sopa de letras
    mientras libera la memoria pedida por la lista de palabras */
void escribir_salida(char **lista,int dim,int comp,int cantidad);