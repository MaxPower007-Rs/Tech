#NO BORRAR LAS IMPORTACIONES QUE ENCUENTRAN A CONTINUACIÓN. LA FUNCIÓN QUE VA A 
#COMPLETAR NO REQUERIRÁ DE PARÁMETROS DE ENTRADA

#LOS MÓDULOS csv Y json ESTÁN ADJUNTOS POR DEFECTO EN LAS VERSIONES MÁS RECIENTES 
#DE PYTHON (3.x). ASEGÚRESE DE QUE LA VERSIÓN DE PYTHON EN LA QUE USTED HA ESTADO 
#EJECUTANDO SU PROPUESTA DE SOLUCIÓN CONTIENE DICHO MÓDULO

import csv
import json
def clima():
    
    #A PARTIR DE ACÁ PUEDE ADJUNTAR SU PROPUESTA DE SOLUCIÓN.REMÍTASE AL ENUNCIADO 
    #PARA MÁS DETALLES.
    
    #RECUERDE QUE SU PROPUESTA DEBE ACCEDER A UN ARCHIVO LLAMADO  "data.csv" 
    #(EL ARCHIVO ESTÁ EN ESTA PLATAFORMA), REALIZAR CÁLCULOS EN CADA FILA CON 
    #DOS DATOS ESPECÍFICOS Y LLEVAR LOS RESULTADOS A UN OBJETO JSON QUE CONTENDRÁ 
    #CINCO LISTAS DE DOS PROMEDIOS CADA UNA. ESTE ES EL OBJETO QUE DEBE RETORNAR.
    
    #SU SOLUCIÓN TAMBIÉN DEBE ESTAR EN CAPACIDAD DE CREAR UN ARCHIVO CSV
    #QUE DEBE LLAMARSE "data_nuevo.csv" A PARTIR DE "data.csv" CON LAS 
    #ESPECIFICACIONES INDICADAS EN EL ENUNCIADO
        #A PARTIR DE ACÁ PUEDE ADJUNTAR SU PROPUESTA DE SOLUCIÓN.REMÍTASE AL ENUNCIADO 
    #PARA MÁS DETALLES.
    
    #RECUERDE QUE SU PROPUESTA DEBE ACCEDER A UN ARCHIVO LLAMADO  "data.csv" 
    #(EL ARCHIVO ESTÁ EN ESTA PLATAFORMA), REALIZAR CÁLCULOS EN CADA FILA CON 
    #DOS DATOS ESPECÍFICOS Y LLEVAR LOS RESULTADOS A UN OBJETO JSON QUE CONTENDRÁ 
    #CINCO LISTAS DE DOS PROMEDIOS CADA UNA. ESTE ES EL OBJETO QUE DEBE RETORNAR.
    
    #SU SOLUCIÓN TAMBIÉN DEBE ESTAR EN CAPACIDAD DE CREAR UN ARCHIVO CSV
    #QUE DEBE LLAMARSE "data_nuevo.csv" A PARTIR DE "data.csv" CON LAS 
    #ESPECIFICACIONES INDICADAS EN EL ENUNCIADO
    
    # Definicio de funciones auxiliares
    def levels(dicc, k, t0,p0):
        t = dicc[k][0]
        p = dicc[k][1]
        if t0>t:
            msgT = 'SI'
        elif t0<t:
            msgT = 'NO'
        else:
            msgT = 'IGUAL'
            
        if p0>p:
            msgP = 'SI'
        elif p0<p:
            msgP = 'NO'
        else:
            msgP = 'IGUAL'
            
        return msgT,msgP
    
    # Inicializacion de variables usadas
    t1,t2,t3,t4,t5 = 0,0,0,0,0
    c1,c2,c3,c4,c5 = 0,0,0,0,0
    p1,p2,p3,p4,p5 = 0,0,0,0,0
    lista = []
    
    with open('data.csv', 'r') as csvfile:
        lector  = csv.reader(csvfile)       # Lectura del archivo csv
        #head    = next(lector)              # Eliminar encabezado
    
        # Extraccion de cada registro con un ciclo for
        for fila in lector:                   
            if fila[1]== '1':
                t1 += int(fila[2])
                p1 += int(fila[3])
                c1+=1 
                
            elif fila[1]== '2': 
                t2 += int(fila[2])
                p2 += int(fila[3])
                c2+=1
    
            elif fila[1]== '3':
                t3 += int(fila[2])
                p3 += int(fila[3])
                c3+=1
    
            elif fila[1]== '4':
                t4 += int(fila[2])
                p4 += int(fila[3])
                c4+=1
                
            elif fila[1]== '5':
                t5 += int(fila[2])
                p5 += int(fila[3])
                c5+=1
        
        # PROMEDIO TEMPERATURAS y formato con 1 decimal
        PT1 = float("{:.1f}".format(t1/c1))
        PT2 = float("{:.1f}".format(t2/c2))
        PT3 = float("{:.1f}".format(t3/c3))
        PT4 = float("{:.1f}".format(t4/c4))
        PT5 = float("{:.1f}".format(t5/c5))
        
       # PROMEDIO PRESIONES y formato con 1 decimal
        PP1 = float("{:.1f}".format(p1/c1))
        PP2 = float("{:.1f}".format(p2/c2)) 
        PP3 = float("{:.1f}".format(p3/c3)) 
        PP4 = float("{:.1f}".format(p4/c4)) 
        PP5 = float("{:.1f}".format(p5/c5))
    
        # Diccionario con promedios de temperatura y presion   
        dicc = {
            "1":[PT1, PP1],
            "2":[PT2, PP2],
            "3":[PT3, PP3],
            "4":[PT4, PP4], 
            "5":[PT5, PP5]
            }
    
    # LOGICA PARA INTEGRAR LA LISTA CON NUEVOS DATOS
    # Se adicionan dos columnas. Extaryendo el encabezado del archivo CSV    
    with open('data.csv', 'r') as csvfile2:
        lector2  = csv.reader(csvfile2)     # Lectura del archivo csv
        head2    = next(lector2)            # Extraccion de cabecera del archivo csv
        head2.append('above_avg_temp')      # Adicion de columna
        head2.append('above_avg_pres')      
        
        # Se crea la lista con nuevo encabezado
        for i in head2:
            lista.append(i)     # ['id', 'location', 'temperature', 'pressure', 'above_avg_temp', 'above_avg_pres']
            
        # Se crea lista nueva con nuevas columnas adicionales. Inicializadas en cero 
        listax =[]    
        for rows_ in lector2:       # Archivo temporal con datos de data.csv. f-->[1, 2, 34.5, 40.3] por cada fila
            f=rows_                 # Variable auxiliar
            t0 = float(f[2])        # Temperatura por zona. Zona = f[1]
            p0 = float(f[3])        # Presion por zona. Zona = f[1]
            
            if f[1]=='1':
                msgT,msgP = levels(dicc,f[1], t0, p0)       # Uso de fx auxiliar.  Comparacion de valores. Salida 'SI', 'NO' o 'IGUAL'
            if f[1]=='2':
                msgT,msgP = levels(dicc,f[1], t0, p0)            
            if f[1]=='3':
                msgT,msgP = levels(dicc,f[1], t0, p0)
            if f[1]=='4':
                msgT,msgP = levels(dicc,f[1], t0, p0)
            if f[1]=='5':
                msgT,msgP = levels(dicc,f[1], t0, p0)
                
            f.append(msgT)            # above_avg_temp - salida adicionada a columna nueva xa temperatura
            f.append(msgP)            # above_avg_pres - salida adicionada a columna nueva xa presion
            listax.append(f)          # ejemplo: ['1000', '1', '41', '31', 'SI', 'NO']
    
    # Integracion de listas para creacion de nuevo archivo CSV con tabla completa
    # Creacion del archivo nuevo y con la opcion 'a' de append, para nuevos datos.
    with open('data_nuevo.csv', 'a', newline='') as new_data:       # newline='', hace que tenga salto de linea unitario
        w = csv.writer(new_data)
        w.writerow(lista)                    # Se escribe el encabezado nuevo
        for i in listax:                     # listax, trae la tabla completa y se va agregando fila x fila al csv
            w.writerow(i)
        new_data.close()
        
    #  Creacion del objeto JSON con datos de diccionario       
    datos = json.dumps(dicc, indent=4) 
      
    return datos
