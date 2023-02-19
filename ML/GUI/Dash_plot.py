from dash import Dash, html, dcc, Input, Output
import plotly.graph_objs as go
import sqlite3
import pandas as pd

conn = sqlite3.connect('newshare.sqlite')

def get_stock_names():
    query = """SELECT DISTINCT Symbol 
                FROM Stock_price_day as SP 
                INNER JOIN Information as I 
                on I.SymbolId = SP.SymbolId"""
    cursor = conn.execute(query)
    stock_names = [row[0] for row in cursor.fetchall()]
    return stock_names

df = pd.read_sql("""SELECT SP."Date", SP.Open, SP.High, SP.Low, SP.Close, SP."Adj Close", SP.Volume, I.Symbol 
                     FROM Stock_price_day as SP 
                     INNER JOIN Information as I 
                     ON I.SymbolId = SP.SymbolId;"""
                     ,conn)

app = Dash()

app.layout = html.Div([
    html.Div([
        html.Label('Choose a stock:'),
        dcc.Dropdown(
            id='stock_dropdown',
            options=[{'label': stock, 'value': stock} for stock in get_stock_names()],
            value=get_stock_names()[0]
        ),
    ], style={'width': '30%', 'display': 'inline-block'}),
    dcc.Graph(id='candles')
])

@app.callback(Output('candles', 'figure'),Input('stock_dropdown', 'value'))
def update_candlestick_chart(value):
    
    df_plot = df[(df['Symbol'] == value)].tail(100)

    my_range = pd.date_range(start= min(df_plot['Date']), end= max(df_plot['Date']), freq='D')
    missing_date = my_range.difference(df_plot['Date']).strftime("%Y-%m-%d").tolist()

    candles = go.Figure(data=[go.Candlestick(x=df_plot['Date'],
                                         open=df_plot['Open'],
                                         high=df_plot['High'],
                                         low=df_plot['Low'],
                                         close=df_plot['Close'])])

    candles.update_xaxes(
    rangebreaks=[
        dict(bounds=["sat", "mon"]), dict(values=missing_date)])
    candles.update(layout_xaxis_rangeslider_visible=False)

    return candles

if __name__ == '__main__':
    app.run_server(debug=True)