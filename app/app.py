# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
 
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import json
import pathlib

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath('data').resolve()

#### load data #####
# Rio geojson
with open(DATA_PATH.joinpath('mapfortaleza.geojson'), encoding='utf-8') as shapefile:
    rio_geojson = json.load(shapefile)


# Rio IPC 
rio_ipc_long = pd.read_csv(DATA_PATH.joinpath('processed', 'IPC_FORTALEZA.csv'), encoding='utf-8', na_values='na')


import plotly.express as px
fig = px.choropleth_mapbox(rio_ipc_long, geojson=rio_geojson, color='Class_IPC',
                            color_discrete_sequence=["#43f1fa", "#00a2e8", "#1013d8", "#12527a", "#000062"],
                            locations= 'NOME', featureidkey="properties.NOME",
                        #    center={"lat": -22.9146, 'lon': -43.4461}, #RIO
                        #    center={"lat": -23.5489, 'lon': -46.6388}, #SP
                        #    center={"lat": -25.4284, 'lon': -49.2733}, #Curitiba
                             center={"lat": -3.71839, 'lon': -38.5434}, #Fortaleza
                           mapbox_style="carto-positron", zoom=9,
                           labels={
                     "Class_IPC": "Classificação IPC",
                     "NOME": "Bairro"
                 },
                title="Mapa IPC São Paulo")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# fig.show()

app.layout = html.Div(
#     children=[
#     html.H1(children='Mapa IPC Rio de Janeiro'),

#     html.Div(children='''
        
#     '''),

#     dcc.Graph(
#         id='example-graph',
#         figure=fig
#     )
# ])
[
            # language select
            # html.Div(
            #     [
            #         # Load in a new tab because some figures do not resize properly otherwise
            #         # TODO: Fix this bug
            #         html.A([labels['language0']], href=labels['language_link0'], target='_blank', className='lang-link'),
            #         html.A([labels['language1']], href=labels['language_link1'], target='_blank', className='lang-link'),
            #         html.A([labels['language2']], href=labels['language_link2'], target='_blank', className='lang-link'),
            #     ],
            #     id='language-container',
            # ),

            # page title
            html.Div(
                [
                    # title
                    html.H3(
                        ['title'],
                        id='title',
                        ),
                    #subtitle
                    html.H6(
                        ['subtitle'],
                        id='subtitle',
                    ),
                ],
                id='title-container',
            ),

            # mini info boxes
            # html.Div(
            #     [
            #         html.Div(
            #             [html.H3(latest_cases_rj, id='cases_rj_text'),
            #              html.P([labels['cases_Rio_de_Janeiro_label']], id='cases_Rio_de_Janeiro_label')],
            #             id='cases_rj',
            #             className='mini_container',
            #         ),
            #         html.Div(
            #             [html.H3(latest_deaths_rj, id='deaths_rj_text'),
            #              html.P([labels['deaths_Rio_de_Janeiro_label']], id='deaths_Rio_de_Janeiro_label')],
            #             id='deaths_rj',
            #             className='mini_container',
            #         ),
            #         html.Div(
            #             [html.H3(latest_recovered_rj, id='recovered_rj_text'),
            #              html.P([labels['recovered_rj_label']], id='recovered_rj_label')],
            #             id='recovered_rj',
            #             className='mini_container',
            #         ),
            #         html.Div(
            #             [html.H3(latest_letal_rj, id='letal_rj_text'),
            #              html.P([labels['letal_rj_label']], id='letal_rj_label')],
            #             id='letal_rj',
            #             className='mini_container',
            #         ),
            #     ],
            #     id='info-container'
            # ),

            # 1st row: two boxes
            html.Div(
                [
                    # left box
                   # html.Div(
                    #     [
                    #         dcc.Markdown([labels['infobox']], id='')
                    #     ],
                    #     className='grid-item',
                    #     id='infobox_container',
                    # ),
                    # right box 

                    
                    html.Div(
                        [
                            html.H6(
                                ['Rio_de_Janeiro_map_label'],
                            ),

                            dcc.Graph(
                                figure=fig,
                                id='Rio_de_Janeiro_map'
                                # responsive=True,
                                # config={
                                #     'modeBarButtonsToRemove': [
                                #         'select2d',
                                #         'lasso2d',
                                #         'hoverClosestGeo',
                                #         ],
                                #     'scrollZoom' : True
                                #     }
                                ),
                        ],
                        className='grid-item'
                    ),
                ],
                className='grid-container-onethird-twothirds-cols',
            ),

            # 2nd row: 2 boxes
            # html.Div(
            #     [
            #         # left box
            #         html.Div(
            #             [

            #                 html.H6(
            #                     [labels['total_cases_label']],
            #                 ),
            #                 dcc.Graph(
            #                     figure=cases_fig,
            #                     id='cases_fig',
            #                     responsive=True,
            #                     config={
            #                         'modeBarButtonsToRemove': modebar_buttons_to_remove,
            #                     }
            #                 ),
            #             ],
            #             className='grid-item'
            #         ),

            #         # left box
            #         html.Div(
            #             [

            #                 html.H6(
            #                     [labels['deaths_fig_label']],
            #                 ),
            #                 dcc.Graph(
            #                     figure=deaths_fig,
            #                     id='deaths_fig',
            #                     responsive=True,
            #                     config={
            #                         'modeBarButtonsToRemove': modebar_buttons_to_remove,
            #                     }
            #                 ),
            #             ],
            #             className='grid-item'
            #         ),
            #     ],
            #     className='grid-container-two-cols',
            #     ),

            # 3rd row: 3 boxes
            # html.Div(
            #     [
            #         # left box
            #         html.Div(
            #             [

            #                 html.H6(
            #                     [labels['deaths_fig_label']],
            #                 ),
            #                 dcc.Graph(
            #                     figure=deaths_fig,
            #                     id='deaths_fig',
            #                     responsive=True,
            #                     config={
            #                         'modeBarButtonsToRemove': modebar_buttons_to_remove,
            #                     }
            #                 ),
            #             ],
            #             className='grid-item'
            #         ),
            #         # middle box
            #         html.Div(
            #             [
            #                 html.H6(
            #                     [labels['total_hospitalisations_label']]
            #                 ),
            #                 dcc.Graph(
            #                     figure=hospitalisations_qc_fig,
            #                     id='hospitalisations_qc_fig',
            #                     responsive=True,
            #                     config={
            #                         'modeBarButtonsToRemove': modebar_buttons_to_remove,
            #                     }
            #                 ),
            #             ],
            #             className='grid-item'
            #         ),
            #         # right box
            #         html.Div(
            #             [
            #                 html.H6(
            #                     [labels['total_testing_label']],
            #                 ),
            #                 dcc.Graph(
            #                     figure=testing_qc_fig,
            #                     id='testing_qc_fig',
            #                     responsive=True,
            #                     config={
            #                         'modeBarButtonsToRemove': modebar_buttons_to_remove,
            #                     }
            #                 ),
            #             ],
            #             className='grid-item'
            #         ),
            #     ],
            #     className='grid-container-three-cols',
            # ),

            # 4th row: 2 boxes
            # html.Div(
            #     [
            #         # left box
            #         html.Div(
            #             [

            #                 html.H6(
            #                     [labels['deaths_loc_fig_mtl_label']],
            #                 ),
            #                 dcc.Graph(
            #                     figure=deaths_loc_mtl_fig,
            #                     id='deaths_loc_fig_mtl',
            #                     responsive=True,
            #                     config={
            #                         'modeBarButtonsToRemove': modebar_buttons_to_remove,
            #                     }
            #                 ),
            #             ],
            #             className='grid-item'
            #         ),
            #         # right box
            #         html.Div(
            #             [
            #                 html.H6(
            #                     [labels['deaths_loc_fig_qc_label']],
            #                 ),
            #                 dcc.Graph(
            #                     figure=deaths_loc_qc_fig,
            #                     id='deaths_loc_fig_qc',
            #                     responsive=True,
            #                     config={
            #                         'modeBarButtonsToRemove': modebar_buttons_to_remove,
            #                     }
            #                 ),
            #             ],
            #             className='grid-item'
            #         ),
            #     ],
            #     className='grid-container-two-cols',
            # ),

            # footer
            html.Div([
                html.Div([
                    dcc.Markdown(['footer_left']),
                ],
                id='footer-left',
                className='footer-item'
                ),
                html.Div([
                    dcc.Markdown(['footer_centre']),
                ],
                id='footer-centre',
                className='footer-item'
                ),
                html.Div([
                    dcc.Markdown(['footer_right']),
                ],
                id='footer-right',
                className='footer-item'
                )
            ],
            id='footer'
            )

        ],
        id='main-container'
    )

if __name__ == '__main__':
    app.run_server(debug=True)
