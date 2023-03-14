import dash
from dash import html,dcc
import plotly.graph_objs as go
import pandas as pd

# load the example data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

# calculate EMA values
ema_20 = df['AAPL.Close'].ewm(span=20).mean()
ema_50 = df['AAPL.Close'].ewm(span=50).mean()

# create the candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'])])

# add the EMA lines
fig.add_trace(go.Scatter(x=df['Date'],
                y=ema_20,
                name='EMA 20',
                line=dict(color='orange', width=2)))

fig.add_trace(go.Scatter(x=df['Date'],
                y=ema_50,
                name='EMA 50',
                line=dict(color='blue', width=2)))

# set the layout
fig.update_layout(title='Candlestick Chart with 2 EMAs',
                  yaxis_title='Price')

# create the Dash app
app = dash.Dash(__name__)

# add the chart to the app layout
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

# run the app
if __name__ == '__main__':
    app.run_server(debug=True)