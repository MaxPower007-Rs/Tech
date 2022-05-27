"""
Created on Fri May 27 08:13:14 2022

@author: arodriguezs
"""

import numpy as np
import random

"""
Codigo para generar el archivo balotas
"""
cadena=[]
c=0
l=list('BINGO')
acc = 0
for z in l:
    c=0
    for x in range(1,75):
        acc+=1
        y = z+str(acc)
        cadena.insert(0, y)
        c+=1
        if c==15:
            break

cadena.reverse()


def balotera(balotas):
    # INICIALIZACION DE VAIABLES
    x = np.zeros(shape=(15,5))  #Se crea una matriz de ceros
    m=x.astype(int)             #Todos los elementos se pasan a enteros
    balotas_revueltas = []      #Inicializacion de lista
    Bx = 0
    Ix = 0
    Nx = 0
    Gx = 0
    Ox = 0
    r=0
    
    
    """
    Se revuelven las balotas, considerando que deben ser unicas, no repetibles dentro de 
    la lista nueva.
    """
    
    # Se randomiza la lista de balotas
    for i in range(len(balotas)):           #Rango dinamico. Se extraen datos de la lista y se borran
        rem = random.choice(balotas)        #Se selecciona aleatoriamente un elemento
        balotas_revueltas.append(rem)       #Se arma nueva lista con elemento seleccionado
        balotas.remove(rem)                 #Se quita elemento de la lista original, para no repetirlo
    
    """
    Se itera la lista revuelta. Cada elemento es una cadena de caracteres, por ejemplo:
    ['G49',
     'O61',
     'G50',
     'B5',
     'I27',......
     ]
    
    Esta lista me dice en qué columna colocar el dato entero, así: 
    'G49'--> se ubica en la fila 0, columna 3
    
            B   I   N   G   O
    array([[ 5, 27, 45, 49, 61],
           [ 4, 28, 37, 50, 75],
           [11, 17, 40, 55, 67],
           [10, 29, 35, 52, 62],
           [12, 18,  0, 47, 74],
           [15, 22,  0, 60, 66],
           [ 0, 16,  0, 48, 68],
           [ 0,  0,  0, 58, 64],
           [ 0,  0,  0, 54,  0],
           [ 0,  0,  0,  0,  0],
           [ 0,  0,  0,  0,  0],......
           
     ....y cuando se llena ese espacio, se incrementa el indice para no sobreescribirlo.
     elif s[0]=='G':               
            m[Gx][3] = int(s[1::]) UBICACION DEL DATO, CONVERTIDO A ENTERO
            Gx+=1                  INCREMENTO DEL INDICE
    ... con el ciclo if, se evalua a que columna pertenece segun la letra inicial y
    el valor que va al lado de la letra se extrae usando slice:
    Ejemplo: s = 'G49', 
                        s[0]--> 'G'
                        s[1::]--> '49' (lo demás) 
                        con int se pasa a entero
    ... m, es la matrix de 15 filas y 5 columnas. Entonces para los numeros que van en B se usa:
        m[x][0], donde x es el valor del indice de la columna
        m[x][1], para los valores de la columna 'I' y asi sucesivamente
        .
        .
        .
    """
    for s in balotas_revueltas:         
        if s[0]=='B':        
            m[Bx][0] = int(s[1::])
            Bx+=1
        elif s[0]=='I':
            m[Ix][1] = int(s[1::])
            Ix+=1
        elif s[0]=='N':        
            m[Nx][2] = int(s[1::])
            Nx+=1
        elif s[0]=='G':
            m[Gx][3] = int(s[1::])
            Gx+=1
        else:
            m[Ox][4] = int(s[1::])
            Ox+=1
        
        if (Bx>=5) and (Ix>=5) and (Gx>=5) and (Ox>=5) and (Nx>=4):
             r = balotas_revueltas.index(s)
             r+=1
             balotas_minimas = tuple(balotas_revueltas[0:r])
             break         

    return balotas_minimas, m, balotas_revueltas
"""
    Esta parte evalua si la cantidad de datos ingresados a la matriz ya se completó
    Para cada letra, correspondiente a cada columna, son 5 datos, a excepcion de la columna de
    la letra 'N', que son 4. Si se cumple para todas las columnas, entonces quiere decir que es 
    una tabla ganadora y termina.
    
    Se crea la tupla con el dato del indice del ultimo item de la tabla, y se hace de nuevo un slice,
    pero no sin antes aumentar el indice en 1 para que incluya el ultimo dato analizado
"""
        


bm, m, br = balotera(cadena)
