import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
from flask import request, session
from utils.utils_login import loginizer


def serve_layout():
    app_layout = html.Div(
        [
            dbc.Row(
                [html.H1("Solicitud de pagos Digitalia", id="title", style={"textAlign": "center"})], justify='center'
            ),
            dbc.Row(
                [
                    dbc.Col
                    ([
                        dbc.Form
                        ([
                            html.Div
                            ([
                                # Aviso
                                html.H4("Sobre el proyecto", style={
                                    'font-size': '30px', 'margin-Bottom': '10px', 'text-align': 'initial'}),

                                # Descripcion del servicio
                                html.Div
                                ([
                                    dbc.Label(
                                        "Descripción del Servicio que estás prestando", className="form-label", style={'line-height': '0.1'}
                                    ),
                                    dbc.Label(
                                        "Si son varios servicios, indica en la descripción que monto está asociado a que proyecto.", className="form-label"),
                                    dbc.Input(
                                        type="text", id="form2-des", placeholder="Tu respuesta", className="form-input"
                                    ),
                                ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-bottom': '30px'}),

                                # Proyecto en donde trabajas
                                html.Div
                                ([
                                    dbc.Label(
                                        "Proyecto en el que trabajas", className="form-label", id="form2-proy", style={'line-height': '0.1'}
                                    ),
                                    dbc.Label(
                                        "Si son varios servicios, indica en la descripción que monto está asociado a que proyecto.", className="form-label"
                                    ),
                                    dcc.Dropdown(
                                        id="form2-drop-proy",
                                        options=[
                                            {'label': 'Proyecto 1',
                                                'value': 'Proyecto 1'},
                                            {'label': 'Proyecto 2',
                                                'value': 'Proyecto 2'},
                                            {'label': 'Proyecto 3',
                                                'value': 'Proyecto 3'}
                                        ],
                                        placeholder="Elegir",
                                        className="form-input",
                                        style={'width': '100%',
                                               'textAlign': 'left'}
                                    ),
                                ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-bottom': '10px'}),

                                # Reembolso o pago por servicio
                                html.Div
                                ([
                                    dbc.Label(
                                        "¿Es un reembolso, pago por servicio o rendición?", className="form-label", id="form2-rem"
                                    ),
                                    dcc.Dropdown(
                                        id="form2-drop-pago",
                                        options=[
                                            {'label': 'Pago por servicio',
                                                'value': 'Pago por servicio'},
                                            {'label': 'Reembolso',
                                                'value': 'Reembolso'}
                                        ],
                                        placeholder="Elegir",
                                        className="form-input",
                                        style={'width': '100%',
                                               'textAlign': 'left'}
                                    ),
                                ], style={'text-align': 'initial', 'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-bottom': '10px'}),

                                # Proyect trabajas
                                html.Div
                                ([
                                    dbc.Label(
                                        "Con que project trabajas", className="form-label", id="form2-proyect"
                                    ),

                                    dcc.Dropdown(
                                        id="form2-drop-project",
                                        options=[
                                            {'label': 'Adrián Torrejón',
                                                'value': 'Adrián Torrejón'},
                                            {'label': 'César Cortez',
                                                'value': 'César Cortez'},
                                            {'label': 'Raul del Mar',
                                                'value': 'Raul del Mar'}
                                        ],
                                        placeholder="Elegir",
                                        className="form-input",
                                        style={'width': '100%',
                                               'textAlign': 'left'}
                                    ),
                                ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-bottom': '30px'}),

                                # Moneda
                                html.Div
                                ([
                                    dbc.Label(
                                        "Tipo de moneda", className="form-label", id="form2-moneda"
                                    ),
                                    dcc.Dropdown(
                                        id="form2-drop-moneda",
                                        options=[
                                            {'label': 'Soles S/',
                                                'value': 'Soles S/'},
                                            {'label': 'Dolares $',
                                                'value': 'Dolares $'}
                                        ],
                                        placeholder="Elegir",
                                        className="form-input",
                                        style={'width': '100%',
                                               'textAlign': 'left'}
                                    ),
                                ], style={'text-align': 'initial', 'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-bottom': '10px'}),

                                # Monto a pagar
                                html.Div
                                ([
                                    dbc.Label(
                                        "Monto a pagar", className="form-label", id="form2-monto"
                                    ),
                                    dbc.Input(
                                        type="text", id="form2-monto", placeholder="Tu respuesta", className="form-input"
                                    ),
                                ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-bottom': '30px'}),

                                # Retencion de impuestos
                                html.Div
                                ([
                                    dbc.Label(
                                        "¿Aplica retención a Impuesto a la Renta? (solo para Recibo por honorario)", className="form-label", id="form2-retencion"
                                    ),
                                    dcc.Dropdown(
                                        id="form2-drop-retencion",
                                        options=[
                                            {'label': 'Si', 'value': 'Si'},
                                            {'label': 'No', 'value': 'No'},
                                            {'label': 'No lo se',
                                                'value': 'No lo se'}
                                        ],
                                        placeholder="Elegir",
                                        className="form-input",
                                        style={'width': '100%',
                                               'textAlign': 'left'}
                                    ),
                                ], style={'text-align': 'initial', 'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-bottom': '30px'}),

                                # recibo
                                html.Div
                                ([
                                    dbc.Label(
                                        "Sube tu recibo o factura", className="form-label", id="form2-label-recibo", style={'line-height': '0.1'}
                                    ),
                                    dbc.Label(
                                        "Emitir a: DIGITALIA TEC S.A.C | RUC: 20608189310", className="form-label", id="form2-label-recibo2"
                                    ),
                                    dcc.Upload(
                                        id="form2-upload",
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
                                    html.Div(
                                        id="form2-upload-result",

                                    ),

                                ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-bottom': '30px'}),


                            ], className="form-input-div"),


                            # Boton para retroceder, se cambia a enviar
                            html.Div
                            ([
                                dbc.Button
                                (
                                    "Volver", id="btn-volver", style={'margin-right': '10px'}
                                ),
                                dbc.Button
                                (
                                    "Enviar", id="btn-send", style={'margin-left': '10px'}
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
    @app.callback(Output("btn-volver", "href"), [Input("btn-volver", "n_clicks")])
    def back_to_index(n_clicks):
        if n_clicks:
            return "/edwin"
        else:
            return ""

    # un callbacks si el filename del upload es diferente a vacio, el div muestra el file con el nombre
    @app.callback(Output("form2-upload-result", "children"), Input("form2-upload", "filename"))
    def filename(filename):
        if filename is None:
            return "Por favor suba el archivo"
        else:
            return f"Se subió el archivo {filename}"

    # un callbacks si el filename del upload es diferente a vacio, el div muestra el file con el nombre
    @app.callback(Output("pruebas-form", "children"), Input("btn-send", "n_clicks"), State("form2-des", "value"), State("form2-drop-proy", "value"), State("form2-drop-pago", "value"), State("form2-drop-project", "value"), State("form2-drop-moneda", "value"), State("form2-monto", "value"), State("form2-drop-retencion", "value"))
    def read_values(n_clicks, value_des, value_proy, value_pago, value_project, value_tipomoneda, value_monto, value_retencion):
        return f"Valores: {value_des},{value_proy},{value_pago}, {value_project},{value_tipomoneda}, {value_monto}, {value_retencion}"

    # Todo el form para los 3 formularios
