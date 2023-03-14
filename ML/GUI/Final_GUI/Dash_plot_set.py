from dash import Dash, html, dcc, Input, Output
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import sqlite3
import pandas as pd

conn = sqlite3.connect('share_V3.sqlite')
df_day = pd.read_sql("""SELECT spd."Date", spd.Open, spd.High, spd.Low, spd.Close, spd."Adj Close", spd.Volume, i.Symbol 
                     FROM Stock_price_day as spd 
                     INNER JOIN Information as i
                     ON i.SymbolId = spd.SymbolId;"""
                     ,conn)

df_hour = pd.read_sql("""SELECT sph."Datetime", sph.Open, sph.High, sph.Low, sph.Close, sph."Adj Close", sph.Volume, i.Symbol 
                     FROM Stock_price_hours as sph 
                     INNER JOIN Information as i
                     ON i.SymbolId = sph.SymbolId;"""
                     ,conn)

def get_stock_names():
    query = """SELECT DISTINCT i.Symbol FROM Stock_price_day as spd
                INNER JOIN Information as i on i.SymbolId = spd.SymbolId
                WHERE i.MarketId = 1
                ORDER BY i.Symbol ASC;"""
    cursor = conn.execute(query)
    stock_names = [row[0] for row in cursor.fetchall()]
    return stock_names

app = Dash()
timeframe_options = [{'label': 'Hour', 'value': '1H'},
                    {'label': 'Day', 'value': '1D'},
                    {'label': 'Week', 'value': '1W'},
                    {'label': 'Month', 'value': '1M'},
                    {'label': '3Month', 'value': '3M'}]
app.layout = html.Div([
                html.Div([
                    html.Label('Choose a stock:'),
                    dcc.Dropdown(id='stock_dropdown',
                                options=[{'label': stock, 'value': stock} for stock in get_stock_names()],
                                value=get_stock_names()[0], clearable=False),
                    dcc.Dropdown(id='timeframe-dropdown',
                                options=timeframe_options, value='1H', clearable=False),
                        ], style={'width': '100%', 'display': 'inline-block'}),
                dcc.Graph(id='candles')
            ])

@app.callback(Output('candles', 'figure'),
              [Input('stock_dropdown', 'value')],[Input('timeframe-dropdown', 'value')])
def update_candlestick_chart(value,timeframe):
    agg_dict = {'Open': 'first','High': 'max','Low': 'min','Close': 'last','Adj Close': 'last','Volume': 'sum'}
    if timeframe == '1H':
        df_plot = df_hour[(df_hour['Symbol'] == value)].tail(100)
        df_plot['Datetime'] = pd.to_datetime(df_plot['Datetime'])
        df_date = df_plot['Datetime']
    elif timeframe == '1D':
        df_plot = df_day[(df_day['Symbol'] == value)].tail(100)
        df_plot['Date'] = pd.to_datetime(df_plot['Date'])
        df_date = df_plot['Date']
    elif timeframe == '1W':
        df_plot = df_day[(df_day['Symbol'] == value)].tail(1000)
        df_plot['Date'] = pd.to_datetime(df_plot['Date'])
        df_plot.set_index('Date', inplace=True)
        df_plot = df_plot.resample('W').agg(agg_dict)
        df_date = df_plot.index
    elif timeframe == '1M':
        df_plot = df_day[(df_day['Symbol'] == value)]
        df_plot['Date'] = pd.to_datetime(df_plot['Date'])
        df_plot.set_index('Date', inplace=True)
        df_plot = df_plot.resample('M').agg(agg_dict)
        df_date = df_plot.index
    elif timeframe == '3M':
        df_plot = df_day[(df_day['Symbol'] == value)]
        df_plot['Date'] = pd.to_datetime(df_plot['Date'])
        df_plot.set_index('Date', inplace=True)
        df_plot = df_plot.resample('3M').agg(agg_dict)
        df_date = df_plot.index

    candles = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1
                            , subplot_titles=('Candlestick', 'Volume'), row_width=[0.5, 1])
    candles.add_trace(go.Candlestick(x=df_date,
                                         open=df_plot['Open'],
                                         high=df_plot['High'],
                                         low=df_plot['Low'],
                                         close=df_plot['Close']), row=1, col=1)

    candles.add_trace(go.Bar(x=df_date,y=df_plot['Volume'],), row=2, col=1)

    if timeframe == '1H':
        my_range = pd.date_range(start= min(df_plot['Datetime']), end= max(df_plot['Datetime']), freq='H')
        missing_datetime = my_range.difference(df_plot['Datetime']).strftime("%Y-%m-%d H%:m%:s%").tolist()
        candles.update_xaxes(rangebreaks=[dict(bounds=[17, 10], pattern="hour"),dict(values=missing_datetime, dvalue=3600000)])
    elif timeframe == '1D':
        my_range = pd.date_range(start= min(df_plot['Date']), end= max(df_plot['Date']), freq='D')
        missing_date = my_range.difference(df_plot['Date']).strftime("%Y-%m-%d").tolist()
        candles.update_xaxes(rangebreaks=[dict(bounds=["sat", "mon"]), dict(values=missing_date)])
    else:
        pass

    candles.update(layout_xaxis_rangeslider_visible=False)
    candles.update_xaxes(showticklabels=False)
    return candles

if __name__ == '__main__':
    app.run_server(debug=True, port=1000)