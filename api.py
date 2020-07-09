from itertools import cycle
from flask import Flask, escape, request
from api_function import generar_datos_carreras, generar_ponderaciones_postulante

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def say_hi():
    return 'API funcionando'

@app.route('/topten', methods=['POST'])
def digito_verificador():
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
        ##############################################  Creacion del Json final
        return{
            "nem":nem,
            "ranking":ranking
        }
        """
        n_rut = rut.split("-")
        reversed_digits = map(int, reversed(str(n_rut[-1])))
        factors = cycle(range(1, 8))
        s = sum(d * f for d, f in zip(reversed_digits, factors))
        mod = (-s) % 10
        if (mod == 9):
            mod = 'k'
        if (mod == 10):
            mod = -1
        if (str(mod) == str(n_rut[0])):
            return {
                "rut": rut,
                "digito verificador": mod,
                "mensaje": "rut correcto"
            }
        else:
            return {
                "mensaje": "rut no coincide con el digito verificador",
                "ingresado": str(n_rut[0]),
                "correcto": mod
            }
            """ 

@app.route('/saludo', methods=['POST'])
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


app.run()
