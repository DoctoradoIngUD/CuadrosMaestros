import dash
import dash_core_components as dcc 
import dash_html_components as html
import plotly.express as px
import pandas as pd 
from dash.dependencies import Input,Output


dfArticulo = pd.read_csv("Resultados/año_articulo.csv")
dfLibro = pd.read_csv("Resultados/año_libro.csv")
dfCapitulo = pd.read_csv("Resultados/año_capitulo.csv")
dfEventos = pd.read_csv("Resultados/año_eventos.csv")
dfProyectos = pd.read_csv("Resultados/año_proyecto.csv")
dfSoftware = pd.read_csv("Resultados/año_software.csv")
dfCuartiles = pd.read_csv("Resultados/CuartilesPorAño.csv")
dfPublindex = pd.read_csv("Resultados/PublindexPorAño.csv")


print(dfCuartiles)
#print(df.vacuna_nombre.nunique())
#print(df.vacuna_nombre.unique())

app = dash.Dash(__name__)

app.layout = html.Div([
    
    html.Div([
        html.H1('Producción Academica Docotorado en Ingeniería'),
        html.Img(src='assets/Docto.png')
    ], className = 'banner'),



##########################---------Articulos-----------#####################################################

    html.Div([
        html.Div([
            html.P('Selecciona tipo de Producción de Articulos', className = 'fix_label', style={'color':'black', 'margin-top': '2px'}),
            dcc.RadioItems(id = 'dosis-radioitems', 
                            labelStyle = {'display': 'inline-block'},
                            options = [
                                {'label' : 'Nacional', 'value' : 'Nacional'},
                                {'label' : 'Internacional', 'value' : 'Internacional'}
                            ], value = 'Nacional',
                            style = {'text-aling':'center', 'color':'black'}, className = 'dcc_compon'),
        ], className = 'create_container2 five columns', style = {'margin-bottom': '20px'}),
    ], className = 'row flex-display'),

##Graficasss


        html.Div([
            html.Div([
                html.P('Producción Articulos', className = 'fix_label', style={'color':'black', 'margin-top': '2px'}),
                dcc.Graph(id = 'Produccion_Articulos', figure = {})
            ], className = 'create_container2 12 columns'),
    ], className = 'row flex-display'),


    # html.Div([
    #     html.Div([
    #         html.P('Producción Articulos', className = 'fix_label', style={'color':'black', 'margin-top': '2px'}),
    #         dcc.Graph(id = 'my_graph', figure = {})
    #     ], className = 'create_container2 eight columns'),

    #     html.Div([
    #         dcc.Graph(id = 'pie_graph', figure = {})
    #     ], className = 'create_container2 five columns')
    # ], className = 'row flex-display'),

##########################---------Libros-----------#####################################################
        html.Div([
            html.Div([
                html.P('Producción Libros', className = 'fix_label', style={'color':'black', 'margin-top': '2px'}),
                dcc.Graph(id = 'Produccion_Libros', figure = {})
            ], className = 'create_container2 eight columns'),

    ], className = 'row flex-display'),


    
################################---------Capitulos de Libros-----------####################################

  html.Div([
            html.Div([
                html.P('Capitulos de Libros', className = 'fix_label', style={'color':'black', 'margin-top': '2px'}),
                dcc.Graph(id = 'Produccion_Capitulos', figure = {})
            ], className = 'create_container2 eight columns'),

    ], className = 'row flex-display'),

#############################---------Eventos-----------#####################################

 html.Div([
            html.Div([
                html.P('Eventos Cientificos', className = 'fix_label', style={'color':'black', 'margin-top': '2px'}),
                dcc.Graph(id = 'Produccion_Eventos', figure = {})
            ], className = 'create_container2 eight columns'),

    ], className = 'row flex-display'),


##############################---------Proyectos-----------###############################
 html.Div([
            html.Div([
                html.P('Proyectos de Investigación', className = 'fix_label', style={'color':'black', 'margin-top': '2px'}),
                dcc.Graph(id = 'Produccion_Proyectos', figure = {})
            ], className = 'create_container2 eight columns'),

    ], className = 'row flex-display'),



##############################---------Software-----------##################################
 html.Div([
            html.Div([
                html.P('Producción de software', className = 'fix_label', style={'color':'black', 'margin-top': '2px'}),
                dcc.Graph(id = 'Produccion_Software', figure = {})
            ], className = 'create_container2 eight columns'),

    ], className = 'row flex-display'),

###############################################################################################

], id='mainContainer', style={'display':'flex', 'flex-direction':'column'})





########################################################################################
########################################################################################
#####################################---Call Backs----##################################


###########################-----Articulos------#########################


@app.callback(
    Output('Produccion_Articulos', component_property='figure'),
    [Input('dosis-radioitems', component_property='value')])

def update_graph(value):

    if value == 'Internacional':
        fig = px.bar(data_frame = dfCuartiles, x = '                AÑO', y = 'count', color='Cuartil')
    else :
        fig = px.bar(data_frame= dfPublindex,  x = '                AÑO', y = 'count', color='Publindex')        
    return fig


###########################-----Libros------#########################


@app.callback(
    Output('Produccion_Libros', component_property='figure'),
     [Input('dosis-radioitems', component_property='value')]
    )

def update_graph(value):
    if value:
        fig = px.bar(
            data_frame = dfLibro,
            x = '                 FECHA',
            y = 'count')  
    return fig


###########################-----Capitulos Libros------#########################

@app.callback(
    Output('Produccion_Capitulos', component_property='figure'),
     [Input('dosis-radioitems', component_property='value')]
    )

def update_graph(value):
    if value:
        fig = px.bar(
            data_frame = dfCapitulo,
            x = '                FECHA',
            y = 'count')  
    return fig

##########################-----Eventos-----##################################
@app.callback(
    Output('Produccion_Eventos', component_property='figure'),
     [Input('dosis-radioitems', component_property='value')]
    )

def update_graph(value):
    if value:
        fig = px.bar(
            data_frame = dfEventos,
            x = '                FECHA',
            y = 'count')  
    return fig
##########################-----Proyectos-----##################################

@app.callback(
    Output('Produccion_Proyectos', component_property='figure'),
     [Input('dosis-radioitems', component_property='value')]
    )

def update_graph(value):
    if value:
        fig = px.bar(
            data_frame = dfProyectos,
            x = '                FECHAI',
            y = 'count')  
    return fig

##########################-----Software-----##################################

@app.callback(
    Output('Produccion_Software', component_property='figure'),
     [Input('dosis-radioitems', component_property='value')]
    )

def update_graph(value):
    if value:
        fig = px.bar(
            data_frame = dfSoftware,
            x = '                FECHA',
            y = 'count')  
    return fig
###########################-----------###########################
##################################################################################







# @app.callback(
#     Output('pie_graph', component_property='figure'),
#     [Input('dosis-radioitems', component_property='value')])


# def update_graph_pie(value):

#     if value == 'Q1':
#         fig2 = px.pie(
#             data_frame = df,
#             names = '                AÑO',
#             values = 'count')
#     else:
#         fig2 = px.pie(
#             data_frame = df,
#             names = 'jurisdiccion_nombre',
#             values = 'segunda_dosis_cantidad'
#         )
#     return fig2

if __name__ == ('__main__'):
    app.run_server(host='10.100.66.8', port=8888, debug=True)