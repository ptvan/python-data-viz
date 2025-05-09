from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

DATA_URL = '~/working/datasets/house_prices/Seattle_house_listings.csv'

df = pd.read_csv(DATA_URL)
app = Dash()

app.layout = [
    html.H1(children='Seattle house prices', style = {'textAlign':'center'}),
    dcc.Dropdown(df.neighborhood.unique(), 'Parkwood', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
]

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)

def update_graph(value):
    dff = df[df.neighborhood == value]
    return px.scatter(dff, x = 'house_sqft', y = 'listed_price', facet_row="n_bedrooms")

if __name__ == '__main__':
    app.run(debug=True)