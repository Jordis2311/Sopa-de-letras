import sys
import random

#Alumno Jordi Solá
#DNI 43492078

#----------------------------
#Sopa de letras
#Nuestra Sopa de letras toma como entrada el archivo de salida de la parte de C
#y nos retornara un archivo conteniendo una sopa de letras que tenga de caracteristas los datos incluidos en el archivo
#----------------------------

#----------------------------
#Representacion de Datos
#----------------------------
#Representamos a nuestra sopa como una matriz bidimensional de tamaño N x N
#siendo N la dimension especificada por nuestro archivo estructura 
#Mientras que las posiciones estaran representadas como tuplas (Int,Int)
#donde las celdas vacias estaran representadas por 0 por conveniencia
#por lo que Matrix = List(List(Any))
#----------------------------

#----------------------------
#Inicio del programa
#----------------------------

def main():

    #Comprueba que el archivo se ha ingresado correctamente
    validar_estructura()
    estructura = sys.argv[1]

    #Obtiene todos los datos necesarios del archivo
    datos = obtenerDatos(estructura)

    dimension = datos[0]
    palabras = datos[1]
    complejidad = datos[2]

    Sopa = intentar_sopa(dimension,palabras,complejidad)
    
    if(Sopa == []):
        print("Lo sentimos, no hemos logrado crear una sopa en la que quepan todas estas palabras")
    else:
        mostrar_sopa(Sopa)

#----------------------------
#Excepciones
#----------------------------

# Error al pasar una cantidad de parametros diferente de la esperada.
class ErrorParametros(Exception):
    def __init__(self, message="Error en el archivo <estructura>"):
        self.message = message
        super().__init__(self.message)

#Excepcion en el tamaño de las palabras de el archivo estructura, aparece cuando una de las palabras no entra en la sopa o es solamente una letra
class ErrorPalabra(Exception):
    def __init__(self, message="Una de las palabras del lemario no es valida para la sopa"):
        self.message = message
        super().__init__(self.message)

#Comprueba que se el programa se ha ejecutado correctamente
def validar_estructura():
    if len(sys.argv) != 2:
        raise ErrorParametros

#----------------------------
#Funciones
#----------------------------

#obtenerDatos: FILE -> (Int,List(String),Int)
#obtenerDatos toma el archivo estructura y devuelve en una tupla La dimension, las palabras, y la complejidad de la sopa de letras
#En caso de que haya errores en el archivo estructura, obtenerDatos termina el programa inmediatamente
def obtenerDatos(estructura):
    #Abrimos el archivo en mode lectura y guardamos su contenido en una lista de strings
    archivo = open(estructura, "r+")

    datos = archivo.readlines()

    #Si la primera linea del archivo estructra no es DIMENSION significa que no es el archivo correcto
    if(datos[0] != 'DIMENSION\n'):
        raise ErrorParametros

    #Como sabemos, la segunda linea del archivo contiene la dimension que tendra nuestra sopa de letras
    dimension = int(datos[1])

    #Desde la 4ta linea del archivo, se encuentran las palabras que iran dentro de la sopa
    #por lo que las guardamos en una lista hasta encontrar la linea COMPLEJIDAD\n que indica el final de la lista
    palabras = []
    i = 3
    while(datos[i] != 'COMPLEJIDAD\n'):
        if(len(datos[i][0:-1]) > dimension or len(datos[i][0:-1]) <= 1):
            raise ErrorPalabra
        palabras += [datos[i][0:-1]] #le saco el \n
        i+=1

    #Finalmente guardamos la complejidad de la sopa y cerramos el archivo
    complejidad = int(datos[i+1])

    archivo.close() 

    return (dimension,palabras,complejidad)

#crear_matriz: Int -> List(List(Int))
#crear_matriz toma un entero N que sera la dimension de nuestra sopa y crea una matriz bidimensional N x N
#en donde cada celda vacia estara representada por un 0
def crear_matriz(N):
    matrix = []
    for i in range(N):
        matrix.append([])
        for j in range(N):
            matrix[i].append(" ")
            matrix[i][j] = 0
    return matrix

#intentar_sopa: Int,List(String),Int -> Matrix
#intenar_sopa: dada la dimension, la lista de palabras y la complejidad
#Da inicio a la creacion de la sopa y la empieza desde cero en caso de se haya trabado en una palabra
#Si crear_sopa retorna una lista vacia entonces la sopa se iniciara devuelta
def intentar_sopa(dimension,palabras,complejidad):
    intentos = 0
    Sopa = []
    while(Sopa == [] and intentos < 1000):
        Sopa = crear_sopa(dimension,palabras,complejidad)
        intentos+=1
    return Sopa

#crear_sopa: Int, List(String), Int -> Matrix
#crear_sopa toma la dimension la complejidad y una lista de palabras y
#insertar las palabras en la sopa, si una palabra no se ha podido ingresar retorna una lista vacia
#para representar este fallo
#Finalmente si todas las palabras han sido insertadas en la sopa, rellena las casillas vacias y devuelve el resultado final
def crear_sopa(DIM,PAL,COMP):
    matriz = crear_matriz(DIM)
    i = 0
    while(i < len(PAL) and matriz != []):
        matriz = agregar_palabra(matriz,PAL[i],DIM,COMP)
        i+=1
    if(matriz != []):
        matriz = llenar_sopa(matriz)
        if(cantidad_palabras_correctas(matriz,PAL) == False):
            matriz = []
    return matriz

#agregar_palabra: Matrix,String,Int,Int -> Matrix
#agregar_palabra toma la matriz, la palabra, la dimension y la complejidad de la sopa e
#intenta buscar posiciones de manera aleatoria para insertar la palabra en la sopa
#de no lograrlo devuelve una lista vacia para indicarlo
def agregar_palabra(matriz,palabra,dimension,complejidad):
    direcciones = []
    intentos = 0
    posiciones = crear_lista_posiciones(dimension)
    random.shuffle(posiciones)
    while(direcciones == [] and intentos < len(posiciones)):
        i = posiciones[intentos][0]
        j = posiciones[intentos][1]
        intentos+=1
        if(matriz[i][j] == 0 or matriz[i][j] == palabra[0]):
            direcciones = donde_es_posible(matriz,palabra,dimension,complejidad,i,j)
 
    if(direcciones != []):
        direccion = random.choice(direcciones)
        #print(palabra,i,j,direccion)
        matriz = escribir_palabra(matriz,palabra,direccion,i,j)
    else:
        return []
        
    return matriz

#crear_lista_posiciones: Int -> Matrix
#crear_lista_posiciones Crea una lista de tuplas que representan las posiciones de la sopa de tamaño N x N
def crear_lista_posiciones(N):
    posiciones = []
    for i in range(N):
        for j in range(N):
            posiciones += [(i,j)]
    return posiciones

#escribir_palabra: Matrix, String,Int, Int, Int
#escribir_palabra dada la matriz, la palabra la direccion y la posicion
#inserta la palabra en la sopa de letras
def escribir_palabra(matriz,palabra,direccion,i,j):
    if(direccion == 0):
        for m in range(len(palabra)):
            matriz[i+m][j] = palabra[m]
    elif(direccion == 1):
        for m in range(len(palabra)):
            matriz[i][j+m] = palabra[m]
    elif(direccion == 2):
        for m in range(len(palabra)):
            matriz[i+m][j+m] = palabra[m]
    elif(direccion == 3):
        for m in range(len(palabra)):
            matriz[i-m][j] = palabra[m]
    elif(direccion == 4):
        for m in range(len(palabra)):
            matriz[i][j-m] = palabra[m]
    elif(direccion == 5):
        for m in range(len(palabra)):
            matriz[i-m][j+m] = palabra[m]
    elif(direccion == 6):
        for m in range(len(palabra)):
            matriz[i-m][j-m] = palabra[m]
    elif(direccion == 7):
        for m in range(len(palabra)):
            matriz[i+m][j-m] = palabra[m]
    return matriz

# posible_AR_AB: Matrix, String, Int, Int, Int, Int -> Boolean
# posible_AR_AB Dados la matriz, la palabra, la dimension, la complejidad y la posicion i , j
# Comprueba si es posible colocar la palabra en la posicion i j de la matriz de arriba hacia abajo
def posible_AR_AB(matriz,palabra,dimension,complejidad,i,j):
    longitud = len(palabra)
    posible = True
    if((i + longitud) <= dimension):
        m = 0
        while(m < longitud and posible):        
            if(matriz[i+m][j] != 0):                                    # Si la casilla es 0 significa que esta vacia por lo que se puede colocar la palabra ahi
                if(complejidad == 3 and matriz[i+m][j] == palabra[m]):  # si la casilla NO es vacia pero la letra que la ocupa coincide con la letra correspondiente 
                    posible = True                                      # a la palabra y la complejidad es 3 entonces Devuelve verdadero
                else: posible = False
            m+=1
    else: 
        posible = False
    return posible

# posible_I_D: Matrix, String, Int, Int, Int, Int -> Boolean
# posible_I_D Dados la matriz, la palabra, la dimension, la complejidad y la posicion i , j
# Comprueba si es posible colocar la palabra en la posicion i j de la matriz de Izquieda a Derecha
def posible_I_D(matriz,palabra,dimension,complejidad,i,j):
    longitud = len(palabra)
    posible = True
    if((j + longitud) <= dimension):
        m = 0
        while(m < longitud and posible):
            if(matriz[i][j+m] != 0):           
                if(complejidad == 3 and matriz[i][j+m] == palabra[m]):
                    posible = True
                else: posible = False
            m+=1
    else: 
        posible = False
    return posible

# posible_DSI_DID: Matrix, String, Int, Int, Int, Int -> Boolean
# posible_DSI_DID Dados la matriz, la palabra, la dimension, la complejidad y la posicion i , j
# Comprueba si es posible colocar la palabra en la posicion i j de la matriz en direccion Diagonal superior Izquierda a Diagonal Inferior Derecha
def posible_DSI_DID(matriz,palabra,dimension,complejidad,i,j):
    longitud = len(palabra)
    posible = True
    if(complejidad >= 1 and (i + longitud) <= dimension and (j + longitud) <= dimension):
        m = 0
        while(m < longitud and posible):
            if(matriz[i+m][j+m] != 0):            
                if(complejidad == 3 and matriz[i+m][j+m] == palabra[m]):
                    posible = True
                else: posible = False
            m+=1
    else: 
        posible = False
    return posible

# posible_AB_AR: Matrix, String, Int, Int, Int -> Boolean
# posible_AB_AR Dados la matriz, la palabra, la complejidad y la posicion i , j
# Comprueba si es posible colocar la palabra en la posicion i j de la matriz en direccion de Abajo Hacia Arriba
def posible_AB_AR(matriz,palabra,complejidad,i,j):
    longitud = len(palabra)
    posible = True
    if(complejidad >= 2 and (i - longitud + 1) >= 0):
        m = 0
        while(m < longitud and posible):
            if(matriz[i-m][j] != 0):            
                if(complejidad == 3 and matriz[i-m][j] == palabra[m]):
                    posible = True
                else: posible = False
            m+=1
    else: 
        posible = False
    return posible

# posible_D_I: Matrix, String, Int, Int, Int -> Boolean
# posible_D_I Dados la matriz, la palabra, la complejidad y la posicion i , j
# Comprueba si es posible colocar la palabra en la posicion i j de la matriz en direccion de Derecha a Izquierda
def posible_D_I(matriz,palabra,complejidad,i,j):
    longitud = len(palabra)
    posible = True
    if(complejidad >= 2 and (j + 1 - longitud) >= 0):
        m = 0
        while(m < longitud and posible):
            if(matriz[i][j-m] != 0):            
                if(complejidad == 3 and matriz[i][j-m] == palabra[m]):
                    posible = True
                else: posible = False
            m+=1
    else: 
        posible = False
    return posible

# posible_DII_DSD: Matrix, String, Int, Int, Int, Int -> Boolean
# posible_DII_DSD Dados la matriz, la palabra, la dimension, la complejidad y la posicion i , j
# Comprueba si es posible colocar la palabra en la posicion i j de la matriz en direccion de Diagonal Inferior Izquierda a Diagonal Superior Derecha
def posible_DII_DSD(matriz,palabra,dimension,complejidad,i,j):
    longitud = len(palabra)
    posible = True
    if(complejidad >= 2 and (i + 1 - longitud) >= 0 and (j + longitud) <= dimension) :
        m = 0
        while(m < longitud and posible):
            if(matriz[i-m][j+m] != 0):           
                if(complejidad == 3 and matriz[i-m][j+m] == palabra[m]):
                    posible = True
                else: posible = False
            m+=1
    else: 
        posible = False
    return posible

# posible_DID_DSI: Matrix, String, Int, Int, Int -> Boolean
# posible_DID_DSI Dados la matriz, la palabra, la complejidad y la posicion i , j
# Comprueba si es posible colocar la palabra en la posicion i j de la matriz en direccion de Diagonal Inferior Derecha a Diagonal Superior Izquierda
def posible_DID_DSI(matriz,palabra,complejidad,i,j):
    longitud = len(palabra)
    posible = True
    if(complejidad >= 2 and (i - longitud + 1) >= 0 and (j - longitud + 1) >= 0) :
        m = 0
        while(m < longitud and posible):
            if(matriz[i-m][j-m] != 0):          
                if(complejidad == 3 and matriz[i-m][j-m] == palabra[m]):
                    posible = True
                else: posible = False
            m+=1
    else: 
        posible = False
    return posible

# posible_DSD_DII: Matrix, String, Int, Int, Int, Int -> Boolean
# posible_DSD_DII Dados la matriz, la palabra, la dimension, la complejidad y la posicion i , j
# Comprueba si es posible colocar la palabra en la posicion i j de la matriz en direccion de Diagonal Superior Derecha a Diagonal Inferior Izquierda
def posible_DSD_DII(matriz,palabra,dimension,complejidad,i,j):
    longitud = len(palabra)
    posible = True
    if(complejidad >=2 and (i + longitud) <= dimension and (j - longitud + 1) >= 0):
        m = 0
        while(m < longitud and posible):
            if(matriz[i+m][j-m] != 0):
                if(complejidad == 3 and matriz[i+m][j-m] == palabra[m]):
                    posible = True
                else: posible = False
            m+=1
    else: 
        posible = False
    return posible

# donde_es_posible: Matrix, String, Int, Int, Int, Int -> List(Int)
# donde_es_posible Dadas la matriz, la palabra, la dimension, complejidad y una posicion
# devuelve una lista de las direcciones posibles en donde la palabra puede ser colocada en la matriz
# Direcciones posibles representadas por numeros
# 0: De arriba hacia abajo
# 1: De izquierda a derecha
# 2: De diagonal superior izquierda a diagonal inferior derecha
# 3: De abajo hacia arriba
# 4: De derecha a izquierda
# 5: De diagonal inferior izquierda a diagonal superior derecha
# 6: De diagonal inferior derecha a diagonal superior izquierda
# 7: de diagonal superior derecha a diagonal inferior izquierda
def donde_es_posible(matriz,palabra,dimension,complejidad,i,j):
    direcciones = []

    #Verificar si es posible de arriba hacia abajo 
    if(posible_AR_AB(matriz,palabra,dimension,complejidad,i,j)):
        direcciones += [0]

    #Verificar si es posible de izquierda a derecha
    if(posible_I_D(matriz,palabra,dimension,complejidad,i,j)):
        direcciones += [1]

    #Verifica si es posible en diagonal superior izquierda a diagonal inferior derecha
    if(posible_DSI_DID(matriz,palabra,dimension,complejidad,i,j)):
        direcciones += [2]

    #Verifica si es posible de abajo hacia arriba
    if(posible_AB_AR(matriz,palabra,complejidad,i,j)):
        direcciones += [3]

    #Verifica si es posible de derecha a izquierda
    if(posible_D_I(matriz,palabra,complejidad,i,j)):
        direcciones += [4]
    
    #Verifica si es posible de diagonal inferior izquierda a diagonal superior derecha
    if(posible_DII_DSD(matriz,palabra,dimension,complejidad,i,j)):
        direcciones += [5]  

    #Verifica si es posible de diagonal inferior derecha a diagonal superior izquierda
    if(posible_DID_DSI(matriz,palabra,complejidad,i,j)):
        direcciones += [6]
    
    #Verifica si es posible de diagonal superior derecha a diagonal inferior izquierda
    if(posible_DSD_DII(matriz,palabra,dimension,complejidad,i,j)):
        direcciones += [7]

    return direcciones

#llenar_sopa: Matrix -> Matrix
#llenar_sopa recorre la sopa para buscar casillas vacias e intercambiarlas por letras aleatorias
def llenar_sopa(matriz):
    alfabeto=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if(matriz[i][j] == 0):
                matriz[i][j] = random.choice(alfabeto)

    return matriz

#cantidad_palabras_correctas: Matrix, List(String) -> Boolean
#cantidad_palabras_correctas Verifica que cada palabra aparezca exactamente 1 vez
#Esto resuelve la consigna de que al completar los espacios vacios no se generen palabras iguales a las de la sopa
def cantidad_palabras_correctas(matriz,palabras):
    repeticion = True
    for palabra in palabras:
        if(palabra_en_matriz(matriz,palabra) != 1):
            repeticion = False
    return repeticion

#palabra_en_matriz: Matrix, String -> Int
#palabra_en_matriz cuenta la cantidad de veces que aparece una palabra dentro de una matriz
def palabra_en_matriz(matriz,palabra):
    dim = len(matriz)
    apariciones = 0
    for i in range(dim):
        for j in range(dim):
            apariciones += palabra_en_casilla(matriz,palabra,dim,i,j)
    return apariciones

#palabra_en_casilla: Matrix, String, Int, Int, Int -> Int
#palabra_en_casilla contabiliza si aparece la palabra empezando por la casilla (i,j) por cada direccion posible
def palabra_en_casilla(matriz,palabra,dimension,i,j):
    apariciones = 0
    longitud = len(palabra)
    #La letra de la casilla coincide con la letra de la palabra?
    if(matriz[i][j] == palabra[0]):
        #Aparece de arriba hacia abajo? (AR_AB)
        if((i + longitud) <= dimension):
            posible = True
            m = 1
            while(m < longitud and posible):
                if(palabra[m]!=matriz[i+m][j]):
                    posible = False
                m+=1
            if(posible): apariciones +=1
        #Aparece de izquieda a derecha? (I_D)
        if((j + longitud) <= dimension):
            posible = True
            m = 1
            while(m < longitud and posible):
                if(palabra[m]!=matriz[i][j+m]):
                    posible = False
                m+=1
            if(posible): apariciones +=1
        #Aparece de diagonal superior izquierda a diagonal inferior derecha? (DSI_DID)
        if((i + longitud) <= dimension and (j + longitud) <= dimension):
            posible = True
            m = 1
            while(m < longitud and posible):
                if(palabra[m]!=matriz[i+m][j+m]):
                    posible = False
                m+=1
            if(posible): apariciones +=1 
        #Aparece de Abajo hacia arriba? (AB_AR)
        if((i - longitud + 1) >= 0):
            posible = True
            m = 1
            while(m < longitud and posible):
                if(palabra[m]!=matriz[i-m][j]):
                    posible = False
                m+=1
            if(posible): apariciones +=1
        #Aparece de Derecha a izquierda? (D_I)
        if((j - longitud + 1) >= 0):
            posible = True
            m = 1
            while(m < longitud and posible):
                if(palabra[m]!=matriz[i][j-m]):
                    posible = False
                m+=1
            if(posible): apariciones +=1
        #Aparece de Diagonal Inferior Izquierda a Diagonal Superior Derecha (DII_DSD)
        if((i + 1 - longitud) >= 0 and (j + longitud) <= dimension):
            posible = True
            m = 1
            while(m < longitud and posible):
                if(palabra[m]!=matriz[i-m][j+m]):
                    posible = False
                m+=1
            if(posible): apariciones +=1
        #Aparece de Diagonal Inferior Derecha a Diagonal superior Izquierda? (DID_DSI)
        if((i - longitud + 1) >= 0 and (j - longitud + 1) >= 0):
            posible = True
            m = 1
            while(m < longitud and posible):
                if(palabra[m]!=matriz[i-m][j-m]):
                    posible = False
                m+=1
            if(posible): apariciones +=1
        #Aparece de Diagonal superior Derecha a Diagonal inferior Izquierda (DSD_DII)
        if((i + longitud) <= dimension and (j - longitud + 1) >= 0):
            posible = True
            m = 1
            while(m < longitud and posible):
                if(palabra[m]!=matriz[i-m][j-m]):
                    posible = False
                m+=1
            if(posible): apariciones +=1
        
    return apariciones

# mostrar_sopa: Matrix -> None
# Muestra la sopa de letras en pantalla
def mostrar_sopa(sopa):
    for linea in sopa:
        res = "".join(linea)
        print(res)

if __name__ == "__main__":
	main()



    
