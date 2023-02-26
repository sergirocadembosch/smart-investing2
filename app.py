# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc

app = Dash(__name__)

app.layout = html.Div([


    html.Div(children=[
    
        html.Br(),
        html.Label('Price 000'),
        dcc.Slider(
            min=0,
            max=350000,
            step=10000,
            #marks={i: f'Label {i}' if i == 1 else str(i) for i in range(1, 350)},
            tooltip={"placement": "bottom", "always_visible": True},
            value=240000,
        ),
    
        html.Br(),
        html.Label('Upfront payment 000'),
        dcc.Slider(
            min=0,
            max=350000,
            step=10000,
            # marks={i: f'Label {i}' if i == 1 else str(i) for i in range(1, 350)},
            value=80000,
        ),

        html.Br(),
        html.Label('Maturity -years-'),
        dcc.Slider(
            min=0,
            max=30,
            step=1,
            # marks={i: f'Label {i}' if i == 1 else str(i) for i in range(1, 350)},
            value=25,
        ),

        # html.Label('Dropdown'),
        # dcc.Dropdown(['New York City', 'Montréal', 'San Francisco'], 'Montréal'),

        # html.Br(),
        # html.Label('Multi-Select Dropdown'),
        # dcc.Dropdown(['New York City', 'Montréal', 'San Francisco'],
        #              ['Montréal', 'San Francisco'],
        #              multi=True),

        html.Br(),
        html.Label('Type of rate'),
        dcc.RadioItems(['Fixed', 'Variable']),

        html.Br(),
        html.Label('Tipo'),
        dcc.Input(value='MTL', type='number'),



    ], style={'padding': 10, 'flex': 1}),

    # html.Div(children=[
    #     html.Label('Checkboxes'),
    #     dcc.Checklist(['New York City', 'Montréal', 'San Francisco'],
    #                   ['Montréal', 'San Francisco']
    #     ),

    #     html.Br(),
    #     html.Label('Text Input'),
    #     dcc.Input(value='MTL', type='text'),

    #     html.Br(),
    #     html.Label('Slider'),
    #     dcc.Slider(
    #         min=0,
    #         max=9,
    #         marks={i: f'Label {i}' if i == 1 else str(i) for i in range(1, 6)},
    #         value=5,
    #     ),
    # ], style={'padding': 10, 'flex': 1})



], style={'display': 'flex', 'flex-direction': 'column'})



if __name__ == '__main__':
    app.run_server(debug=True)