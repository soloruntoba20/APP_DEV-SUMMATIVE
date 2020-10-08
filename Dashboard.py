import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pickle
import base64
import io

def get_dash(server):
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = dash.Dash(__name__,
                    server=server,
                    routes_pathname_prefix='/dashapp/',
                    external_stylesheets=external_stylesheets
                    )


    df = get_data()
    styles = get_styles()

    # import CVS into pandas

    df = pd.read_csv('solar_generation_data.csv')

    fig = go.Figure(df=[go.Scatter(x=['Day'], y=['Power Generated in MW'])])
    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )

    app.layout = html.Div([
        # html.H6("Change the value in the text box to see callbacks in action!"),
        html.A("Go to Home Page", href="/", style=styles["button_styles"]),
        html.Div("My Dashboard.", id='my-output',
                 style=styles["text_styles"]),
        html.Div(
            dcc.Graph(
                id='example-graph-2',
                figure=fig
            ),
            style=styles["fig_style"]
        )
    ])

    return app





def get_styles():
    """
    Very good for making the thing beautiful.
    """
    base_styles = {
        "text-align": "center",
        "border": "1px solid #ddd",
        "padding": "7px",
        "border-radius": "2px",
    }
    text_styles = {
        "background-color": "#eee",
        "margin": "auto",
        "width": "50%"
    }
    text_styles.update(base_styles)

    button_styles = {
        "text-decoration": "none",
    }
    button_styles.update(base_styles)

    fig_style = {
        "padding": "10px",
        "width": "80%",
        "margin": "auto",
        "margin-top": "5px"
    }
    fig_style.update(base_styles)
    return {
        "text_styles": text_styles,
        "base_styles": base_styles,
        "button_styles": button_styles,
        "fig_style": fig_style,
    }




