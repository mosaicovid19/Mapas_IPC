# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 17:21:55 2020

@author: pchir
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import json
import pathlib
import os

import plotly
import plotly.express as px


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


#get relative data folder
PATH = os.getcwd()
PATH = pathlib.Path(PATH)
DATA_PATH = PATH.joinpath('data').resolve()

lati = [-3.78300,-3.78300,-22.9146,-25.4784,-23.6489]
long = [-38.5434,-38.5434,-43.4461,-49.2733,-46.6388]
zoom = [11,11,10,10,9]

state = ["a","a","b","c","d"]

for x in range(1,5):
    MAP_ESTADO = "".join([state[x],".geojson"]) #'mapfortaleza.geojson' #ok
    with open(DATA_PATH.joinpath(MAP_ESTADO), encoding='utf-8') as shapefile:
        Estado_geojson = json.load(shapefile)
        Estado = "".join([state[x],".csv"]) #'IPC_FORTALEZA.csv'
        ipc_long = pd.read_csv(DATA_PATH.joinpath('processed', Estado), encoding='utf-8', na_values='na')
        fig = px.choropleth_mapbox(ipc_long, geojson=Estado_geojson, color='IPC',
                           color_continuous_scale=px.colors.sequential.OrRd,
                            locations= 'NOME', featureidkey="properties.NOME",
                             center={"lat": lati[x], 'lon': long[x]}, # lati long
                           mapbox_style="carto-positron", zoom=zoom[x],
                           labels={
                     "Class_IPC": "Classificação IPC",
                     "NOME": "Bairro"
                 },
                title=" ".join([state[x],"IPC"]))
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        fig_NOME = "".join([state[x],".html"])#"ipcFortaleza.html"
        plotly.offline.plot(fig, filename="\\".join([os.getcwd(),fig_NOME]))
        
