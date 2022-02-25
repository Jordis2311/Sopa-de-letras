from src.Sopa_de_Letras import *

def test_crear_matriz():
        assert crear_matriz(3) == [[0,0,0],
                                   [0,0,0],
                                   [0,0,0],]

def test_posible_AR_AB():
        matriz0 =[[0,0,0],
                  [0,0,0],
                  [0,0,0]]

        matriz1 =[[0,0,0],
                  ["a",'s',0],
                  ["h",'h',0]]
        
        assert posible_AR_AB(matriz0,'wah',3,0,0,0) == True
        assert posible_AR_AB(matriz0,'wah',3,0,0,2) == True
        assert posible_AR_AB(matriz0,'waha',3,0,0,0) == False
        assert posible_AR_AB(matriz0,'wah',3,3,1,1) == False
        assert posible_AR_AB(matriz1,'wah',3,3,0,0) == True
        assert posible_AR_AB(matriz1,'wah',3,2,0,0) == False
        assert posible_AR_AB(matriz1,'wah',3,3,0,1) == False


def test_posible_I_D():
        matriz0 =[[0,0,0],
                  [0,0,0],
                  [0,0,0]] 

        matriz1 =[[0,'a','h'],
                  [0,'s','h'],
                  [0,0,0]]
        
        assert posible_I_D(matriz0,'wah',3,0,0,0) == True
        assert posible_I_D(matriz0,'wah',3,0,2,0) == True
        assert posible_I_D(matriz0,'waha',3,0,2,0) == False
        assert posible_I_D(matriz0,'wah',3,3,1,1) == False
        assert posible_I_D(matriz1,'wah',3,3,0,0) == True
        assert posible_I_D(matriz1,'wah',3,2,0,0) == False
        assert posible_I_D(matriz1,'wah',3,3,0,1) == False

def test_posible_DSI_DID():
        matriz0 =[[0,0,0],
                  [0,0,0],
                  [0,0,0]] 

        matriz1 =[[0,0,0],
                  [0,'a',0],
                  [0,0,'h']]
        matriz2 =[[0,0,0],
                  [0,'s',0],
                  [0,0,'h']]
        assert posible_DSI_DID(matriz0,'wah',3,1,0,0) == True
        assert posible_DSI_DID(matriz0,'waha',3,1,0,0) == False
        assert posible_DSI_DID(matriz0,'wah',3,0,0,0) == False
        assert posible_DSI_DID(matriz0,'wah',3,1,1,1) == False
        assert posible_DSI_DID(matriz1,'wah',3,3,0,0) == True
        assert posible_DSI_DID(matriz1,'wah',3,2,0,0) == False
        assert posible_DSI_DID(matriz2,'wah',3,3,0,0) == False

def test_posible_AB_AR():
        matriz0 =[[0,0,0],
                  [0,0,0],
                  [0,0,0]] 

        matriz1 =[['h','h',0],
                  ['a','s',0],
                  [0,0,0]]

        assert posible_AB_AR(matriz0,'wah',2,2,2) == True
        assert posible_AB_AR(matriz0,'waha',2,2,2) == False
        assert posible_AB_AR(matriz0,'wah',2,2,0) == True
        assert posible_AB_AR(matriz0,'wah',1,2,2) == False
        assert posible_AB_AR(matriz0,'wah',2,1,1) == False
        assert posible_AB_AR(matriz1,'wah',3,2,0) == True
        assert posible_AB_AR(matriz1,'wah',2,2,0) == False
        assert posible_AB_AR(matriz1,'wah',3,2,1) == False

def test_posible_D_I():
        matriz0 =[[0,0,0],
                  [0,0,0],
                  [0,0,0]] 
        matriz1 =[['h','a',0],
                  ['h','s',0],
                  [0,0,0]]
        assert posible_D_I(matriz0,'wah',2,2,2) == True
        assert posible_D_I(matriz0,'waha',2,2,2) == False
        assert posible_D_I(matriz0,'wah',2,0,2) == True
        assert posible_D_I(matriz0,'wah',2,1,1) == False
        assert posible_D_I(matriz1,'wah',3,0,2) == True
        assert posible_D_I(matriz1,'wah',2,0,2) == False
        assert posible_D_I(matriz1,'wah',3,1,2) == False

def test_posible_DII_DSD():
        matriz0 =[[0,0,0],
                  [0,0,0],
                  [0,0,0]] 

        matriz1 =[[0,0,'h'],
                  [0,'a',0],
                  [0,0,0]]
        
        matriz2 =[[0,0,'h'],
                  [0,'s',0],
                  [0,0,0]]
                
        assert posible_DII_DSD(matriz0,'wah',3,2,2,0) == True
        assert posible_DII_DSD(matriz0,'wah',3,1,2,0) == False
        assert posible_DII_DSD(matriz0,'wah',3,3,0,2) == False
        assert posible_DII_DSD(matriz0,'waha',3,2,2,0) == False
        assert posible_DII_DSD(matriz1,'wah',3,2,2,0) == False
        assert posible_DII_DSD(matriz1,'wah',3,3,2,0) == True
        assert posible_DII_DSD(matriz2,'wah',3,3,2,0) == False

def test_posible_DID_DSI():
        matriz0 =[[0,0,0],
                  [0,0,0],
                  [0,0,0]] 

        matriz1 =[['h',0,0],
                  [0,'a',0],
                  [0,0,0]]
        matriz2 =[['h',0,0],
                  [0,'s',0],
                  [0,0,0]]

        assert posible_DID_DSI(matriz0,'wah',2,2,2) == True
        assert posible_DID_DSI(matriz0,'wah',1,2,2) == False
        assert posible_DID_DSI(matriz0,'wah',2,1,1) == False
        assert posible_DID_DSI(matriz0,'waha',2,2,2) == False
        assert posible_DID_DSI(matriz1,'wah',3,2,2) == True
        assert posible_DID_DSI(matriz1,'wah',2,2,2) == False
        assert posible_DID_DSI(matriz2,'wah',3,2,2) == False     

def test_posible_DSD_DII():
        matriz0 =[[0,0,0],
                  [0,0,0],
                  [0,0,0]] 

        matriz1 =[[0,0,0],
                  [0,'a',0],
                  ['h',0,0]]

        matriz2 =[[0,0,0],
                  [0,'s',0],
                  ['h',0,0]]
        
        assert posible_DSD_DII(matriz0,'wah',3,2,0,2) == True
        assert posible_DSD_DII(matriz0,'wah',3,1,0,2) == False
        assert posible_DSD_DII(matriz0,'wah',3,2,1,1) == False
        assert posible_DSD_DII(matriz0,'waha',3,2,0,2) == False
        assert posible_DSD_DII(matriz1,'wah',3,3,0,2) == True
        assert posible_DSD_DII(matriz1,'wah',3,2,0,2) == False
        assert posible_DSD_DII(matriz2,'wah',3,3,0,2) == False

def test_donde_es_posible():
        matriz0 =[[0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0]]   
        matriz1 =[[0,0,'x','a'],
                  [0,'a','a',0],
                  ['h','a',0,0],
                  ['a',0,0,0]]


        assert donde_es_posible(matriz0,'waha',4,3,0,0) == [0,1,2]
        assert donde_es_posible(matriz0,'wah',4,3,3,3) == [3,4,6]
        assert donde_es_posible(matriz0,'wa',4,0,1,1) == [0,1]
        assert donde_es_posible(matriz0,'wa',4,3,1,1) == [0,1,2,3,4,5,6,7]
        assert donde_es_posible(matriz1,'wah',4,3,2,2) == [4,6]
        assert donde_es_posible(matriz1,'wah',4,1,2,2) == []
        assert donde_es_posible(matriz1,'waha',4,3,0,0) == [0,2]

def test_escribir_palabra():

        matriz =[[0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0]]
        matriz0 =[[0,'w',0,0],
                  [0,'a',0,0],
                  [0,'h',0,0],
                  [0,0,0,0]]
        assert escribir_palabra(matriz,'wah',0,0,1) == matriz0

        matriz =[[0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0]]
        matriz1 =[[0,'w','a','h'],
                  [0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0]]
        assert escribir_palabra(matriz,'wah',1,0,1) == matriz1

        matriz =[[0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0]]
        matriz2 =[[0,'w',0,0],
                  [0,0,'a',0],
                  [0,0,0,'h'],
                  [0,0,0,0]]
        assert escribir_palabra(matriz,'wah',2,0,1) == matriz2

        matriz =[[0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0]]
        matriz3 =[[0,'h',0,0],
                  [0,'a',0,0],
                  [0,'w',0,0],
                  [0,0,0,0]]
        assert escribir_palabra(matriz,'wah',3,2,1) == matriz3

        matriz =[[0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0]]
        matriz4 =[[0,0,0,0],
                  [0,'h','a','w'],
                  [0,0,0,0],
                  [0,0,0,0]]
        assert escribir_palabra(matriz,'wah',4,1,3) == matriz4

        matriz =[[0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0]]
        matriz5 =[[0,0,0,'h'],
                  [0,0,'a',0],
                  [0,'w',0,0],
                  [0,0,0,0]]
        assert escribir_palabra(matriz,'wah',5,2,1) == matriz5

        matriz =[[0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0]]
        matriz6 =[[0,0,0,0],
                  [0,'h',0,0],
                  [0,0,'a',0],
                  [0,0,0,'w']]
        assert escribir_palabra(matriz,'wah',6,3,3) == matriz6

        matriz =[[0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0]]
        matriz7 =[[0,0,'w',0],
                  [0,'a',0,0],
                  ['h',0,0,0],
                  [0,0,0,0]]
        assert escribir_palabra(matriz,'wah',7,0,2) == matriz7


def test_agregar_palabra():
        matriz =[['w',0,'a',0],
                  ['a',0,'m',0],
                  ['s','e','h','o'],
                  ['s','m','n',0]]
        
        matriz1 = [['w',0,'a',0],
                  ['a','a','m',0],
                  ['s','e','h','o'],
                  ['s','m','n','a']]

        assert agregar_palabra(matriz,'waha',4,3) == matriz1
        assert agregar_palabra(matriz,'sex',4,3) == []

def test_palabra_en_casilla():
        matriz = [['w','a','h','l'],
                  ['a','a','h','o'],
                  ['h','a','h','q'],
                  ['w','a','h','s']]
        matriz1 =[['h','a','s','s'],
                  ['w','h','w','h'],
                  ['a','a','a','a'],
                  ['h','h','a','w'],]

        assert palabra_en_casilla(matriz,'wah',4,0,0) == 3
        assert palabra_en_casilla(matriz,'wah',4,3,0) == 2
        assert palabra_en_casilla(matriz,'wah',4,1,2) == 0
        assert palabra_en_casilla(matriz1,'wah',4,3,3) == 3
        assert palabra_en_casilla(matriz1,'wah',4,1,2) == 1

def test_palabra_en_matriz():
        matriz =[['w','a','h','s'],
                 ['m','a','n','h'],
                 ['a','p','h','a'],
                 ['s','u','s','w'],]
        assert palabra_en_matriz(matriz,'wah') == 3
        assert palabra_en_matriz(matriz,'man') == 1
        assert palabra_en_matriz(matriz,'spn') == 1
        assert palabra_en_matriz(matriz,'wha') == 1 
        assert palabra_en_matriz(matriz,'ayuda') == 0
        assert palabra_en_matriz(matriz,'uwu') == 0

def test_cantidad_palabras_correctas():
        matriz =[['w','a','h','s'],
                 ['m','a','n','h'],
                 ['a','p','h','a'],
                 ['s','u','s','w'],]
        assert cantidad_palabras_correctas(matriz,['spn','wah','man']) == False
        assert cantidad_palabras_correctas(matriz,['spn','wha','man']) == True
        assert cantidad_palabras_correctas(matriz,['spn','wha','man','awa']) == False