import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from flask import request, session
from utils.utils_login import loginizer


def serve_layout():
    app_layout = html.Div(
        [
            dbc.Row(
                [html.H1("Formulario de Diginautas 2023", id="title", style={"textAlign": "center"})], justify='center'
            ),
            dbc.Row(
                [
                    dbc.Col
                    ([
                        dbc.Form
                        ([
                            html.Div
                            ([
                                # TITULO
                                html.Div
                                ([
                                    dbc.Label(
                                        "Hola diginauta, te pedimos nos ayudes llenando este formulario para registrarte en nuestra base oficial!", className="form-label", id="form3-titulo"
                                    ),
                                ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-bottom': '15px'}),

                                # NOMBRES
                                html.Div
                                ([
                                    dbc.Label(
                                        "NOMBRES", className="form-label"
                                    ),
                                    dbc.Input(
                                        type="text", id="form3-nombre", placeholder="Tu respuesta", className="form-input"
                                    ),
                                ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-bottom': '15px'}),

                                # APELLIDOS
                                html.Div
                                ([
                                    dbc.Label(
                                        "APELLIDOS", className="form-label", id="form3-ape"
                                    ),
                                    dbc.Input(
                                        type="text", id="form3-apellido", placeholder="Tu respuesta", className="form-input"
                                    ),
                                ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-bottom': '15px'}),

                                # CORREO
                                html.Div
                                ([
                                    dbc.Label(
                                        "CORREO", className="form-label"
                                    ),
                                    dbc.Input(
                                        type="email", id="form3-correo", placeholder="Tu respuesta", className="form-input"
                                    ),
                                ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-bottom': '15px'}),

                                # CELULAR
                                html.Div
                                ([
                                    dbc.Label(
                                        "CELULAR", className="form-label"
                                    ),
                                    dbc.Input(
                                        type="text", id="form3-cell", placeholder="Tu respuesta", className="form-input"
                                    ),
                                ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-bottom': '15px'}),

                                # GÉNERO
                                html.Div
                                ([
                                    dbc.Label(
                                        "GÉNERO", className="form-label",
                                    ),
                                    dcc.Dropdown(
                                        id="form3-drop-genero",
                                        options=[
                                            {'label': 'Masculino',
                                                'value': 'Masculino'},
                                            {'label': 'Femenino',
                                                'value': 'Femenino'},
                                            {'label': 'Otro',
                                                'value': 'Otro'}
                                        ],
                                        placeholder="Elegir",
                                        className="form-input",
                                        style={'width': '100%',
                                               'textAlign': 'left'}
                                    ),
                                ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-bottom': '15px'}),

                                # PAIS
                                html.Div
                                ([
                                    dbc.Label(
                                        "PAIS DE NACIMIENTO", className="form-label",
                                    ),
                                    dcc.Dropdown(
                                        id="form3-drop-pais",
                                        options=[
                                            {'label': 'Argentina',
                                                'value': 'Argentina'},
                                            {'label': 'Chile',
                                                'value': 'Chile'},
                                            {'label': 'Ecuador',
                                                'value': 'Ecuador'},
                                            {'label': 'Perú',
                                                'value': 'Perú'},
                                            {'label': 'España',
                                                'value': 'España'},
                                            {'label': 'Colombia',
                                                'value': 'Colombia'},
                                            {'label': 'USA',
                                                'value': 'USA'},
                                        ],
                                        placeholder="Elegir",
                                        className="form-input",
                                        style={'width': '100%',
                                               'textAlign': 'left'}
                                    ),
                                ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-bottom': '15px'}),

                                # DEPARTAMENTO / CIUDAD
                                html.Div
                                ([
                                    dbc.Label(
                                        "DEPARTAMENTO / CIUDAD", className="form-label"
                                    ),
                                    dbc.Input(
                                        type="text", id="form3-departamento", placeholder="Tu respuesta", className="form-input"
                                    ),
                                ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-bottom': '15px'}),

                                # DIRECCION (Calle / Número)
                                html.Div
                                ([
                                    dbc.Label(
                                        "DIRECCIÓN (CALLE - NÚMERO)", className="form-label"
                                    ),
                                    dbc.Input(
                                        type="text", id="form3-direccion", placeholder="Tu respuesta", className="form-input"
                                    ),
                                ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-bottom': '15px'}),

                                # FECHA
                                html.Div
                                ([
                                    dbc.Label(
                                        "FECHA DE NACIMIENTO", className="form-label"
                                    ),
                                    dbc.Input(
                                        type="date", id="form3-fecha-nac", placeholder="Tu respuesta", className="form-input"
                                    ),
                                ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-bottom': '15px'}),

                                # DOCUMENTO
                                html.Div
                                ([
                                    dbc.Label(
                                        "TIPO DE DOCUMENTO DE IDENTIDAD", className="form-label",
                                    ),
                                    dcc.Dropdown(
                                        id="form3-drop-documento",
                                        options=[
                                            {'label': 'DNI',
                                                'value': 'DNI'},
                                            {'label': 'Carnet de extranjería',
                                                'value': 'Carnet de extranjería'},
                                            {'label': 'Otro',
                                                'value': 'Otro'}
                                        ],
                                        placeholder="Elegir",
                                        className="form-input",
                                        style={'width': '100%',
                                               'textAlign': 'left'}
                                    ),
                                ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-bottom': '15px'}),

                                # NUMERO DE DOCUMENTO
                                html.Div
                                ([
                                    dbc.Label(
                                        "NÚMERO DE DOCUMENTO DE IDENTIDAD", className="form-label"
                                    ),
                                    dbc.Input(
                                        type="number", id="form3-num-doc", placeholder="Tu respuesta", className="form-input"
                                    ),
                                ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-bottom': '15px'}),

                                # PAIS
                                html.Div
                                ([
                                    dbc.Label(
                                        "NIVEL EDUCATIVO", className="form-label",
                                    ),
                                    dcc.Dropdown(
                                        id="form3-nivel",
                                        options=[
                                            {'label': 'Secundaria completa',
                                                'value': 'Secundaria completa'},
                                            {'label': 'Estudiante',
                                                'value': 'Estudiante'},
                                            {'label': 'Técnico',
                                                'value': 'Técnico'},
                                            {'label': 'Universitario',
                                                'value': 'Universitario'},
                                            {'label': 'Magister',
                                                'value': 'Magister'},
                                            {'label': 'PHD',
                                                'value': 'PHD'},
                                            {'label': 'Otro',
                                                'value': 'Otro'},
                                        ],
                                        placeholder="Elegir",
                                        className="form-input",
                                        style={'width': '100%',
                                               'textAlign': 'left'}
                                    ),
                                ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-bottom': '15px'}),

                                # CARRERA
                                html.Div
                                ([
                                    dbc.Label(
                                        "CARRERA", className="form-label"
                                    ),
                                    dbc.Input(
                                        type="text", id="form3-carrera", placeholder="Tu respuesta", className="form-input"
                                    ),
                                ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-bottom': '15px'}),

                                # ESTADO CIVIL
                                html.Div
                                ([
                                    dbc.Label(
                                        "ESTADO CIVIL", className="form-label",
                                    ),
                                    dcc.Dropdown(
                                        id="form3-estado-civil",
                                        options=[
                                            {'label': 'Soltero(a)',
                                                'value': 'Soltero(a)'},
                                            {'label': 'Casado(a)',
                                                'value': 'Casado(a)'},
                                            {'label': 'Cohabitante legal',
                                                'value': 'Cohabitante legal'},
                                            {'label': 'Divorciado',
                                                'value': 'Divorciado'},
                                            {'label': 'Viudo(a)',
                                                'value': 'Viudo(a)'},
                                        ],
                                        placeholder="Elegir",
                                        className="form-input",
                                        style={'width': '100%',
                                               'textAlign': 'left'}
                                    ),
                                ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-bottom': '15px'}),

                                # TIENES HIJOS
                                html.Div
                                ([
                                    dbc.Label(
                                        "¿TIENES HIJOS, CUANTOS?", className="form-label",
                                    ),
                                    dcc.Dropdown(
                                        id="form3-hijos",
                                        options=[
                                            {'label': '0',
                                                'value': '0'},
                                            {'label': '1',
                                                'value': '1'},
                                            {'label': '2',
                                                'value': '2'},
                                            {'label': '3',
                                                'value': '3'},
                                            {'label': '4',
                                                'value': '4'},
                                            {'label': '5',
                                                'value': '5'},
                                            {'label': '6',
                                                'value': '6'},
                                            {'label': '7',
                                                'value': '7'},
                                            {'label': '8',
                                                'value': '8'},
                                        ],
                                        placeholder="Elegir",
                                        className="form-input",
                                        style={'width': '100%',
                                               'textAlign': 'left'}
                                    ),
                                ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-bottom': '15px'}),

                                # BANCO DE PREFERENCIA NUMERO  1  SOLES
                                html.Div
                                ([
                                    dbc.Label(
                                        "BANCO DE PREFERENCIA SOLES 1 (si cuentas con Interbank es preferible que elijas esta cuenta, si no eres de Perú marca otros y pon tu plataforma de pagos internacionales de preferencia)", className="form-label",
                                    ),
                                    dcc.Dropdown(
                                        id="form3-drop-banco",
                                        options=[
                                            {'label': 'BCP',
                                                'value': 'BCP'},
                                            {'label': 'Interbanck',
                                                'value': 'Interbanck'},
                                            {'label': 'Scotiabank',
                                                'value': 'Scotiabank'},
                                            {'label': 'BBVA',
                                                'value': 'BBVA'},
                                            {'label': 'Banco de la Nación',
                                                'value': 'Banco de la Nación'},
                                            {'label': 'BanBif',
                                                'value': 'BanBif'},
                                            {'label': 'Otro',
                                                'value': 'Otro'},
                                        ],
                                        clearable=False,
                                        placeholder="Elegir",
                                        className="form-input",
                                        style={'width': '100%',
                                               'textAlign': 'left'}
                                    ),
                                    html.Div(id='form3-option-banco')
                                ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-bottom': '15px'}),

                                # NÚMERO DE CUENTA EN SOLES
                                html.Div
                                ([
                                    dbc.Label(
                                        "NUMERO DE CUENTA SOLES (si no eres de Perú escribe tu correo asociado a tu plataforma de pagos)", className="form-label"
                                    ),
                                    dbc.Input(
                                        type="text", id="form3-num-cuenta", placeholder="Tu respuesta", className="form-input"
                                    ),
                                ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-bottom': '15px'}),

                                # NÚMERO DE CUENTA EN SOLES INTERBANCARIO
                                html.Div
                                ([
                                    dbc.Label(
                                        "NUMERO DE CUENTA INTERBANCARIA SOLES  (si no eres de Perú escribe tu correo asociado a tu plataforma de pagos)", className="form-label"
                                    ),
                                    dbc.Input(
                                        type="text", id="form3-num-cuenta-inter", placeholder="Tu respuesta", className="form-input"
                                    ),
                                ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-bottom': '15px'}),

                                # BANCO DE PREFERENCIA NUMERO 2 DOLARES
                                html.Div
                                ([
                                    dbc.Label(
                                        "BANCO DE PREFERENCIA DOLARES 2 (si cuentas con Interbank es preferible que elijas esta cuenta, si no eres de Perú marca otros y pon tu plataforma de pagos internacionales de preferencia)", className="form-label",
                                    ),
                                    dcc.Dropdown(
                                        id="form3-drop-banco-dolar",
                                        options=[
                                            {'label': 'BCP',
                                                'value': 'BCP'},
                                            {'label': 'Interbanck',
                                                'value': 'Interbanck'},
                                            {'label': 'Scotiabank',
                                                'value': 'Scotiabank'},
                                            {'label': 'BBVA',
                                                'value': 'BBVA'},
                                            {'label': 'Banco de la Nación',
                                                'value': 'Banco de la Nación'},
                                            {'label': 'BanBif',
                                                'value': 'BanBif'},
                                            {'label': 'Otro',
                                                'value': 'Otro'},
                                        ],
                                        clearable=False,
                                        placeholder="Elegir",
                                        className="form-input",
                                        style={'width': '100%',
                                               'textAlign': 'left'}
                                    ),
                                    html.Div(id='form3-option-banco-dolar')
                                ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-bottom': '15px'}),

                                # NÚMERO DE CUENTA EN DOLARES
                                html.Div
                                ([
                                    dbc.Label(
                                        "NUMERO DE CUENTA DOLARES (si no eres de Perú escribe tu correo asociado a tu plataforma de pagos)", className="form-label"
                                    ),
                                    dbc.Input(
                                        type="text", id="form3-num-cuenta-dolar", placeholder="Tu respuesta", className="form-input"
                                    ),
                                ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-bottom': '15px'}),

                                # NÚMERO DE CUENTA EN DOLARES INTERBANCARIO
                                html.Div
                                ([
                                    dbc.Label(
                                        "NUMERO DE CUENTA INTERBANCARIA DOLARES (si no eres de Perú escribe tu correo asociado a tu plataforma de pagos)", className="form-label"
                                    ),
                                    dbc.Input(
                                        type="text", id="form3-num-cuenta-dolar-inter", placeholder="Tu respuesta", className="form-input"
                                    ),
                                ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-bottom': '15px'}),

                                # SUBIR CV
                                html.Div
                                ([
                                    dbc.Label(
                                        "SUBIR CV (OPCIONAL)", className="form-label", id="form3-label-cv"
                                    ),
                                    dcc.Upload(
                                        id="form3-upload",
                                        children=html.Div(
                                            [" Agregar archivo"],
                                            className="form-input",
                                            style={"padding": "0 10px"}
                                        ), style={
                                            'lineHeight': '60px',
                                            'borderWidth': '1px',
                                            'borderStyle': 'dashed',
                                            'borderRadius': '5px',
                                            'textAlign': 'center',
                                            'pading': '10px',
                                            'cursor': 'pointer',
                                        }
                                    ),
                                    html.Div(id="form3-upload-result",)
                                ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-bottom': '15px'}
                                ),

                                # NOMBRE DE CONTACTO DE EMERGENCIA
                                html.Div
                                ([
                                    dbc.Label(
                                        "NOMBRE DE CONTACTO DE EMERGENCIA", className="form-label"
                                    ),
                                    dbc.Input(
                                        type="text", id="form3-nom-contac", placeholder="Tu respuesta", className="form-input"
                                    ),
                                ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-bottom': '15px'}),

                                # TELEFONO DE CONTACTO DE EMERGENCIA
                                html.Div
                                ([
                                    dbc.Label(
                                        "TELÉFONO DE CONTACTO DE EMERGENCIA", className="form-label"
                                    ),
                                    dbc.Input(
                                        type="text", id="form3-tel-contac", placeholder="Tu respuesta", className="form-input"
                                    ),
                                ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-bottom': '15px'}),


                            ], className="form-input-div"),


                            # Boton para retroceder, se cambia a enviar
                            html.Div
                            ([
                                dbc.Button
                                (
                                    "Volver", id="btn-volver-1", style={'margin-right': '10px', 'margin-bottom': '30px'}
                                ),
                                dbc.Button
                                (
                                    "Enviar", id="btn-send1", style={'margin-left': '10px', 'margin-bottom': '30px'}
                                ),
                            ]),

                            html.Div(id="pruebas-form")
                        ], style={'display': 'flex', 'flex-direction': 'column', 'padding': '0 20%', 'align-items': 'center'})
                    ]),
                ], justify='left'
            ),
        ],
    )
    return app_layout


def init_callbacks(app):
    # BOTON VOLVER
    @app.callback(Output("btn-volver-1", "href"), [Input("btn-volver-1", "n_clicks")])
    def back_to_index(n_clicks):
        if n_clicks:
            return "/edwin"
        else:
            return ""

    # Callback para ingresar el banco de tu preferencia  SOLES
    @app.callback(Output('form3-option-banco', 'children'), [Input('form3-drop-banco', 'value')])
    def value(value):
        if value == 'Otro':
            return dbc.Input(type="text", id="form3-banco-otro", placeholder="Escriba el banco de tu prefenrencia", className="form-input", style={'margin': '10px 0', 'width': '300px'}),
        else:
            return None

    # Callback para ingresar el banco de tu preferencia  DOLARES
    @app.callback(Output('form3-option-banco-dolar', 'children'), [Input('form3-drop-banco-dolar', 'value')])
    def value(value):
        if value == 'Otro':
            return dbc.Input(type="text", id="form3-banco-otro", placeholder="Escriba el banco de tu prefenrencia", className="form-input", style={'margin': '10px 0', 'width': '300px'}),
        else:
            return None
