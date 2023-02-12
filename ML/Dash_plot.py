from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import sqlite3

import pandas as pd
import numpy as np
import pandas_ta as ta

#---------------------------------------Connect Database----------------------------------------#
conn = sqlite3.connect('share.sqlite')
cursor = conn.cursor()
df = pd.read_sql("""SELECT SP."Date",SP.Open,Sp.High,SP.Low,SP.Close,SP."Adj Close",SP.Volume,I.Symbol 
                FROM Stock_price_day as SP 
                INNER JOIN Information as I 
                on I.SymbolId = SP.SymbolId 
                WHERE I.Symbol = 'KBANK';   
                """,conn)
conn.close()
df = df.tail(100)
#---------------------------------------Connect Database----------------------------------------#

#---------------------------------------Check missing date----------------------------------------#
df['Date'] = pd.to_datetime(df['Date'])
my_range = pd.date_range(start= min(df['Date']), end= max(df['Date']), freq='D')
missing_date = my_range.difference(df['Date']).strftime("%Y-%m-%d").tolist()
#---------------------------------------Check missing date----------------------------------------#

#---------------------------------------resample----------------------------------------#
agg_dict = {'Open': 'first','High': 'max','Low': 'min','Close': 'last','Adj Close': 'last','Volume': 'sum'}
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
re_df1d = df.resample('D').agg(agg_dict)

new_df1d = re_df1d.dropna()
new_df1d_index = new_df1d.index.strftime("%Y.%m.%d %H:%M:%S")

# new_df1d['rsi'] = ta.rsi(new_df1d['Close'].astype(float))
#---------------------------------------resample----------------------------------------#

app = Dash()

app.layout = html.Div([

    dcc.Graph(id='candles'), 
    dcc.Graph(id='indicator'), 

    dcc.Interval(id='interval', interval = 2000),
    ])

@app.callback(
    Output('candles', 'figure'),
    Output('indicator', 'figure'),
    Input('interval', 'n_intervals')
)
def update_figure(n_intervals):

    candles = go.Figure(
        data = [
            go.Candlestick(
                x=new_df1d_index,
                open=new_df1d['Open'],
                high=new_df1d['High'],
                low=new_df1d['Low'],
                close=new_df1d['Close']
            )])

    # indicator = px.line(x=new_df1d_index, y=new_df1d['rsi'])

    candles.update_xaxes(showticklabels=False)
    candles.update(layout_xaxis_rangeslider_visible=False)
    # indicator.update_xaxes(showticklabels=False)

    return candles

if __name__ == '__main__':
    app.run_server(debug=True)