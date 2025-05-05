from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('~/working/datasets/house_prices/Seattle_house_listings.csv')
app = Dash()

app.layout = [
    html.H1(children='Seattle house prices', style={'textAlign':'center'}),
    dcc.Dropdown(df.neighborhood.unique(), 'Parkwood', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
]

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.neighborhood==value]
    return px.line(dff, x='house_sqft', y='listed_price')

if __name__ == '__main__':
    app.run(debug=True)