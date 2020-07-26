"""
Apartado de Funciones:
En este espacio de codigo, se encuentran las funciones generadas para resolver los
problemas solicitados; para mas informacion, cada funcion esta documentada para su
mejor comprension
"""
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

def ordenar(listado): ###Funcion para el ordenamiento de mejores a peores posiciones de los postulantes
    positivos=[]
    negativos=[]
    for elemento in listado:
        if(elemento[1]>=0): ###Si su posicion es positivo, (que NO esta en lista de espera), los ordena de menor a mayor (mientras mas cerca a 1, mejor es la posicion)
            positivos.append(elemento)
        else: ###Si la posicion es negativa, (que esta en lista de espera), los ordena de mayor a menor (mientras mas cerca de 0, mejor posicion)
            negativos.append(elemento) 
    return ordenar_mayores(positivos)+ordenar_menores(negativos) ###Retorna las 2 sublista unidas como una sola, la cual esta ordenada de mejor a peor posicion
###################################################################

def generar_info_carreras(): ###Funcion que entrega una lista con todos los datos de todas las carreras UTEM 2019
    L=[
        [21089,"Administración Pública",15, 20, 30, 25, 10, 450, "No tiene", 35, 625.8, 513],
        [21002,"Bibliotecología y Documentación", 20, 20, 40, 10, 10, 450, "No tiene", 35, 675.3, 453.6],
        [21012,"Contador Público y Auditor", 20, 20, 30, 15, 15, 450, "No tiene", 80, 635.55, 452.2],
        [21048,"Ingeniería Comercial", 10, 20, 30, 30, 10, 450, "No tiene", 125, 652.9, 496.9],
        [21015,"Ingeniería en Administración Agroindustrial", 10, 20, 30, 30, 10, 450, "No tiene", 30, 628.8, 461.8],
        [21081,"Ingeniería en Comercio Internacional", 10, 20, 30, 30, 10, 450, "No tiene", 90, 637.2, 458.8],
        [21082,"Ingeniería en Gestión Turística", 10, 20, 30, 30, 10, 450, "No tiene", 25, 659.4, 448.1],
        [21047,"Arquitectura", 15, 25, 20, 20, 20, 450, "No tiene", 100, 640.2, 527.4],
        [21074,"Ingeniería Civil en Obras Civiles", 20, 20, 15, 35, 10, 450, "No tiene", 100, 625, 476.1],
        [21032,"Ingeniería en Construcción", 20, 20, 15, 35, 10, 450, "No tiene", 100, 716.3, 476.95],
        [21087,"Ingeniería Civil en Prevención de Riesgos y Medioambiente", 15, 35, 20, 20, 10, 450, "No tiene", 30, 615.2, 462.85],
        [21073,"Ingeniería en Biotecnología", 15, 25, 20, 30, 10, 450, "No tiene", 60, 675.8, 540.9],
        [21039,"Ingeniería en Industria Alimentaria", 15, 25, 20, 30, 10, 450, "No tiene", 30, 680.2, 464.9],
        [21080,"Ingeniería en Química", 10, 25, 15, 30, 20, 450, "No tiene", 80, 606.55, 451.7],
        [21083,"Química Industrial", 10, 25, 15, 30, 20, 450, "No tiene", 40, 596.05, 472],
        [21024,"Diseño en Comunicación Visual", 10, 40, 30, 10, 10, 450, "No tiene", 100, 706.3, 440.2],
        [21023,"Diseño Industrial", 10, 40, 30, 10, 10, 450, "No tiene", 65, 642.2, 439.9],
        [21043,"Trabajo Social", 20, 30, 20, 10, 20, 450, "No tiene", 95, 705.9, 510.5],
        [21046,"Bachillerato en Ciencias de la Ingeniería", 10, 25, 20, 35, 10, 450, "No tiene", 25, 586.45, 504.25],
        [21071,"Dibujante Proyectista", 10, 25, 20, 35, 10, 450, "No tiene", 25, 689.85, 496.45],
        [21041,"Ingeniería Civil en Computación, mención Informática", 10, 25, 20, 35, 10, 450, "No tiene", 130, 673.65, 539.35],
        [21076,"Ingeniería Civil Industrial", 10, 25, 20, 35, 10, 450, "No tiene", 200, 671.25, 500.85],
        [21049,"Ingeniería Civil en Ciencia de Datos", 10, 25, 20, 35, 10, 450, "No tiene", 60, 673.65, 539.35],
        [21075,"Ingeniería Civil Electrónica", 10, 25, 20, 35, 10, 450, "No tiene", 80, 657.35, 500.65],
        [21096,"Ingeniería Civil en Mecánica", 10, 25, 20, 35, 10, 450, "No tiene", 90, 697.65, 506.8],
        [21031,"Ingeniería en Geomensura", 10, 25, 20, 35, 10, 450, "No tiene", 60, 614.3, 487.85],
        [21030,"Ingeniería en Informática", 10, 25, 20, 35, 10, 450, "No tiene", 105, 705.15, 507.75],
        [21045,"Ingeniería Industrial", 10, 25, 20, 35, 10, 450, "No tiene", 60, 584.75, 476.25]
    ]
    return L
