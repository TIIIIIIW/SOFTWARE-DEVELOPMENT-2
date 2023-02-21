import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import sqlite3

# Load the data
conn = sqlite3.connect('newshare.sqlite')

df = pd.read_sql("""SELECT SP."Date", SP.Open, SP.High, SP.Low, SP.Close, SP."Adj Close", SP.Volume, I.Symbol 
                     FROM Stock_price_day as SP 
                     INNER JOIN Information as I 
                     ON I.SymbolId = SP.SymbolId
                     WHERE Symbol = 'KBANK';"""
                     ,conn)

# Define the app
app = Dash(__name__)

# Define the layout
app.layout = html.Div(children=[
    html.H1(children='Candlestick with Volume'),

    dcc.Graph(
        id='candlestick-volume',
        figure={
            'data': [],
            'layout': {
                'title': 'Candlestick with Volume',
                'yaxis': {'title': 'Price'},
                'yaxis2': {'title': 'Volume', 'overlaying': 'y', 'side': 'right'},
                'xaxis': {'title': 'Date'}
            }
        }
    )
])

# Define the callback
@app.callback(Output('candlestick-volume', 'figure'), [Input('candlestick-volume', 'relayoutData')])
def update_graph(relayoutData):
    # Define the figure
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.05)

    # Add the candlestick chart
    fig.add_trace(go.Candlestick(x=df['Date'],
                                 open=df['Open'],
                                 high=df['High'],
                                 low=df['Low'],
                                 close=df['Close'],
                                 name='Candlestick'), row=1, col=1)

    # Add the volume chart
    fig.add_trace(go.Bar(x=df['Date'],
                         y=df['Volume'],
                         name='Volume'), row=2, col=1)

    # Update the layout
    fig.update_layout(title='Candlestick with Volume',
                      yaxis=dict(title='Price'),
                      yaxis2=dict(title='Volume', overlaying='y', side='right'),
                      xaxis=dict(title='Date'))

    # Apply the relayoutData
    if relayoutData:
        fig.update_layout(relayoutData=relayoutData)

    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)