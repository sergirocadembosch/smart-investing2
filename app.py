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
            value=200000,
            id='price',
        ),
    
        html.Br(),
        html.Label('Upfront payment 000'),
        dcc.Slider(
            min=0,
            max=350000,
            step=10000,
            value=100000,
            id='upfront',
        ),

        html.Br(),
        html.Label('Maturity -years-'),
        dcc.Slider(
            min=0,
            max=30,
            step=1,
            value=30,
            id='maturity'
        ),

        html.Br(),
        html.Label('Type of rate'),
        dcc.RadioItems(['Fixed', 'Variable']),

        html.Br(),
        html.Label('Type -%-'),
        dcc.Slider(
            min=0,
            max=5,
            step=0.2,
            value=3,
            id='rate'
        ),

        html.Br(),
        html.Div(id='amount_due'),

        html.Br(),
        html.Div(id='montly_payment'),

    ], style={'padding': 10, 'flex': 1}),





], style={'display': 'flex', 'flex-direction': 'column'})




@app.callback(
   # Output(component_id='amount_due', component_property='children'),
    Output(component_id='montly_payment', component_property='children'),
    Input(component_id='price', component_property='value'),
    Input(component_id='upfront', component_property='value'),
    Input(component_id='maturity', component_property='value'),
    Input(component_id='rate', component_property='value'),
)


#(rate/12) * (1/(1-(1+rate/12)**(-months)))*P

def calculator(price, upfront, maturity, rate):
    #amount_due=upfront-price
    months=12*maturity
    P=price*(111/100)-upfront
    rate=rate/100
    montly_payment=(rate/12) * (1/(1-(1+rate/12)**(-months)))*P
    return f'montly_payment:{montly_payment}'
 


if __name__ == '__main__':
    app.run_server(debug=True)