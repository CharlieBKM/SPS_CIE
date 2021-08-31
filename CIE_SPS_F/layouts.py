# Dash components, html, dash tables,...
import dash_html_components as html
import dash_bootstrap_components as dbc


              

# Para tablas con enlaces a bases de datos
bancoLayout =html.Div([
    dbc.Row(dbc.Col(html.H3(children='\n'))),
    dbc.Row(dbc.Col(html.H3(children='Material para consulta y análisis', style={'fontSize':27}))),
    dbc.Row(dbc.Col(html.H3(children='\n'))),
    dbc.Row(dbc.Col(html.H3(children='\n'))),
    dbc.Row(dbc.Col(html.H3(children='• Servicios de salud', style={'fontSize':18}))),
    html.Iframe(src='assets/appBD.html', width='100%', height='200', 
                style={'border':'none'},
                ),
    dbc.Row(dbc.Col(html.H3(children='• Servicios de Guardería', style={'fontSize':18}))),
    html.Iframe(src='assets/appBD_G.html', width='100%', height='200', 
                style={'border':'none'},
                )
],className = 'app-page')




# Para Sistema de Percepción Social
spsLayout=html.Div([
    
    html.Iframe(src='assets/A1.html', width='100%', height='850', 
                style={'background': '13322B', 'border':'none'},
                )
],className = 'app-page')





#Para resultados 
secciones={
    'Actuación del IMSS ante la contingencia sanitaria por Covid-19':['imsscovid','imsscomp'],
    'Percepción de seguridad en las unidades médicas del IMSS':['protec_med'],
    'Salud mental ante el distanciamiento social':['salud_m_a','salud_m_b','salud_m_c','salud_m_d',
                                                   'salud_m_e','salud_m_f'],
    'Vacunación contra Covid-19 y expectativas sobre el final de la pandemia':['protec_vac','esperanza'],
    'Hospitalización por Covid-19 en el IMSS y en hospitales diferentes al IMSS':['covid_diag3',
                                                                                  'covid_diagf3','covid_diagf3_n_x'],
    'Trabajo en casa':['trabajo'],
    'Difusión de información sobre Covid-19':['infimss'],
    'Preferencias en la atención':['atnpref','atn1fam'],
    'Transparencia y posibles acciones de corrupción':['atnpref2_a','corrup1','quejas'],
    'Condicionamiento en la entrega de medicamentos':['corrupfarm'],
    'Solicitud de atención médica en farmacias con consultorio privado':['cons_farm'],
    'Surtimiento de medicamentos':['totmed'],
    'Satisfacción y trato':['sat3','sat3_mot_a','sat3_mot_b','sat3_mot_c','sat3_mot_d',
                            'sat3_mot_e','sat3_mot_f','btratou'],
    'Diagnóstico de Covid-19 de personas usuarias y familiares':['covid_diag1','covid_diag2',
                                                                 'covid_diagf2_x','covid_def',
                                                                 'covid_diagg2_x']              
            }


titulo=html.Div('Resultados de la Encuesta Nacional de Imagen del IMSS 2021', style={'fontSize':27,"textAlign": "center", 'font-weight':'bold'},)


resLayout = html.Div(
    [
     dbc.Row(html.Div("Sistema Integral de Medición de la Satisfacción de Usuarios",
                       style={'fontSize':27,"textAlign": "center", 'font-weight':'bold'},)
             ,justify="center"),
     html.Br(),
     
     dbc.Row(html.Div("Mediciones en 2021",
                      style={'fontSize':23,"textAlign": "center"},
                      ),justify="center"),
     html.Br(),
     dbc.Row(
         [
            dbc.Col(html.Button("Encuesta Nacional de Imagen Institucional"),width = 10, lg=6),                    
         ],
         justify="center"),
      html.Br(),
     
     
     dbc.Row(html.Div("Mediciones en 2020",
                      style={'fontSize':23,"textAlign": "center"},
                      ),justify="center"),
     html.Br(),
     dbc.Row(
         [
            dbc.Col(html.Button("Estudio Nacional de Calidad de la Atención y de los servicios de salud"),width = 10, lg=6),                    
            dbc.Col(html.Button("Estudio Nacional de Calidad de la Atención del servicio de guardería"),width = 10, lg=6),
         ],
         justify="center"),
     html.Br(),
     
     dbc.Row(html.Div("Mediciones en 2019",
                      style={'fontSize':23,"textAlign": "center"},
                      ),justify="center"),
     
     html.Br(),
     dbc.Row(
         [
            dbc.Col(html.Button("Estudio Nacional de Calidad de la Atención y de los servicios de salud")),                    
            dbc.Col(html.Button("Estudio Nacional de Calidad de la Atención del servicio de guardería")),
         ],
         justify="center"),
     html.Br(),
     
     dbc.Row(html.Div("Históricos",
                      style={'fontSize':23,"textAlign": "center"},
                      ),justify="center"),
     
     html.Br(),
     dbc.Row(html.Button("Comparación de los principales indicadores"),
         justify="center"),
     html.Br(),
        ]
        ),

