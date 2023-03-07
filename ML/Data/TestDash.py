import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd

# Load data
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")

# Create subplots
fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.05)

# Add candlestick chart
fig.add_trace(go.Candlestick(x=df['Date'],
                             open=df['AAPL.Open'],
                             high=df['AAPL.High'],
                             low=df['AAPL.Low'],
                             close=df['AAPL.Close'],
                             name='Candlestick'),
              row=1, col=1)

# Add volume chart
fig.add_trace(go.Bar(x=df['Date'],
                     y=df['AAPL.Volume'],
                     name='Volume'),
              row=2, col=1)

# Update layout
fig.update_layout(height=600, title_text="Candlestick and Volume Chart")

# Create Dash app
app = dash.Dash(__name__)

# Define dropdown options
dropdown_options = [{'label': 'Hour', 'value': '1H'},
                    {'label': 'Day', 'value': '1D'},
                    {'label': 'Week', 'value': '1W'},
                    {'label': 'Month', 'value': '1M'}]

# Define app layout
app.layout = html.Div(children=[
    html.Label('Select timeframe:'),
    dcc.Dropdown(id='timeframe-dropdown', options=dropdown_options, value='1H', clearable=False),
    dcc.Graph(id='graph', figure=fig),
    html.Br(),
])

# Define callback to update chart based on dropdown selection
@app.callback(Output('graph', 'figure'),
              [Input('timeframe-dropdown', 'value')])
def update_chart(timeframe):
    # Filter data based on selected timeframe
    if timeframe == '1H':
        df_filtered = df[-252:]
    elif timeframe == '1D':
        df_filtered = df[-126:]
    elif timeframe == '1W':
        df_filtered = df[-63:]
    elif timeframe == '1M':
        df_filtered = df[-21:]
    
    # Create new chart based on filtered data
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.05)
    fig.add_trace(go.Candlestick(x=df_filtered['Date'],
                                 open=df_filtered['AAPL.Open'],
                                 high=df_filtered['AAPL.High'],
                                 low=df_filtered['AAPL.Low'],
                                 close=df_filtered['AAPL.Close'],
                                 name='Candlestick'),
                  row=1, col=1)
    fig.add_trace(go.Bar(x=df_filtered['Date'],
                         y=df_filtered['AAPL.Volume'],
                         name='Volume'),
                  row=2, col=1)
    fig.update(layout_xaxis_rangeslider_visible=False)
    
    return fig

# Run app
if __name__ == '__main__':
    app.run_server(debug=True, port=8000)
