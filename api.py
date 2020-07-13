##########################################################  Librerias
from flask import Flask, escape, request, jsonify
from api_function import generar_datos_carreras, generar_ponderaciones_postulante, ordenar, generar_info_carreras
##########################################################  Definiciones del servicio
app = Flask(__name__)
app.config["DEBUG"] = True

##########################################################  Servicios Incorporados
@app.route('/', methods=['GET', 'POST']) ###Servicio por defecto: Confirma que se esta pudiendo consumir el servicio
def say_hi():
    return 'API funcionando'

@app.route('/topten', methods=['POST']) ###Servicio POST 10mejores: Mediante los puntajes de un postulante, entrega un JSON con las 10 mejores carreras para el
def generar_top():
    if(request.method=='POST'):
        ##############################################  Variables
        nem=float(request.form.get('nem'))
        ranking=float(request.form.get('ranking'))
        matematicas=float(request.form.get('matematicas'))
        lenguaje=float(request.form.get('lenguajes'))
        ciencias=float(request.form.get('ciencias'))
        historia=float(request.form.get('historia'))
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
        return jsonify(Jsons)

@app.route('/carrer/', methods=['GET']) ###Servicio el cual, para un codigo en particular, entrega la informacion de la respectiva carrera (solo acepta 1 codigo)
def datos_carrera():
    if(request.method=='GET'):
        args = request.args
        if(len(args)!=1): ###Corrobora que sea solo UN codigo el recibido, si no cumple, manda un error
            return {
                "Codigo de Error": 121,
                "Descripcion del Error": "La cantidad de carreras enviadas es diferente a las aceptadas por este sistema"
            }
        else:
            cod_recibido=args['codigo']
            try: ###Corrobora si el codigo es numerico, si no lo es, manda error (los codigos de la UTEM son unicamente numericos)
                cod_recibido=int(cod_recibido)
            except:
                return{
                    "Cod": 12312
                }
            
            carreras=generar_info_carreras() ###Se genera un listado con todos los datos de todas las carreras
            for iteracion in range(0,29): ###Se realiza un ciclo iterativo para revisar si existe una carrera con el respectivo codigo
                if(cod_recibido==carreras[iteracion][0]): ###Si existe una carrera con ese codigo, retorna su informacion
                    return {
                        "Codigo":carreras[iteracion][0],
                        "Nombre":carreras[iteracion][1]
                    }
                else: ###En caso contrario, prosigue;  si llega a la 29a iteracion, implica que no encontro ninguna carrera con el codigo respectivo, por lo que manda excepcion
                    if(iteracion==28):
                        return {
                            "Codigo de Error":232,
                            "Descripcion del Error": "El codigo ingresado no concuerda con el codigo de ninguna carrera"
                        }

@app.route('/carrers/', methods=['GET']) ###Servicio el cual, para un codigo en particular, entrega la informacion de la respectiva carrera (acepta n codigo)
def datos_carreras():
    if(request.method=='GET'):
        args = request.args
        if(len(args)==0):
            return {
                "Codigo de Error": 121,
                "Descripcion del Error": "La cantidad de carreras enviadas es diferente a las aceptadas por este sistema"
            }
        else:
            cod_recibido=args['codigo']
            try:
                cod_recibido=int(cod_recibido)
            except:
                return{
                    "Cod": 12312
                }
            carreras=generar_info_carreras()
            for iteracion in range(0,29):
                if(cod_recibido==carreras[iteracion][0]):
                    return {
                        "Codigo":carreras[iteracion][0],
                        "Nombre":carreras[iteracion][1]
                    }
                else:
                    if(iteracion==28):
                        return {
                            "Codigo de Error":232,
                            "Descripcion del Error": "El codigo ingresado no concuerda con el codigo de ninguna carrera"
                        }
"""
        print(codigo_carrera)
        nom = request.form.get('nombre')
        pat = request.form.get('paterno')
        mat = request.form.get('materno')
        nombreCompleto = nom + ' ' + pat + ' ' + mat + ' '
        nomComProp = nombreCompleto.title()
        sexo = request.form.get('sexo')
        if (int(sexo) == 1):
            sex = 'Sra. '
        else:
            sex = 'Sr. '
        return {
            "Sexo": sex,
            "Nombre completo": nomComProp,
            "Mensaje": "Saludos " + sex + nomComProp
        }
"""

app.run() ###Activacion del servicio
