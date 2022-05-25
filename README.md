# Proyecto_ingenieria
<h2>integrantes:</h2>
<ul>
  <li>Paula Andrea Castiblanco Niño</li>
  <li>Daniela Sofía Gil Polanco </li>
  <li>Juan Sebastián Contreras Alejo </li>
 </ul>
<br>

<h3>Sobre el proyecto:</h3>
<p> Desde hace mucho tiempo se usa excel para el manejo de informacion "masiva" sin embargo con el pasar de los años se implementaron herramientas más eficientes a la hora de manejar bases de datos. Una de estas es postgresql, que atravez del lenguaje SQL, la cual permite mantener toda la informacion y al mismo tiempo , a travez de consultas, se puede visualizar de forma más clara y compacta usando relaciones entre tablas, asi mismo ocupa un espacion menor en memoria y es facilmente portable. </p>

<p> Este github contiene todos los archivos necesarios para el diseño e implementacion de la base de datos, ubicada en prueba.csv, en postgresql. <br>
podran encontrar dos carpetas, en la primera, nombrada "Excel", se encontrarán los archivos .csv que contienen los datos de las tablas de su mismo nombre. La segunda , "Postgres" donde se encuentran varios scripts con diferentes propositos que se deben ejecutar en postgresql, finalmente en el directorio "main" se encuentra la dase de datos y un .jpg con la foto del diagrama relacional de nuestro proyecto </p>

<b> <img width="538" alt="Captura" src="https://user-images.githubusercontent.com/91902584/170176711-4af65035-6b28-4969-8ce8-c310a6a17b52.png"> </b>


 
<h3>instrucciones para la creacion de la base de datos:</h3>
<p>Aclaración:  se usó el arcihivo /script_generar_excel.txt en una base de datos temporal, ya que su unica funcionalidad es convertir la base de datos completa(prueba.csv) a las diferentes tablas que se van a trabajar en el proyecto,  ordena estos datos creando archivos excel individuales , los cuales se ubicaron en la carpeta /excel/, segun las tablas definidas en el diagrama relacional. los excel tipología.csv , escalafón.csv y día.csv se crearon manualmente </p>

a continuacion están las instruciones para el uso de estos archivos: <br>
<ol>
  <li>antes que nada, se debe correr el archivo /script_pgmodeler_modificado.txt, a partir de este se generará estructura de la base de datos que se usará en el    proyecto
  <li>una vez generada se puede utiizar el archivo /script_cargar_datos.txt que carga los datos desde los excel .csv a la base de datos creadas en el punto 1
  <li>de ultimas se ejecuta /script_generacion_roles.txt para crear los roles estudiante, profesor y auxiliar registro
</ol>


<h3> utilidades del proyecto </h3>
este proyecto tiene dos funcionalidades principales:
<ul>
  <li><h5>visualización de tablas</h5>
  <li><h5>analisis practico, (DASH) </h5>
</ul>

<h5>visualización de tablas</h5>
<p> anteriormente se deben de tener las librerías: pandas, tabulate y display, instaladas en la maquina, esta se puede realizar a traves del archivo en /python/dash/ consulta_fisioterapia.py , este preguntará cual tabla se desea visualizar, se debe ingresar la tabla deseada y si se tiene dudas respecto a su nombre se ingresa un .help que despliega el nombre de todas las tablas de la forma que se debe ingresar, tambien se puede ingresar "no mas" para detener la consulta</p>


<h5>analisis practico de los datos</h5>
 para el proyecto se plantearon cuatro escenarios de analisis:
 <ol>
    <li> se quiere buscar un perfil del escalafón más usado a la hora de dictar clases
    <li> analizar la cantidad de estudiantes que la universidad espera que inscriban una asignatura, esto con el fin de evaluar cuál es la expectativa de la universidad  
     <li>analizar en cuales asignaturas hacen falta profesores y cuantos, esto con el fin de realizar perfiles en las entrevistas
      <li> analizar las horas trabajadas por los profesores, esto con el fin de evaluar aumentos, pagos y otros
 </ol>






  
 



