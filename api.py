##########################################################  Librerias
from flask import Flask, escape, request
from api_function import generar_datos_carreras, generar_ponderaciones_postulante

##########################################################  Definiciones del servicio
app = Flask(__name__)
app.config["DEBUG"] = True

##########################################################  Servicios Incorporados
@app.route('/') ###Servicio por defecto: Confirma que se esta pudiendo consumir el servicio
def say_hi():
    return 'API funcionando'

@app.route('/topten', methods=['POST']) ###Servicio POST 10mejores: Mediante los puntajes de un postulante, entrega un JSON con las 10 mejores carreras para el
def generar_top():
    if(request.method=='POST'):
        ##############################################  Variables
        nem=request.form.get('nem')
        ranking=request.form.get('ranking')
        matematicas=request.form.get('matematicas')
        lenguaje=request.form.get('lenguajes')
        ciencias=request.form.get('ciencias')
        historia=request.form.get('historia')
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
            mi_numero=ponderacion_postulante[posicion]
            if(mi_numero>=base[2]):
                while(mi_numero>=base[2]):
                    if(mi_numero>base[2]):
                        contador+=1
                        mi_numero+=base[3]
                    else:
                        mis_carreras.append([posicion+1, contador])
                        break
            else:
                contador=0
                while(mi_numero<base[2]):
                    if(mi_numero<base[2]):
                        base[2]-=base[3]
                        contador-=1
                    else:
                        mis_carreras.append([posicion+1, contador])
                        break
        ##############################################  Ordenamiento de datos y creacion del Json final a retornar
        mis_carreras=ordenar(mis_carreras)
        Jsons=[]
        for iteracion in range(0,10):
            datos=mis_carreras[iteracion]
            datos_carrera_particular=carreras[datos[0]]
            if(datos[0]>=0):
                json_especifico={
                    "Codigo":datos_carrera_particular[1],
                    "Nombre":datos_carrera_particular[0],
                    "Ponderacion":datos[0],
                    "Posicion":(130-datos[1])
                }
                Jsons.append(json_especifico)
            else:
                json_especifico={
                    "Codigo":datos_carrera_particular[1],
                    "Nombre":datos_carrera_particular[0],
                    "Ponderacion":datos[0],
                    "Posicion":"Lista de Espera: "+str(datos[1])
                }
                Jsons.append(json_especifico)
        ### Retorno del JSON final
        return {
            "Carrera 1":Jsons[0],
            "Carrera 2":Jsons[1],
            "Carrera 3":Jsons[2],
            "Carrera 4":Jsons[3],
            "Carrera 5":Jsons[4],
            "Carrera 6":Jsons[5],
            "Carrera 7":Jsons[6],
            "Carrera 8":Jsons[7],
            "Carrera 9":Jsons[8],
            "Carrera 10":Jsons[9],
        }

@app.route('/saludo', methods=['GET'])
def generar_saludo():
    if(request.method=='POST'):
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


app.run() ###Activacion del servicio
