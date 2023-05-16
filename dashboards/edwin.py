import dash
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
from flask import request, session, render_template, send_file, json, make_response, render_template_string
from utils.utils_login import loginizer
from utils import utils, utils_google


def serve_layout():
    app = dash.Dash(__name__)
    index_login = html.Div(
        [
            dbc.Row(
                [html.H1("Solicitud de pagos Digitalia", id="title", style={"textAlign": "center"})], justify='center'
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Button("Formulario 1", id="btn-form-1",
                                        style={"margin-bottom": "5px"})
                        ]),
                ],
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Button("Formulario 2", id="btn-form-2",
                                        style={"margin-bottom": "5px"})
                        ]),
                ],
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Button("Formulario 3", id="btn-form-3",
                                        style={"margin-bottom": "5px"})
                        ]),
                ],
            ),

        ], style={"textAlign": "center"}, className="dash-inside-container")
    return index_login


app = serve_layout()


def init_callbacks(app):
    @app.callback(Output("url", 'pathname'), [Input('btn-form-1', 'n_clicks')], Input('btn-form-2', 'n_clicks'), Input('btn-form-3', 'n_clicks'), prevent_initial_call=True)
    def redirect_to_formu(btn1, btn2, btn3):
        if btn1:
            return '/formu'
        elif btn2:
            return '/formulario2'
        elif btn3:
            return '/formulario3'
        else:
            return '/edwin'
