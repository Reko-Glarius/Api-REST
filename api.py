"""
Nombre del proyecto: API REST ESTUDIANTIL
Equipo Desarrollador:
    -Ricardo Aliste G. (Desarrollador)
    -Daniel Cajas U. (Documentador)
    -Rodrigo Carmona R. (Documentador)
Resumen del proyecto:
    El proyecto consta del desarrollo de una API REST, la cual conste de 3 servicios:
    
    1)TOPTEN: Servicio que, en funcion del puntaje obtenido en la psu del consumidor,
              entregue las 10 carreras en las que este mejor posicionado.
              
              En caso de no entrar en primera instancia, entrega si posicion relativa 
              en la lista de espera.
              
    2)CARRER: Servicio que recibe un codigo numerico, el cual corresponde a el codigo
              de alguna de las carreras de la UTEM; entrega toda la informacion de 
              esta ultima.
              
              En caso de que el codigo no sea valido, o no se encuentre una carrera 
              con el respectivo codigo, se entrega una excepcion.
              
    3)CARRERS: Servicio el cual recibe un o N palabras (ya sea como una sola expresion,
               como varias), las cuales se corroboran que concuerden con el nombre de 
               alguna carrera; si se cumple este caso, se entregara la informacion de 
               todas las carreras a las que concuerden.
               
               Si no concuerda con ninguna, o el largo es menor al establecido (minimo 
               4 caracteres para que la palabra sea valida), se entregara la respectiva 
               excepcion.
               
* Para mas informacion, consultar el README del repositorio 'https://github.com/Reko-Glarius/Api-REST' *
"""
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
            json={
                'codigo':400,
                'mensaje':"Datos enviados incorrectamente, corrobore las etiquetas de los datos"
            }
            return jsonify(json), 400

        try:
            nem = float(nem)
            ranking = float(ranking)
            matematicas = float(matematicas)
            lenguaje = float(lenguaje)
            ciencias = float(ciencias)
            historia = float(historia)
        except:
            json={
                'codigo':400,
                'mensaje':"Datos enviados invalidos, los valores deben ser unicamente numericos"
            }
            return jsonify(json), 400
        var=matematicas+lenguaje
        var=var/2
        if(var<450):
            json = {
                'codigo': 400,
                'mensaje': "El promedio entre lenguaje y matematicas promedia menos de 450 puntos"
            }
            return jsonify(json), 400
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
            json = {
                'codigo': 400,
                'mensaje': "La cantidad de carreras enviadas es invalida; debe ser enviado solo 1"
            }
            return jsonify(json), 400
        else:
            try: ###Corrobora la existencia de una variable 'codigo'; de no existir, manda excepcion
                cod_recibido=args['codigo']
            except:
                json = {
                    'codigo': 400,
                    'mensaje': "Nombre de variable invalido; la variable debe llamarse 'codigo'"
                }
                return jsonify(json), 400

            try: ###Corrobora si el codigo es numerico, si no lo es, manda error (los codigos de la UTEM son unicamente numericos)
                cod_recibido=int(args['codigo'])
            except:
                json = {
                    'codigo': 400,
                    'mensaje': "El codigo a corroborar es invalido; solo codigos numericos"
                }
                return jsonify(json), 400
            
            carreras=generar_info_carreras() ###Se genera un listado con todos los datos de todas las carreras
            for iteracion in range(0,29): ###Se realiza un ciclo iterativo para revisar si existe una carrera con el respectivo codigo
                if (iteracion == 28): ### En caso de no encajar con ningun codigo de carrera, se retorna una excepcion
                    json = {
                        'codigo': 400,
                        'mensaje': "El codigo recibido NO concuerda con ninguna carrera"
                    }
                    return jsonify(json), 400
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
            json = {
                'codigo': 400,
                'mensaje': "Cantidad de datos invalido, debe enviarse almenos 1 variable"
            }
            return jsonify(json), 400
        elif(len(args)==1): ###En caso de que solo se reciba solo una variable
            palabra=''
            try:
                palabra=str(args['texto_1']) ###Se corrobora la existencia de la variable solicitada
            except: ###En caso de no estar, se manda una excepcion
                json = {
                    'codigo': 400,
                    'mensaje': "Nombre de variable invalido, la variable debe llamarse 'texto_1'"
                }
                return jsonify(json), 400
            palabra=palabra.upper() ###La palabra es pasada a mayusculas para mejorar el manejo a futuro
            if(len(palabra)<=3): ###Se corrobora que la palabra tenga almenos 4 caracteres (incluyend)
                json = {
                    'codigo': 400,
                    'mensaje': "La palabra no cumple con el largo minimo (4 caracteres)"
                }
                return jsonify(json), 400
            carreras=generar_info_carreras()
            respuestas=[] ###Listado de carreras validas
            for carrera in carreras: ###Para cada carrera...
                if(carrera[1].upper().find(palabra)>=0): ###Se corrobora que la palabra se encuentre dentro del nombre de la carrera...
                    respuestas.append({ ###De estar presente, almacena toda la informacion de esa carrera para posteriormente entregarla
                        "Codigo":carrera[0],
                        "Nombre":carrera[1],
                        "Nem": carrera[2],
                        "Ranking": carrera[3],
                        "Lenguaje": carrera[4],
                        "Matematicas": carrera[5],
                        "Ciencias sociales o Historia": carrera[6],
                        "Pun. prom. min. entre Leng. y Mat.": carrera[7],
                        "Pun. Min. de postulacion": carrera[8],
                        "Vacantes": carrera[9],
                        "Primer matriculado": carrera[10],
                        "Ultimo matriculado": carrera[11]
                    })
            if(len(respuestas)==0): ###En caso de no encontrarse carrera, retorna excepcion
                json = {
                    'codigo': 400,
                    'mensaje': "La palabra recibida no concuerda con ninguna carrera"
                }
                return jsonify(json), 400
            else: ###Si se encuentra almenos 1, las entrega con exito
                return jsonify(respuestas), 200
        else: ###En caso de recibir multiples variables (cada una con una palabra)
            palabras=[]
            for i in range(0,len(args)): ###Se realiza un ciclo iterativo, en el cual almacena todas las variables nombradas 'text_n', donde n es menor/igual a la cantidad de variables recibidas
                try:
                    palabras.append(str(args["texto_"+str(i+1)]))
                except:
                    pass
            copia_palabras=[]
            if(len(palabras)==0): ###En caso de que no se detecte ninguna variable con un nombre valido, se retorna una escepcion
                json = {
                    'codigo': 400,
                    'mensaje': "La cantidad de palabras recibidas es invalido; debe ser almenos 1"
                }
                return jsonify(json), 400
            else: ###En caso de que si hayan, se realiza ciclo iterativo para corroborar que cumplen con la cantidad minima de letras por palabra
                for palabra in palabras:
                    if(len(palabra)<=3):
                        pass
                    else: ###Si son validas, se re almacenan, en caso contrario, no
                        copia_palabras.append(palabra.upper())
            if(len(copia_palabras)==0): ###En caso de que no queden palabras, se retorna una excepcion
                json = {
                    'codigo': 400,
                    'mensaje': "Las palabras recibidas son invalidas; deben tener minimo 4 caracteres cada una"
                }
                return jsonify(json), 400
            else: ###En caso contrario, se prosigue con el servicio
                palabras=copia_palabras
            carreras=generar_info_carreras() ###Se crea lista con todos los datos de todas las carreras
            datos_carreras_seleccionadas=[]
            codigos=[]
            contador=0
            for palabra in palabras: ###Se realiza ciclo, en el cual, para cada palabra...
                contador=0
                for carrera in carreras: ###Se comprueba para cada carrera...
                    if(carrera[1].upper().find(palabra)>=0 and carrera[0] not in codigos): ###Con la condicion de estar presente y que esta carrera no este ya registrada
                        codigos.append(carrera[0])
                        datos_carreras_seleccionadas.append({
                            "Codigo": carreras[contador][0],
                            "Nombre": carreras[contador][1],
                            "Nem": carreras[contador][2],
                            "Ranking": carreras[contador][3],
                            "Lenguaje": carreras[contador][4],
                            "Matematicas": carreras[contador][5],
                            "Ciencias sociales o Historia": carreras[contador][6],
                            "Pun. prom. min. entre Leng. y Mat.": carreras[contador][7],
                            "Pun. Min. de postulacion": carreras[contador][8],
                            "Vacantes": carreras[contador][9],
                            "Primer matriculado": carreras[contador][10],
                            "Ultimo matriculado": carreras[contador][11]
                        })
                    contador+=1
            if(len(datos_carreras_seleccionadas)==0): ###En caso de que ningun codigo concuerde con alguna carrera, se retorna excepcion
                json = {
                    'codigo': 400,
                    'mensaje': "No se encontre ninguna carrera que concordase con esas palabras"
                }
                return jsonify(json), 400
            else: ###En caso contrario, se retornan las carreras de manera exitosa
                return jsonify(datos_carreras_seleccionadas), 200

app.run() ###Activacion del servicio