import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from Connection import Connection
import fisioterapiaSQL as sql                       

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

# Inicializacion app dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# horas_trabajadas
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.horas_trabajadas(), con.connection)
con.closeConnection()
dfhoras = pd.DataFrame(query, columns=["horas", "nombre"])

#estudiantes_esperados
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.estudiantes_esperados(), con.connection)
con.closeConnection()
dfestudiantes = pd.DataFrame(query, columns=["nombre", "cantidad_esperada"])

#falta_de_profesor
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.falta_de_profesor(), con.connection)
con.closeConnection()
dfprofesor = pd.DataFrame(query, columns=["nombre", "vacante"])

#clases_escalafon
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.clases_escalafon(), con.connection)
con.closeConnection()
dfescalafon = pd.DataFrame(query, columns=["tipo_escalafon", "cantidad"])

# Grafico barras horas_trabajadas
figBarhoras = px.bar(dfhoras.head(10), x="horas", y="nombre")

# Grafico lineal horas_trabajadas
figlinehoras = px.line(dfhoras.head(10), x="nombre", y="horas")

# Grafico barras estudiantes_esperados
figBarestudiantes = px.bar(dfestudiantes.head(60), x="nombre", y="cantidad_esperada")

# Grafico barras estudiantes_esperados
figlineestudiantes = px.line(dfestudiantes.head(60), x="nombre", y="cantidad_esperada")

# Grafico pie profesor
figpieprofessor = px.pie(dfprofesor.head(2), names="nombre", values="vacante")

# Grafico pie profesor
figBarprofesor = px.bar(dfprofesor.head(12), x="nombre", y="vacante")

#grafico pie clases_escalafon
figlineescalafon = px.line(dfescalafon.head(12), x="tipo_escalafon", y="cantidad")

#grafico baras clases_escalafon
figBarescalafon = px.bar(dfescalafon.head(12), x="tipo_escalafon", y="cantidad")




# Layout 
app.layout = html.Div(children=[
    
    html.H2(children='Casos por profesor'),
    html.H3(children='Grafico barras'),

    dcc.Graph(
        id='barhoras_trabajadas',
        figure=figBarhoras
    ),
   
    html.H3(children='Grafico de linea'),

    dcc.Graph(
        id='linehoras_trabajadas',
       figure=figlinehoras
    ),

    
    html.H2(children='Casos por estudiantes_esperados'),
    html.H3(children='Grafico barras'),
    dcc.Graph(
        id='barestudiantes_esperados',
        figure=figBarestudiantes
    ),
   
   html.H3(children='Grafico linea'),
   dcc.Graph(
        id='lineestudiantes_esperados',
        figure= figlineestudiantes
    ),
   

    
    html.H2(children='Casos por profesor'),
    html.H3(children='Grafico pie'),
    dcc.Graph(
        id='pieprofesor',
        figure = figpieprofessor
    ),

    html.H3(children='Grafico barras'),
    dcc.Graph(
        id='barprofesor',
        figure = figBarprofesor

    ),

    html.H2(children='Casos por Escalafon'),
    html.H3(children='Grafico line'),
    dcc.Graph(
        id='pieescalafon',
        figure = figlineescalafon
    ),

    html.H3(children='Grafico barras'),
    dcc.Graph(
        id='barescalafon',
        figure = figBarescalafon
    )
    

])

if __name__ == '__main__':
    app.run_server(debug=True)
