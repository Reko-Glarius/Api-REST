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
def 10mejores():
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
        ##############################################  Ordenamiento y re-configuracion listado
        mis_carreras=ordenar(mis_carreras)
        for iteracion in range(0,28):
            datos=mis_carreras[iteracion]
            if()
        ##############################################  Creacion del Json final a retornar
        return{
            "Carrera 1":str(mis_carreras[0][0])+"%"+str(mis_carreras[0][1])+"%"+str(mis_carreras[0][2])+"%"+str(mis_carreras[0][3]),
            "Carrera 2":str(mis_carreras[1][0])+"%"+str(mis_carreras[1][1])+"%"+str(mis_carreras[1][2])+"%"+str(mis_carreras[1][3]),
            "Carrera 3":str(mis_carreras[2][0])+"%"+str(mis_carreras[2][1])+"%"+str(mis_carreras[2][2])+"%"+str(mis_carreras[2][3]),
            "Carrera 4":str(mis_carreras[3][0])+"%"+str(mis_carreras[3][1])+"%"+str(mis_carreras[3][2])+"%"+str(mis_carreras[3][3]),
            "Carrera 5":str(mis_carreras[4][0])+"%"+str(mis_carreras[4][1])+"%"+str(mis_carreras[4][2])+"%"+str(mis_carreras[4][3]),
            "Carrera 6":str(mis_carreras[5][0])+"%"+str(mis_carreras[5][1])+"%"+str(mis_carreras[5][2])+"%"+str(mis_carreras[5][3]),
            "Carrera 7":str(mis_carreras[6][0])+"%"+str(mis_carreras[6][1])+"%"+str(mis_carreras[6][2])+"%"+str(mis_carreras[6][3]),
            "Carrera 8":str(mis_carreras[7][0])+"%"+str(mis_carreras[7][1])+"%"+str(mis_carreras[7][2])+"%"+str(mis_carreras[7][3]),
            "Carrera 9":str(mis_carreras[8][0])+"%"+str(mis_carreras[8][1])+"%"+str(mis_carreras[8][2])+"%"+str(mis_carreras[8][3]),
            "Carrera 10":str(mis_carreras[9][0])+"%"+str(mis_carreras[9][1])+"%"+str(mis_carreras[9][2])+"%"+str(mis_carreras[9][3])
        }

@app.route('/saludo', methods=['GET'])
def generar_saludo():
    if request.method == 'POST':
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
