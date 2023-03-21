from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QMainWindow
from plotly.graph_objects import Figure, Scatter
import plotly
import sqlite3
import pandas as pd
import plotly.express as px
# import geopandas as gpd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        # create data
        conn = sqlite3.connect(r'C:\Users\Admin\Desktop\SOFTDEV2\SOFTWARE-DEVELOPMENT-2\share_V3.sqlite')
        df_day = pd.read_sql("""SELECT spd."Date", spd.Open, spd.High, spd.Low, spd.Close, spd."Adj Close", spd.Volume, i.Symbol 
                            FROM Stock_price_day as spd 
                            INNER JOIN Information as i
                            ON i.SymbolId = spd.SymbolId
                            WHERE i.Symbol = 'ADVANC.BK'
                            ORDER BY spd."Date" ASC;"""
                            ,conn)
        
        df_hour = pd.read_sql("""SELECT sph."Datetime", sph.Open, sph.High, sph.Low, sph.Close, sph."Adj Close", sph.Volume, i.Symbol 
                     FROM Stock_price_hours as sph 
                     INNER JOIN Information as i
                     ON i.SymbolId = sph.SymbolId
                     ORDER BY sph."Datetime" ASC;"""
                     ,conn)
        
        df_roaroe = pd.read_sql("""SELECT fq.ROA,fq.ROE,fq.Period FROM Financial_quarterly as fq
                            INNER JOIN Information as i ON i.SymbolId = fq.SymbolId
                            WHERE i.Symbol = 'AAVL'
                            ORDER BY i.Symbol ASC;"""
                     ,conn)

        fig = make_subplots(rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.1
                            , subplot_titles=('Candlestick', 'Volume', 'ROA/ROE'), row_width=[1, 1, 1])
        fig.add_trace(go.Candlestick(x=df_day['Date'],open=df_day['Open'],
                                    high=df_day['High'],low=df_day['Low'],
                                    close=df_day['Close'], name='ADVANC.BK'), row=1, col=1)
        fig.add_trace(go.Bar(x=df_day['Date'],y=df_day['Volume'], name='Volume'), row=2, col=1)
        fig.update(layout_xaxis_rangeslider_visible=False)

        df_day['MA5'] = df_day['Close'].rolling(5).mean()
        df_day['MA25'] = df_day['Close'].rolling(25).mean()
        fig.add_trace(go.Scatter(x=df_day['Date'], y=df_day['MA5'], line=dict(color='orange'), name='MA5'), row=1, col=1)
        fig.add_trace(go.Scatter(x=df_day['Date'], y=df_day['MA25'] , line=dict(color='yellow'), name='MA25'), row=1, col=1)

        fig.add_trace(go.Scatter(x=df_roaroe['Period'], y=df_roaroe['ROA'] , line=dict(color='red'), name='ROA'), row=3, col=1)
        
        html = '<html><body>'
        html += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        html += '</body></html>'
        # we create an instance of QWebEngineView and set the html code
        plot_widget = QWebEngineView()
        plot_widget.setHtml(html)
        # set the QWebEngineView instance as main widget
        self.setCentralWidget(plot_widget)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
