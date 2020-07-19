##########################################################  Librerias
from flask import Flask, escape, request, jsonify

### Librerias para sistema de seguridad Basic auth
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

### Libreria para permitir funcionamiento CORS
from flask_cors import CORS, cross_origin

###Libreria personalizada para resulocion de problemas
from api_function import generar_datos_carreras, generar_ponderaciones_postulante, ordenar, generar_info_carreras
##########################################################  Definiciones del servicio
app = Flask(__name__)
app.config["DEBUG"] = True ###Activacion del Debugger
CORS(app) ###Permite activar sistema CORS en todas las rutas de la API
auth = HTTPBasicAuth() ###Funcion para activar sistema de seguridad mediante basic auth

###Usuarios predeterminados (Cambiar en produccion, o cambiar seccion por datos en BB.DD.)
users = {
    "Tester": generate_password_hash("betaman"),
    "APP": generate_password_hash("RDR-331")
}

@auth.verify_password ###Funcion para corroborar nombre de usuario y clave ingresados para consumo de api
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


##########################################################  Servicios Incorporados
@app.route('/', methods=['GET', 'POST']) ###Servicio por defecto: Confirma que se esta pudiendo consumir el servicio
@auth.login_required ###Decorador para forzar la utilizacion de autentificacion en el servicio
def say_hi():
    return "Hi, {}!. The API it's working".format(auth.current_user())

@app.route('/topten', methods=['POST']) ###Servicio POST 10mejores: Mediante los puntajes de un postulante, entrega un JSON con las 10 mejores carreras para el
@auth.login_required
def generar_top():
    if(request.method=='POST'):
        ##############################################  Variables
        nem=request.form.get('nem')
        ranking=request.form.get('ranking')
        matematicas=request.form.get('matematicas')
        lenguaje=request.form.get('lenguajes')
        ciencias=request.form.get('ciencias')
        historia=request.form.get('historia')

        if(matematicas==None or nem==None or ranking==None or lenguaje==None or ciencias==None or historia==None):
            return "Datos enviados incorrectamente, corrobore las etiquetas de los datos", 400

        try:
            nem = float(nem)
            ranking = float(ranking)
            matematicas = float(matematicas)
            lenguaje = float(lenguaje)
            ciencias = float(ciencias)
            historia = float(historia)
        except:
            return "Daton enviados invalidos, los valores recibidos deben ser numericos unicamente", 400
        var=matematicas+lenguaje
        var=var/2
        if(var<450):
            return "El postulante no puede postular a ninguna carrera, debido a que promedia entre lenguaje y matematicas menos de 450 puntos", 400
        carreras=generar_datos_carreras() ###Generacion de lista con los datos relevantes de cada carrera
        mis_carreras=[]
        ##############################################  Calculo de las ponderaciones del estudiante
        if(ciencias>=historia):
            ponderaciones_postulante=generar_ponderaciones_postulante(nem, ranking, matematicas, lenguaje, ciencias) ###Generacion ponderaciones para todas las carreras, con ciencias mayor que historia
        else:
            ponderaciones_postulante=generar_ponderaciones_postulante(nem, ranking, matematicas, lenguaje, historia) ###Generacion ponderaciones para todas las carreras, con historia mayor que ciencias

        ##############################################  Calculo de la posicion para cada carreras
        for posicion in range(0,28):
            contador=-1
            base=carreras[posicion]
            mi_numero=ponderaciones_postulante[posicion]
            if(mi_numero>=base[2]): ###Caso de estudiante que NO quedarian en lista de espera
                while(True):
                    if(mi_numero>base[2]):
                        contador+=1
                        base[2]+=base[3]
                    else:
                        mis_carreras.append([posicion+1, base[4]-contador, mi_numero])
                        break
            else:
                contador=0
                while(True): ###Estudiantes que quedarian en lista de espera
                    if(mi_numero<base[2]):
                        base[2]-=base[3]
                        contador-=1
                    else:
                        mis_carreras.append([posicion+1, contador, mi_numero])
                        break
        ##############################################  Ordenamiento de datos y creacion del Json final a retornar
        mis_carreras=ordenar(mis_carreras) ###Organiza posiciones del estudiante, priorizando valores positivos y el menor de ellos
        Jsons=[]
        for iteracion in range(0,10):
            datos=mis_carreras[iteracion]
            datos_carrera_particular=carreras[datos[0]-1]
            if(datos[1]>=0): ###Escenario en que el estudiante NO quedo en lista de espera
                json_especifico={
                    "Codigo":datos_carrera_particular[1],
                    "Nombre":datos_carrera_particular[0],
                    "Ponderacion":datos[2],
                    "Posicion":datos[1]
                }
                Jsons.append(json_especifico)
            else: ###Escenario en que el estudiante queda en lista de espera
                json_especifico={
                    "Codigo": datos_carrera_particular[1],
                    "Nombre": datos_carrera_particular[0],
                    "Ponderacion": datos[2],
                    "Posicion": "Lista de Espera: "+str(datos[1]*(-1))
                }
                Jsons.append(json_especifico)
        ### Retorno del JSON final
        return jsonify(Jsons), 200

@app.route('/carrer/', methods=['GET']) ###Servicio el cual, para un codigo en particular, entrega la informacion de la respectiva carrera (solo acepta 1 codigo)
@auth.login_required
def datos_carrera():
    if(request.method=='GET'):
        args = request.args
        if(len(args)!=1): ###Corrobora que sea solo UN codigo el recibido, si no cumple, manda un error
            return "La cantidad de carreras enviadas es diferente a las aceptadas por este sistema", 400
        else:
            try: ###Corrobora la existencia de una variable 'codigo'; de no existir, manda excepcion
                cod_recibido=args['codigo']
            except:
                return "Nombre de variable recibido invalido (el nombre debe se 'codigo')", 400

            try: ###Corrobora si el codigo es numerico, si no lo es, manda error (los codigos de la UTEM son unicamente numericos)
                cod_recibido=int(args['codigo'])
            except:
                return "El codigo a corroborar es invalido para este sistema (codigos solo numericos)", 400
            
            carreras=generar_info_carreras() ###Se genera un listado con todos los datos de todas las carreras
            for iteracion in range(0,29): ###Se realiza un ciclo iterativo para revisar si existe una carrera con el respectivo codigo
                if (iteracion == 28): ### En caso de no encajar con ningun codigo de carrera, se retorna una excepcion
                    return "El codigo ingresado no concuerda con el codigo de ninguna carrera", 400
                if(cod_recibido==carreras[iteracion][0]): ###Si existe una carrera con ese codigo, retorna su informacion
                    return {
                        "Codigo":carreras[iteracion][0],
                        "Nombre":carreras[iteracion][1],
                        "Nem": carreras[iteracion][2],
                        "Ranking": carreras[iteracion][3],
                        "Lenguaje": carreras[iteracion][4],
                        "Matematicas": carreras[iteracion][5],
                        "Ciencias sociales o Historia": carreras[iteracion][6],
                        "Pun. prom. min. entre Leng. y Mat.": carreras[iteracion][7],
                        "Pun. Min. de postulacion": carreras[iteracion][8],
                        "Vacantes": carreras[iteracion][9],
                        "Primer matriculado": carreras[iteracion][10],
                        "Ultimo matriculado": carreras[iteracion][11]
                    }, 200

@app.route('/carrers/', methods=['GET']) ###Servicio el cual, para un codigo en particular, entrega la informacion de la respectiva carrera (acepta n codigo)
@auth.login_required
def datos_carreras():
    if(request.method=='GET'):
        args = request.args
        if(len(args)==0): ###Se corrobora la existencia de almenos una variable
            return "La cantidad de carreras enviadas es diferente a las aceptadas por este sistema", 400
        elif(len(args)==1):
            palabra=''
            try:
                palabra=str(args['texto_1'])
            except:
                return "La frase recibida esta mal etiquetada; el nombre de la variable debe ser 'texto_1'", 400
            palabra=palabra.upper()
            if(len(palabra)<=3):
                return "La palabra a revisar debe tener un largo minimo de 4 letras"
            carreras=generar_info_carreras()
            respuestas=[]
            for carrera in carreras:
                if(carrera[1].upper().find(palabra)>=0 and carrera[1].upper().count(palabra)==1):
                    respuestas.append({
                        "Codigo":carrera[0],
                        "Nombre":carrera[1]
                    })
            if(len(respuestas)==0):
                return "No se encontro ninguna carrera que concordace", 400
            else:
                return jsonify(respuestas), 200
        else:
            palabras=[]
            for i in range(0,len(args)): ###Se realiza un ciclo iterativo, en el cual almacena todas las variables nombradas 'codigo_n', donde n es menor/igual a la cantidad de variables recibidas
                try:
                    palabras.append(str(args["texto_"+str(i+1)]))
                except:
                    pass
            copia_palabras=[]
            if(len(palabras)==0): ###En caso de que no se detecte ninguna variable con un nombre valido, se retorna una escepcion
                return "La cantidad de carreras recibidas validas es insuficiente para el funcionamiento del sistema", 400
            else:
                for palabra in palabras:
                    if(len(palabra)<=3):
                        pass
                    else:
                        copia_palabras.append(palabra.upper())
            if(len(copia_palabras)==0):
                return "La cantidad de palabras recibidas es insuficientes", 400
            else:
                palabras=copia_palabras
            carreras=generar_info_carreras() ###Se crea lista con todos los datos de todas las carreras
            datos_carreras_seleccionadas=[]
            codigos=[]
            contador=0
            for palabra in palabras:
                contador=0
                for carrera in carreras:
                    if(carrera[1].upper().find(palabra)>=0 and carrera[0] not in codigos):
                        codigos.append(carrera[0])
                        datos_carreras_seleccionadas.append({
                            "Codigo": carreras[contador][0],
                            "Nombre": carreras[contador][1]
                        })
                    contador+=1
            if(len(datos_carreras_seleccionadas)==0): ###En caso de que ningun codigo concuerde con alguna carrera, se retorna excepcion
                return "Ninguno de los codigos de careras es valido", 400
            else:
                return jsonify(datos_carreras_seleccionadas), 200

app.run() ###Activacion del servicio