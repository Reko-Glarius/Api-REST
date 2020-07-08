def generar_datos_carreras():
    nom_car=[]
    cod_car=[]
    alfa_car=[]
    omega_car=[]
    cant_car=[]
    L=[]
    for iteracion in range(0,28):
        puntos_per_posicion=((alfa_car[iteracion]-omega_car[iteracion])/cant_car[iteracion])
        aux=[nom_car[iteracion],cod_car[iteracion],omega_car[iteracion],puntos_per_posicion]
        L.append(aux)