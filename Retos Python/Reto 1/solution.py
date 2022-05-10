"""
NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, 
El equipo de desarrollo de este calificador modificó las funciones 'print' e 'input'.
Esta modificación se hizo con la finalidad de que el sistema pueda calificar tu solución.
Por eso LEER MUY BIEN LO QUE SE SOLICITA Y LAS RESTRICCIONES QUE SE LE IMPUSIERON A ESTAS DOS FUNCIONES.
"""
from student_utilities import input, print


def solucion():
    #ACÁ INICIA LA FUNCIÓN SOLUCIÓN (En este espacio debes entregar tu solución)
    masP = "S"
    subtotal = 0

    while masP == "S":

        v_uni = int(input("Ingrese el valor unitario: "))
        iva = input("¿El producto cuenta con IVA? (S/N): ")
        qty = int(input("Ingrese la cantidad que lleva el cliente del producto a registrar: "))
        if iva == "S":
            print("IVA incluído")
            subtotal = subtotal + 1.19*v_uni*qty
        else:
            print("PRODUCTO SIN IVA")
            subtotal = subtotal + v_uni*qty

        print(f"SUBTOTAL: {subtotal}")
        x = input("¿Faltan productos por cobrar? S/N: ")
        if x=="N":
            masP = "N"
            print(f"TOTAL A COBRAR: {subtotal}")
    
       
#ACÁ TERMINA LA FUNCIÓN SOLUCIÓN
    
"""
¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE!
NO AÑADIR CÓDIGO FUERA DE LA FUNCIÓN solucion().
SOLO AÑADIR CÓDIGO ENTRE EL ESPACIO DONDE DICE: ACÁ INICIA... ACÁ TERMINA
"""
