#librerias necesarias
	#pip install pandas
	#pip install tabulate
	#pip install display

import psycopg2
import pandas as pd
from IPython.display import display

#se definen las consultas de las tablas con un markdown() para una visualizacion más comoda y clara
def asignatura():
    sql1 = """select *
    from asignatura;"""
    n=3

    cursor = conexion.cursor()
    cursor.execute(sql1)
    asig = cursor.fetchone()
    
    print("*********************************************ASIGNATURAS****************************************************")
    full_data = []
    while asig:
        linea = ""
        for i in range(n):
            linea += f"{asig[i]}:"
            #print(linea)
            #print(asig[i], end=" ")
            asig = cursor.fetchone()
        linea = linea.split(":")
        dato = {"codigo":linea[0],
                "nombre":linea[1],
                "tipologia":linea[2]}
        full_data.append(dato)
    dataframe = pd.DataFrame(full_data)
    print(dataframe.to_markdown())
    cursor.close()

    

def tipo_profesor():
    sql2= """select *
    from tipo_p;"""
    n=2

    cursor = conexion.cursor()
    cursor.execute(sql2)
    asig1 = cursor.fetchone()
    
    print("*******************************************************tipo_profesor**************************************************")
    full_data = []
    while asig1:
        linea = ""
        for i in range(n):
            linea += f"{asig1[i]}:"
            #print(linea)
            #print(asig1[i], end=" ")
        asig1 = cursor.fetchone()
        linea = linea.split(":")
        dato = {"id":linea[0],
                "tipo":linea[1],}
        full_data.append(dato)
    dataframe = pd.DataFrame(full_data)
    print(dataframe.to_markdown())
    cursor.close()    
    
def grupo():
    sql2= """select *
    from grupo;"""
    n=3

    cursor = conexion.cursor()
    cursor.execute(sql2)
    asig1 = cursor.fetchone()
    
    print("*************************************************grupo*********************************************************************")
    full_data = []
    while asig1:
        linea = ""
        for i in range(n):
            linea += f"{asig1[i]}:"
            #print(linea)
            #print(asig1[i], end=" ")
        asig1 = cursor.fetchone()
        linea = linea.split(":")
        dato = {"grupo":linea[0],
                "capacidad":linea[1],
                "codigo_asignatura":linea[2]}
        full_data.append(dato)
    dataframe = pd.DataFrame(full_data)
    print(dataframe.to_markdown())
    cursor.close()

def horaro_grupo():
    sql2= """select *
    from horario_grupo;"""
    n=5

    cursor = conexion.cursor()
    cursor.execute(sql2)
    asig1 = cursor.fetchone()
    
    print("***************************************************horario_grupo*********************************************************")
    full_data = []
    while asig1:
        linea = ""
        for i in range(n):
            linea += f"{asig1[i]};"
            #print(linea)
            #print(asig1[i], end=" ")
        asig1 = cursor.fetchone()
        linea = linea.split(";")
        dato = {"dia":linea[0],
                "hora_inico":linea[1],
                "hora_fin":linea[2],
                "grupo":linea[3],
                "codigo_asig":linea[4]}
        full_data.append(dato)
    dataframe = pd.DataFrame(full_data)
    print(dataframe.to_markdown()) 
    cursor.close()    

    
def horario():
    sql2= """select *
    from horario;"""
    n=3

    cursor = conexion.cursor()
    cursor.execute(sql2)
    asig1 = cursor.fetchone()
    
    print("***************************************************horario*********************************************************")
    full_data = []
    while asig1:
        linea = ""
        for i in range(n):
            linea += f"{asig1[i]};"
            #print(linea)
            #print(asig1[i], end=" ")
        asig1 = cursor.fetchone()
        linea = linea.split(";")
        dato = {"dia":linea[0],
                "hora_inico":linea[1],
                "hora_fin":linea[2]}
        full_data.append(dato)
    dataframe = pd.DataFrame(full_data)
    print(dataframe.to_markdown()) 
    cursor.close()    

    

    
def asignatura_profesor():
    sql2= """select*
    from asignatura_profesor;"""
    n=2

    cursor = conexion.cursor()
    cursor.execute(sql2)
    asig1 = cursor.fetchone()
    
    
    print("***************************************************asignatura_profesor*********************************************************")
    full_data = []
    while asig1:
        linea = ""
        for i in range(n):
            linea += f"{asig1[i]};"
            #print(linea)
            #print(asig1[i], end=" ")
        asig1 = cursor.fetchone()
        linea = linea.split(";")
        dato = {"codigo_asignatura":linea[0],
                "cedula_profesor":linea[1]}
        full_data.append(dato)
    dataframe = pd.DataFrame(full_data)
    print(dataframe.to_markdown())
    cursor.close()  
    
def grupo_profesor():
    sql2= """select*
    from grupo_profesor;"""
    n=6

    cursor = conexion.cursor()
    cursor.execute(sql2)
    asig1 = cursor.fetchone()
    
    print("***************************************************grupo_profesor*********************************************************")
    full_data = []
    while asig1:
        linea = ""
        for i in range(n):
            linea += f"{asig1[i]};"
            #print(linea)
            #print(asig1[i], end=" ")
        asig1 = cursor.fetchone()
        linea = linea.split(";")
        dato = {"fecha_inicio":linea[0],
                "fecha_cierre":linea[1],
                "grupo":linea[2],
                "codigo_asignatura":linea[3],
                "cedula_profesor":linea[4],
                "observaciones":linea[5]}
        full_data.append(dato)
    dataframe = pd.DataFrame(full_data)
    print(dataframe.to_markdown())    
    cursor.close()  

def profesor():
    sql2= """select*
    from profesor;"""
    n=3

    cursor = conexion.cursor()
    cursor.execute(sql2)
    asig1 = cursor.fetchone()
    
    print("***************************************************profesor*********************************************************")
    full_data = []
    while asig1:
        linea = ""
        for i in range(n):
            linea += f"{asig1[i]};"
            #print(linea)
            #print(asig1[i], end=" ")
        asig1 = cursor.fetchone()
        linea = linea.split(";")
        dato = {"cedula_profesor":linea[0],
                "nombre_profesor":linea[1],
                "escalafon":linea[2]}
        full_data.append(dato)
    dataframe = pd.DataFrame(full_data)
    print(dataframe.to_markdown())
    cursor.close()  

def profesor_tipo_p():  
    sql2= """select*
    from profesor_tipo_p;"""
    n=2

    cursor = conexion.cursor()
    cursor.execute(sql2)
    asig1 = cursor.fetchone()
    
    print("***************************************************profesor_tipo_profesor*********************************************************")
    full_data = []
    while asig1:
        linea = ""
        for i in range(n):
            linea += f"{asig1[i]};"
            #print(linea)
            #print(asig1[i], end=" ")
        asig1 = cursor.fetchone()
        linea = linea.split(";")
        dato = {"cedula_profesor":linea[0],
                "id_tipo_p":linea[1]}
        full_data.append(dato)
    dataframe = pd.DataFrame(full_data)
    print(dataframe.to_markdown())
    cursor.close()  
    
def modalidad():
    sql2= """select*
    from tipo_modalidad;"""
    n=2

    cursor = conexion.cursor()
    cursor.execute(sql2)
    asig1 = cursor.fetchone()
    
    print("***************************************************modalidad*********************************************************")
    full_data = []
    while asig1:
        linea = ""
        for i in range(n):
            linea += f"{asig1[i]};"
            #print(linea)
            #print(asig1[i], end=" ")
        asig1 = cursor.fetchone()
        linea = linea.split(";")
        dato = {"id":linea[0],
                "modalidad":linea[1]}
        full_data.append(dato)
    dataframe = pd.DataFrame(full_data)
    print(dataframe.to_markdown())
    cursor.close() 

def ayuda():
    print ("instrucciones: ")
    print("las tablas son:")
    print("\t asignatura \n \t tipo profesor \n \t grupo \n \t horario_grupo \n \t horario \n \t asignatura profesor \n \t grupo profesor \n \t profesor \n \t profesor tipo profesor \n \t modalidad")
    print("recuerde escribir todo en minusculas")
    print("si quiere salir del programa escriba no mas")
    
#inicio de la conexion
try:
    conexion = psycopg2.connect(user="postgres",
                                password="123456",
                                database="proyecto_inge",
                                host="localhost",
                                port="5432")
    print("Conexión correcta!")
    
    
    
#condicional para mostrar las tablas segun lo deseado por el usuario
    corriendo=True
    
    while corriendo:
        ex=input("que taba quiere ver: ")
    
        if ex=="asignatura":
            asignatura()
        elif ex=="grupo":
            grupo()
        elif ex=="horario_grupo":
            horaro_grupo()
        elif ex=="horario":
            horario()
        elif ex=="asignatura profesor":
            asignatura_profesor()
        elif ex=="grupo profesor":
            grupo_profesor()
        elif ex=="profesor":
            profesor()
        elif ex=="profesor tipo profesor":
            profesor_tipo_p()
        elif ex=="modalidad":
            modalidad()
        elif ex=="no mas":
            corriendo=False
        elif ex==".help":
            ayuda()

        else:
            print("ingrese un valor valido, para mas informacion escriba .help")

    conexion.close()

###############################################################################################################################333#3###
    
    ################################################################################################################################
    
###############################################################################################################################################
    
    ##############################################################################################################################

    #############################################################################################################################3
except psycopg2.Error as e:
    print("Ocurrió un error al consultar: ", e)

finally:
    conexion.close()
