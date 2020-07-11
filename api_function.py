def generar_datos_carreras(): ###Funcion para generar lista con todos los datos relevantes de todas las carreras
    ### Variables para datos de las carreras
    nom_car=["Administración Pública","Bibliotecología y Documentación","Contador Público y Auditor","Ingeniería Comercial","Ingeniería en Administración Agroindustrial",
             "Ingeniería en Comercio Internacional","Ingeniería en Gestión Turística","Arquitectura","Ingeniería Civil en Obras Civiles","Ingeniería en Construcción",
             "Ingeniería Civil en Prevención de Riesgos y Medioambiente","Ingeniería en Biotecnología","Ingeniería en Industria Alimentaria","Ingeniería en Química",
             "Química Industrial","Diseño en Comunicación Visual","Diseño Industrial","Trabajo Social","Bachillerato en Ciencias de la Ingeniería","Dibujante Proyectista",
             "Ingeniería Civil en Computación, mención Informática","Ingeniería Civil Industrial","Ingeniería Civil en Ciencia de Datos","Ingeniería Civil Electrónica",
             "Ingeniería Civil en Mecánica","Ingeniería en Geomensura", "Ingeniería en Informática", "Ingeniería Industrial"]
    
    cod_car=[21089,21002,21012,21048,21015,21081,21082,21047,21074,21032,21087,21073,21039,21080,
             21083,21024,21023,21043,21046,21071,21041,21076,21049,21075,21096,21031,21030,21045]
    
    alfa_car=[625.8,675.3,635.55,652.9,628.8,637.2,659.4,640.2,625,716.3,615.2,675.8,680.2,606.55,596.05
              ,706.3,642.2,705.9,586.45,689.85,673.65,671.25,673.65,657.35,697.65,614.3,705.15,584.75]
    
    omega_car=[513,453.6,452.2,496.9,461.8,458.8,448.1,527.4,476.1,476.95,462.85,540.9,464.9,451.7,
               472,440.2,439.9,510.5,504.25,496.45,539.35,500.85,539.35,500.65,506.8,487.85,507.75,476.25]
    
    cant_car=[35,35,80,125,30,90,25,100,100,100,30,60,30,80,40,100,65,95,25,25,130,200,60,80,90,60,105,60]
    
    L=[]
    for iteracion in range(0,28): ###Ciclo iterativo para juntar toda la informacion
        puntos_per_posicion=((alfa_car[iteracion]-omega_car[iteracion])/cant_car[iteracion])
        aux=[nom_car[iteracion],cod_car[iteracion],omega_car[iteracion],puntos_per_posicion,cant_car[iteracion]]
        L.append(aux)
    return L ###Retorno de la lista resultante

def generar_ponderaciones_postulante(nem, ranking, matematicas, lenguaje, ciencia_historia): ###Funcion para la generacion de lista con todas las ponderaciones posibles
    L=[]
    for i in range(0,28):
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
        elif(i==7): ###Caso para carrera 8
            ponderacion=float(nem*0.15+ranking*0.25+lenguaje*0.2+matematicas*0.2+ciencia_historia*0.2)
            L.append(ponderacion)
        elif(i>=8 and i<=9): ###Caso para carrera 9-10
            ponderacion=float(nem*0.2+ranking*0.2+lenguaje*0.15+matematicas*0.35+ciencia_historia*0.1)
            L.append(ponderacion)
        elif(i==10): ###Caso para carrera 11
            ponderacion=float(nem*0.15+ranking*0.35+lenguaje*0.2+matematicas*0.2+ciencia_historia*0.1)
            L.append(ponderacion)
        elif(i>=11 and i<=12): ###Caso para carrera 12-13
            ponderacion=float(nem*0.15+ranking*0.25+lenguaje*0.2+matematicas*0.3+ciencia_historia*0.1)
            L.append(ponderacion)
        elif(i>=13 and i<=14): ###Caso para carrera 14-15
            ponderacion=float(nem*0.1+ranking*0.25+lenguaje*0.15+matematicas*0.3+ciencia_historia*0.2)
            L.append(ponderacion)
        elif(i>=15 and i<=16): ###Caso para carrera 16-17
            ponderacion=float(nem*0.1+ranking*0.4+lenguaje*0.3+matematicas*0.1+ciencia_historia*0.1)
            L.append(ponderacion)
        elif(i==17): ###Caso para carrera 18
            ponderacion=float(nem*0.2+ranking*0.3+lenguaje*0.2+matematicas*0.1+ciencia_historia*0.2)
            L.append(ponderacion)
        elif(i>=18 and i<=27): ###Caso para carrera 19-28
            ponderacion=float(nem*0.1+ranking*0.25+lenguaje*0.2+matematicas*0.35+ciencia_historia*0.1)
            L.append(ponderacion)
    return L ###Retorno de la lista resultante


def ordenar_mayores(listado):  ###Funcion recursiva para ordenar de mayor a menor los valores de una lista
    izq = []
    cen = []
    der = []
    if (len(
            listado) <= 1):  ###Condicion de termino de la recursiva; cuando la cantidad de elementos de la lista a ordenar es 0 o 1, ya que no habria elementos a ordenar
        return listado
    else:  ###Escenario recursivo, cuando existen 2 o mas elementos, ya que es posible tener que ordenarlos
        pivote = listado[0][1]
        for elemento in listado:  ###Para cada elemento de la lista...
            if (elemento[1] > pivote):  ### ...Se corrobora si es mayor...
                der.append(elemento)
            elif (elemento[1] == pivote):  ### ...Igual...
                cen.append(elemento)
            else:  ### ...O menor al pivote
                izq.append(elemento)
    return ordenar(izq) + cen + ordenar(
        der)  ###Finalmente se retorna la aplicacion recursiva de los elementos mayores e inferiores al pivote


def ordenar_menores(listado):  ###Funcion recursiva para ordenar de mayor a menor los valores de una lista
    izq = []
    cen = []
    der = []
    if (len(
            listado) <= 1):  ###Condicion de termino de la recursiva; cuando la cantidad de elementos de la lista a ordenar es 0 o 1, ya que no habria elementos a ordenar
        return listado
    else:  ###Escenario recursivo, cuando existen 2 o mas elementos, ya que es posible tener que ordenarlos
        pivote = listado[0][1]
        for elemento in listado:  ###Para cada elemento de la lista...
            if (elemento[1] > pivote):  ### ...Se corrobora si es mayor...
                izq.append(elemento)
            elif (elemento[1] == pivote):  ### ...Igual...
                cen.append(elemento)
            else:  ### ...O menor al pivote
                der.append(elemento)
    return ordenar(izq) + cen + ordenar(
        der)  ###Finalmente se retorna la aplicacion recursiva de los elementos mayores e inferiores al pivote

def ordenar(listado):
    positivos=[]
    negativos=[]
    for elemento in listado:
        if(elemento[1]>=0):
            positivos.append(elemento)
        else:
            negativos.append(elemento)
    return ordenar_mayores(positivos)+ordenar_menores(negativos)