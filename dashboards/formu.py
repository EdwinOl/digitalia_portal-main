import dash
import dash_bootstrap_components as dbc
# import dash_core_components as dcc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
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
                                html.Label("¡Hola! Por favor, si trabajas con nosotros llena este formulario para poder depositarte de la manera más rápida posible.", style={
                                    'font-size': '15px', 'margin-Bottom': '0', 'text-align': 'initial'}),
                                html.Label("Son datos necesarios que necesitamos tener para poder generar el abono.", style={
                                    'font-size': '15px'}),
                                html.Label("Gracias"),
                                html.Br(),

                                # Ingreso de datos
                                dbc.Label
                                (
                                    "Ingresa tu correo electrónico", className="form-label", id="form-email-label-formu"
                                ),
                                dbc.Input
                                (
                                    type="email", id="form-email-formu", placeholder="Tu dirección de correo electrónico", style={'margin-bottom': '10px'}, className="form-input"
                                ),

                                dbc.Label
                                (
                                    "Selecciona tu Nombre de la Lista o Marca: No estoy aquí", className="form-label", id="form-email-label-formu"
                                ),
                                dcc.Dropdown(
                                    options=[
                                        {'label': 'Opción 1', 'value': 1},
                                        {'label': 'Opción 2', 'value': 2}
                                    ],
                                    placeholder="Seleccione una opcion",
                                    className="form-input",
                                    style={'width': '100%',
                                           'textAlign': 'left'}
                                ),

                            ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-bottom': '15px'}, className="form-input-div"),


                            # Boton para retroceder, se cambia a enviar
                            html.Div
                            ([
                                dbc.Button
                                (
                                    "Volver", id="btn-volver1", style={'margin-right': '10px'}
                                ),
                                dbc.Button
                                (
                                    "Enviar", id="btn-send", style={'margin-left': '10px'}
                                ),
                            ]),
                        ], style={'display': 'flex', 'flex-direction': 'column', 'padding': '0 25%', 'align-items': 'center'})
                    ]),
                ], justify='left'
            ),
        ], style={"textAlign": "center", "width": "100%"}
    )
    return app_layout


def init_callbacks(app):
    @app.callback(Output("btn-volver1", "href"), [Input("btn-volver1", "n_clicks")])
    def back_to_index(n_clicks):
        if n_clicks:
            return "/edwin"
        else:
            return ""
