import psycopg2
import pandas as pd
from IPython.display import display

try:
    conexion = psycopg2.connect(user="postgres",
                                password="972672",
                                database="proyecto_inge2.3",
                                host="localhost",
                                port="5432")
    print("Conexión correcta!")
    

    tablas=["asignatura","tipo_profesor","grupo"]
    #sql1="""SELECT COUNT(*)
    #        FROM information_schema.columns
    #        WHERE table_name = f"{tablas[i]} """
    #sqln=""" SELECT COUNT(*)
    #        FROM information_schema.columns
    #        WHERE table_name = 'proyecto_total';"""
    
#se establece el numero de columnas de la tabla
#    cursor1 = conexion.cursor()
#   cursor1.execute(sqln)
#    asig1 = cursor1.fetchone()
#    #n=int(asig1[0])
    
##############################################################################################################################
#Se ejecuta la sentencia para mostrar los nombres de las asignaturas
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
##########################################################################################################################33
#Se ejecuta la sentencia para mostrar los nombres de las tipos_profesor
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
###################################################################################################################3#
#Se ejecuta la sentencia para mostrar los nombres de las grupos
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
################################################################################################################33333
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

###############################################################################################################################333#3###
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
    #############################################################################################################################3
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
    ################################################################################################################################
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
###############################################################################################################################################
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
    ##############################################################################################################################
    sql2= """select*
    from profesor_tipo_p;"""
    n=2

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
                "id_tipo_p":linea[1]}
        full_data.append(dato)
    dataframe = pd.DataFrame(full_data)
    print(dataframe.to_markdown())

    #############################################################################################################################3
except psycopg2.Error as e:
    print("Ocurrió un error al consultar: ", e)

finally:
    cursor.close()
    conexion.close()
