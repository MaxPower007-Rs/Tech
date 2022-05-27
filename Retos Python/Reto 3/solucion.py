# -*- coding: utf-8 -*-
"""
Created on Fri May 27 08:13:14 2022

@author: arodriguezs
"""

import numpy as np
import random

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
    # ACÁ INICIA LA FUNCIÓN
    x = np.zeros(shape=(15,5))  #Se crea una matriz de ceros
    m=x.astype(int)             #Todos los elementos se pasan a enteros
    
    Bx = 0
    Ix = 0
    Nx = 0
    Gx = 0
    Ox = 0
    r=0
    b_min = []
    
    
    balotas_revueltas = []
    # Se randomiza la lista de balotas
    for i in range(len(balotas)):
        rem = random.choice(balotas)        #Se selecciona aleatoriamente un elemento
        balotas_revueltas.append(rem)       #Se arma nueva lista con elemento seleccionado
        balotas.remove(rem)                 #Se quita elemento de la lista original, para no repetir
    
    """
    
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
        b_min.append(s)
            
        if (Bx>=5) and (Ix>=5) and (Gx>=5) and (Ox>=5) and (Nx>=4):
            r = balotas_revueltas.index(s)
            r+=1
            balotas_minimas = tuple(balotas_revueltas[0:r])
            break    
    
    
    return balotas_minimas, b_min,m,balotas_revueltas

f1,f2,m,g = balotera(cadena)


X =set(f1)
Y =set(f2)


