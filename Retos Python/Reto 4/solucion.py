# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 20:43:43 2022

@author: aero7
"""
pensum = [{'0123':{'créditos':2, 'nombre':'intro a la ing'},
          '4567':{'créditos':1, 'nombre':'intro a la ing'}},
          {},
          {}]

def es_semestre_valido(p, s):
    # Pensum / Semestre
    # Semestre empieza en 1, y la ista en 0
    s_qty = len(p)
    s-=1                                          # Logitud de la lista, igual a cantidad de semestres
    if s <= 0 or s > s_qty:                                 # Si el semestre es menor a 0 o mayor a la cantidad, retorna False
        isTrue = False
    else:
        isTrue = True
    return isTrue 

def es_semestre_vacio(p, s):
    isEmpty = True if p[s]=={} else False
    return isEmpty

def es_materia_valida(p, s, m):
    s-=1
    materias = p[s]
    for d in materias:
        course = materias[d]['nombre']
        if course==m:            
            courseOK = True
        else: 
            courseOK = False 
            break
    return courseOK
        
def modificar_materia(pensum , semestre, materia, nombre, creditos):
    p = pensum
    s = semestre 
    m = materia 
    n = nombre 
    c = creditos
    msg =''
    s-=1
    
    
    if es_semestre_valido(p, s):
        if not es_semestre_vacio(p, s):
            if es_materia_valida(p, s, m):
                p[s][m]['nombre'] = n
                p[s][m]['créditos'] = creditos
                msg = 'Course update done'
            else:
                msg = "Course don't exist"
        else:
            msg = 'Semester is empty'
    else: 
        msg: 'Semester is wrong'

def eliminar_materia(pensum, semestre, materia):
    

