# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 20:43:43 2022

@author: aero7
"""
pensum = [{'0123':{'créditos':2, 'nombre':'intro a la ing'},
          '4567':{'créditos':1, 'nombre':'intro a la ing'}},
          {},
          {}]

# POR FAVOR LEA TODAS LAS INDICACIONES SUMINISTRADAS EN EL 
# ENUNCIADO ANTES DE EMPEZAR A IMPLEMENTAR SU SOLUCIÓN

def es_semestre_valido(p, s):
    # ESTA VEZ TU DEFINES TUS RETORNOS
    # Pensum / Semestre
    # Semestre empieza en 1, y la ista en 0
    s_qty = len(p)
    #s-=1                                         
    if s <= 0 or s > s_qty:                                
        isTrue = False
    else:
        isTrue = True
    return isTrue 
    
def es_semestre_vacio(p, s):
    # ESTA VEZ TU DEFINES TUS RETORNOS
    s-=1
    isEmpty = True if p[s]=={} else False
    return isEmpty
    
def es_materia_valida(p, s, m):
    # ESTA VEZ TU DEFINES TUS RETORNOS
    courseOK = False
    materias = p[s]
    for d in materias:
        course = materias[d]['nombre']
        if course!=" ":            
            courseOK = True
            break          
    return courseOK
    
def modificar_materia(pensum, semestre, materia, nombre, creditos):
    # ACÁ INICIA LA FUNCIÓN
    p = pensum
    s = semestre 
    m = materia 
    n = nombre 
    c = creditos
    #msg =''
    s-=1
    
    
    if es_semestre_valido(p, s):
        if not es_semestre_vacio(p, s):
            if es_materia_valida(p, s, m):
                p[s][m]['nombre'] = n
                p[s][m]['créditos'] = c
                msg = True
            
    
    
    # ACÁ TERMINA LA FUNCIÓN
    # ESTA VEZ TU DEFINES TUS RETORNOS

def eliminar_materia(pensum, semestre, materia):
    # ACÁ INICIA LA FUNCIÓN
    p = pensum
    s = semestre 
    m = materia 
    s-=1
    
    if es_semestre_valido(p, s):
        if not es_semestre_vacio(p, s):
            if es_materia_valida(p, s, m):
                x = p[s]
                x.pop(m)
                
                msg = True
           
    
    # ACÁ TERMINA LA FUNCIÓN
    # ESTA VEZ TU DEFINES TUS RETORNOS
