# Proyecto_ingenieria
<h2>integrantes:</h2>
<ul>
  <li>Paula Andrea Castiblanco Niño</li>
  <li>Daniela Sofía Gil Polaco </li>
  <li>Juan Sebastián Contreras Alejo </li>
 </ul>
<br>

<h3>Sobre el proyecto:</h3>
<p> Desde hace mucho tiempo se usa excel para el manejo de informacion "masiva" sin embargo con el paso del tiempo se implementaron herramientas más eficientes a la hora del manejo de bases de datos, una de estas es postgresql que atravez del leguaje SQL, la cual permite mantener toda la informacion, y al mismo tiempo , a travez de consultas, se puede visualizar de forma más clara y compacta usando relaciones entre tablas, asi mismo ocupa un espacion menor en memoria y es facilmente portable. </p>

<p> Este github contiene todos los archivos necesarios para el diseño e implementacion de la base de datos, ubicada en prueba.csv, en postgresql. <br>
podran encontrar dos carpetas, en la primera, nombrada "Excel", se encontrarán los archivos .csv que contienen los datos de las tablas de su mismo nombre. La segunda , "Postgres" donde se encuentran varios scripts con diferentes propositos que se deben ejecutar en postgresql, finalmente en el directorio "main" se encuentra la dase de datos y un .jpg con la foto del diagrama relacional de nuestro proyecto </p>
 
 
<h3>instrucciones para la creacion de la base de datos:</h3>
<p>Aclaración:  se usó el arcihivo /script_generar_excel.txt en una base de datos temporal, ya que su unica funcionalidad es convertir la base de datos completa(prueba.csv) a las diferentes tablas que se van a trabajar en el proyecto,  ordena estos datos creando archivos excel individuales , los cuales se ubicaron en la carpeta /excel/, segun las tablas definidas en el diagrama relacional. </p>

a continuacion están las instruciones para el uso de estos archivos: <br>
<ol>
  <li>prinero que nada, se debe correr el archivo /script_pgmodeler_modificado.txt, a partir de este se generará estructura de la base de datos que se usará en el    proyecto
  <li>una vez generada se puede utiizar el archivo /script_cargar_datos.txt que carga los datos desde los excel .csv a la base de datos creadas en el punto 1
</ol>


<h3> utilidades del proyecto </h3>
este proyecto tiene dos funcionalidades principales:
<ol>
  <li><h4>visualización de tablas</h4>
  <li><h4>analisis, (DASH) </h4>
</ol>

<h4>visualización de tablas</h4>
<p> esta se puede realizar a traves del archivo en /python/ Conexión_Consulta.py </p>
      se deben instalar las librerías:
      <ul>
          <li>pandas
          <li>tabulate
          <li>display
      </ul>


  
 
