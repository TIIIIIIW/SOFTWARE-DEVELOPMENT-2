from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QMainWindow
from plotly.graph_objects import Figure, Scatter
import plotly
import sqlite3
import pandas as pd
import plotly.express as px
import geopandas as gpd
import plotly.graph_objs as go

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        # create data
        sql = """ SELECT Inf.Symbol,Lin.Lname,Lin.Country,Lin.Latitude,Lin.Longitude,COUNT(Lin.Lname) as size,N.Date
        FROM Information as Inf
        INNER JOIN Share_in_News as Sin on Inf.SymbolId = Sin.SymbolId
        INNER JOIN News as N on N.NewsId = Sin.NewsId 
        INNER JOIN Location_in_News as Lin on N.NewsId = Lin.NewsId 
        WHERE Inf.Symbol = ''
        GROUP BY Lin.Lname;
        """
        con = sqlite3.connect('share_V3.sqlite')   
        df = pd.read_sql(sql, con)
        con.commit()
        con.close

        if len(df) == 0:
            fig = go.Figure(go.Scattergeo())
        else:
            gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))

            fig = px.scatter_geo(gdf,
                                lat=gdf.geometry.y,
                                lon=gdf.geometry.x,
                                hover_name="Lname",
                                size="size",
                                projection="natural earth")
        
        html = '<html><body>'
        html += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        html += '</body></html>'
        # we create an instance of QWebEngineView and set the html code
        plot_widget = QWebEngineView()
        plot_widget.setHtml(html)
        # set the QWebEngineView instance as main widget
        self.setCentralWidget(plot_widget)
        print(html)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
