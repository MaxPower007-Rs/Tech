# POR FAVOR LEA TODAS LAS INDICACIONES SUMINISTRADAS EN EL 
# ENUNCIADO ANTES DE EMPEZAR A IMPLEMENTAR SU SOLUCIÓN

# NO MODIFICAR EL NOMBRE, PARÁMETROS O RETORNO DE LA FUNCIÓN
def modificar_materia(pensum, semestre, materia, nombre, creditos):
    # ACÁ INICIA LA FUNCIÓN modificar_materia (En este espacio debes 
    # poner el código necesario para implementar esta funcionalidad)
    # Constantes y variables
    
    len_pensum =len(pensum)    # Longitud de la lista para validar el semestre
    
    # Funciones
    def sem(s, l):          # S = semestre (str), l = len(pensum)
        if s <= 0 or s >l:            
            isTrue = False
        else:
            isTrue = True            
        return isTrue
    # Función 
    def mat(materia,keys):
        x = materia in keys
        if not x:            
            isTrue = False
        else:
            isTrue = True            
        return isTrue
    
    # Lógica
    # Validacion de semestre
    s = sem(semestre,len_pensum)
    
    
    if s:
        indice = semestre-1
        if pensum[indice]!= {}:
            keys = pensum[indice].keys()     # Extrae las llaves para verificar si existe la materia
            m = mat(materia, keys)            
            if m:             
                pensum[indice][materia]['nombre'] = nombre
                pensum[indice][materia]['créditos'] = creditos
                mensaje = 'Modificada con éxito'
            else:
                mensaje = 'La materia no existe'
        else:
            mensaje = 'El semestre no tiene materias'
        
    else:
        mensaje = 'Ingrese un semestre válido'
    
    
    # ACÁ TERMINA LA FUNCIÓN modificar_materia
    # NO MODIFIQUES LA SIGUIENTE LÍNEA
    return mensaje

