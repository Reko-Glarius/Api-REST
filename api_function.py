def generar_datos_carreras(): ###Funcion para generar lista con todos los datos relevantes de todas las carreras
    ### Variables para datos de las carreras
    nom_car=[]
    cod_car=[]
    alfa_car=[]
    omega_car=[]
    cant_car=[]
    L=[]
    for iteracion in range(0,28): ###Ciclo iterativo para juntar toda la informacion
        puntos_per_posicion=((alfa_car[iteracion]-omega_car[iteracion])/cant_car[iteracion])
        aux=[nom_car[iteracion],cod_car[iteracion],omega_car[iteracion],puntos_per_posicion]
        L.append(aux)
    return L ###Retorno de la lista resultante

def generar_ponderaciones_postulante(nem, ranking, matematicas, lenguaje, ciencia_historia): ###Funcion para la generacion de lista con todas las ponderaciones posibles
    L=[]
    for iteracion in range(0,28):
        if(i==0): ###Caso para carrera 1
            ponderacion=float(nem*0.15+ranking*0.2+lenguaje*0.3+matematicas*0.25+ciencia_historia*0.1) ###Calculo valor ponderado
            L.append(ponderacion) ###Adicion valor ponderado a la lista
        elif(i==1): ###Caso para carrera 2
            ponderacion=float(nem*0.2+ranking*0.2+lenguaje*0.4+matematicas*0.1+ciencia_historia*0.1)
            L.append(ponderacion)
        elif(i==2): ###Caso para carrera 3
            ponderacion=float(nem*0.2+ranking*0.2+lenguaje*0.3+matematicas*0.15+ciencia_historia*0.15)
            L.append(ponderacion)
        elif(i>=3 and i<=6): ###Caso para carreras 4-7
            ponderacion=float(nem*0.1+ranking*0.2+lenguaje*0.3+matematicas*0.3+ciencia_historia*0.1)
            L.append(ponderacion)
        elif(i==1): ###Caso para carrera 8
            ponderacion=float(nem*0.15+ranking*0.25+lenguaje*0.2+matematicas*0.2+ciencia_historia*0.2)
            L.append(ponderacion)
        elif(i==1): ###Caso para carrera 9-10
            ponderacion=float(nem*0.2+ranking*0.2+lenguaje*0.15+matematicas*0.35+ciencia_historia*0.1)
            L.append(ponderacion)
        elif(i==1): ###Caso para carrera 11
            ponderacion=float(nem*0.15+ranking*0.35+lenguaje*0.2+matematicas*0.2+ciencia_historia*0.1)
            L.append(ponderacion)
        elif(i==1): ###Caso para carrera 12-13
            ponderacion=float(nem*0.15+ranking*0.25+lenguaje*0.2+matematicas*0.3+ciencia_historia*0.1)
            L.append(ponderacion)
        elif(i==1): ###Caso para carrera 14-15
            ponderacion=float(nem*0.1+ranking*0.25+lenguaje*0.15+matematicas*0.3+ciencia_historia*0.2)
            L.append(ponderacion)
        elif(i==1): ###Caso para carrera 16-17
            ponderacion=float(nem*0.1+ranking*0.4+lenguaje*0.3+matematicas*0.1+ciencia_historia*0.1)
            L.append(ponderacion)
        elif(i==1): ###Caso para carrera 18
            ponderacion=float(nem*0.2+ranking*0.3+lenguaje*0.2+matematicas*0.1+ciencia_historia*0.2)
            L.append(ponderacion)
        elif(i==1): ###Caso para carrera 19-28
            ponderacion=float(nem*0.1+ranking*0.25+lenguaje*0.2+matematicas*0.35+ciencia_historia*0.1)
            L.append(ponderacion)
    return L ###Retorno de la lista resultante

def ordenar(listado): ###Funcion recursiva para ordenar de mayor a menor los valores de una lista
    izq=[]
    cen=[]
    der=[]
    if(len(listado)<=1): ###Condicion de termino de la recursiva; cuando la cantidad de elementos de la lista a ordenar es 0 o 1, ya que no habria elementos a ordenar
        return listado
    else: ###Escenario recursivo, cuando existen 2 o mas elementos, ya que es posible tener que ordenarlos
        pivote=listado[0][1]
        for elemento in listado: ###Para cada elemento de la lista...
            if(elemento[1]>pivote):    ### ...Se corrobora si es mayor...
                izq.append(elemento)
            elif(elemento[1]==pivote): ### ...Igual...
                cen.append(elemento)
            else:                      ### ...O menor al pivote
                der.append(elemento)
    return ordenar(izq)+cen+ordenar(der) ###Finalmente se retorna la aplicacion recursiva de los elementos mayores e inferiores al pivote
    
