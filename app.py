# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Output, Input

app = Dash(__name__)

app.layout = html.Div([


    html.Div(children=[
    
        html.Br(),
        html.Label('Price 000'),
        dcc.Slider(
            min=0,
            max=350000,
            step=10000,
            tooltip={"placement": "bottom", "always_visible": True},
            value=240000,
            id='price',
        ),
    
        html.Br(),
        html.Label('Upfront payment 000'),
        dcc.Slider(
            min=0,
            max=350000,
            step=10000,
            value=80000,
        ),

        html.Br(),
        html.Label('Maturity -years-'),
        dcc.Slider(
            min=0,
            max=30,
            step=1,
            value=25,
        ),

        html.Br(),
        html.Label('Type of rate'),
        dcc.RadioItems(['Fixed', 'Variable']),

        html.Br(),
        html.Label('Tipo'),
        dcc.Input(value='MTL', type='number'),

        html.Br(),
        html.Div(id='my-output'),



    ], style={'padding': 10, 'flex': 1}),





], style={'display': 'flex', 'flex-direction': 'column'})




@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='price', component_property='value')
)
def update_output_div(input_value):
    return f'Amount due: {input_value}'


if __name__ == '__main__':
    app.run_server(debug=True)