from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
import sqlite3
from datetime import datetime, timedelta
import pandas as pd
import plotly
import plotly.graph_objs as go
import plotly.express as px
import geopandas as gpd
from Class_update_Share import Update_Stock
from selenium import webdriver

class Ui_MainWindow(object):
#---------------------------------------------------------------- Load Data All
    def load_dataset_all(self):
        conn = sqlite3.connect(r'C:\Users\Admin\Desktop\SOFTDEV2\SOFTWARE-DEVELOPMENT-2\share_V3.sqlite')
        sqlquery = f"""SELECT DISTINCT i.Symbol,i.Sname,m.Mname,s.Full_Sector,ind.Full_Industry,i.Description FROM Information as i
                        INNER JOIN Category as c ON c.SymbolId = i.SymbolId
                        INNER JOIN Sector as s ON c.SectorId = s.SectorId
                        INNER JOIN Industry as ind ON c.IndustryId = ind.IndustryId
                        INNER JOIN Market as m ON m.MarketId = i.MarketId
                        WHERE m.Mname = 'SET'
                        ORDER BY i.Symbol ASC;"""
        result = conn.execute(sqlquery)
        self.tableWidget_dataset.setRowCount(0)
        for row_num, row_data in enumerate(result):
            self.tableWidget_dataset.insertRow(row_num)
            for column_num, data in enumerate(row_data):
                self.tableWidget_dataset.setItem(row_num, column_num, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()
    def load_datanasdaq_all(self):
        conn = sqlite3.connect(r'C:\Users\Admin\Desktop\SOFTDEV2\SOFTWARE-DEVELOPMENT-2\share_V3.sqlite')
        sqlquery = f"""SELECT DISTINCT i.Symbol,i.Sname,m.Mname,s.Full_Sector,ind.Full_Industry FROM Information as i
                        INNER JOIN Category as c ON c.SymbolId = i.SymbolId
                        INNER JOIN Sector as s ON c.SectorId = s.SectorId
                        INNER JOIN Industry as ind ON c.IndustryId = ind.IndustryId
                        INNER JOIN Market as m ON m.MarketId = i.MarketId
                        WHERE m.Mname = 'NASDAQ'
                        ORDER BY i.Symbol ASC;"""
        result = conn.execute(sqlquery)
        self.tableWidget_datanasdaq.setRowCount(0)
        for row_num, row_data in enumerate(result):
            self.tableWidget_datanasdaq.insertRow(row_num)
            for column_num, data in enumerate(row_data):
                self.tableWidget_datanasdaq.setItem(row_num, column_num, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()
    def load_datacrypto_all(self):
        conn = sqlite3.connect(r'C:\Users\Admin\Desktop\SOFTDEV2\SOFTWARE-DEVELOPMENT-2\share_V3.sqlite')
        sqlquery = f"""SELECT DISTINCT i.Symbol,i.Sname,m.Mname FROM Information as i
                        INNER JOIN Market as m ON m.MarketId = i.MarketId
                        WHERE m.Mname = 'CRYPTO'
                        ORDER BY i.Symbol ASC;"""
        result = conn.execute(sqlquery)
        self.tableWidget_datacrypto.setRowCount(0)
        for row_num, row_data in enumerate(result):
            self.tableWidget_datacrypto.insertRow(row_num)
            for column_num, data in enumerate(row_data):
                self.tableWidget_datacrypto.setItem(row_num, column_num, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()
#---------------------------------------------------------------- Load Financial All
    def load_fncset_all(self):
        conn = sqlite3.connect(r'C:\Users\Admin\Desktop\SOFTDEV2\SOFTWARE-DEVELOPMENT-2\share_V3.sqlite')
        sqlquery = f"""SELECT DISTINCT fq.Asset,fq.TotalDebt,fq.Equity,fq.Revenue,fq.NetProfit,fq.ROA,fq.ROE,fq.Period,i.Symbol FROM Financial_quarterly as fq
                        INNER JOIN Information as i ON fq.SymbolId = i.SymbolId
                        WHERE i.MarketId = 1
                        ORDER BY Symbol ASC;"""
        result = conn.execute(sqlquery)
        self.tableWidget_fncset.setRowCount(0)
        for row_num, row_data in enumerate(result):
            self.tableWidget_fncset.insertRow(row_num)
            for column_num, data in enumerate(row_data):
                self.tableWidget_fncset.setItem(row_num, column_num, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()
    def load_fncnasdaq_all(self):
        conn = sqlite3.connect(r'C:\Users\Admin\Desktop\SOFTDEV2\SOFTWARE-DEVELOPMENT-2\share_V3.sqlite')
        sqlquery = f"""SELECT DISTINCT fq.Asset,fq.TotalDebt,fq.Equity,fq.Revenue,fq.NetProfit,fq.ROA,fq.ROE,fq.Period,i.Symbol FROM Financial_quarterly as fq
                        INNER JOIN Information as i ON fq.SymbolId = i.SymbolId
                        WHERE i.MarketId = 2
                        ORDER BY Symbol ASC;"""
        result = conn.execute(sqlquery)
        self.tableWidget_fncnasdaq.setRowCount(0)
        for row_num, row_data in enumerate(result):
            self.tableWidget_fncnasdaq.insertRow(row_num)
            for column_num, data in enumerate(row_data):
                self.tableWidget_fncnasdaq.setItem(row_num, column_num, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()
#---------------------------------------------------------------- Load Data Select
    def load_dataset(self):
        selected_item = self.comboBox_dataset.currentText()
        conn = sqlite3.connect(r'C:\Users\Admin\Desktop\SOFTDEV2\SOFTWARE-DEVELOPMENT-2\share_V3.sqlite')
        sqlquery = f"""SELECT DISTINCT i.Symbol,i.Sname,m.Mname,s.Full_Sector,ind.Full_Industry,i.Description FROM Information as i
                        INNER JOIN Category as c ON c.SymbolId = i.SymbolId
                        INNER JOIN Sector as s ON c.SectorId = s.SectorId
                        INNER JOIN Industry as ind ON c.IndustryId = ind.IndustryId
                        INNER JOIN Market as m ON m.MarketId = i.MarketId
                        WHERE i.Symbol = '{str(selected_item)}';"""
        result = conn.execute(sqlquery)
        self.tableWidget_searchset.setRowCount(0)
        for row_num, row_data in enumerate(result):
            self.tableWidget_searchset.insertRow(row_num)
            for column_num, data in enumerate(row_data):
                self.tableWidget_searchset.setItem(row_num, column_num, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()
    def load_datanasdaq(self):
        selected_item = self.comboBox_datanasdaq.currentText()
        conn = sqlite3.connect(r'C:\Users\Admin\Desktop\SOFTDEV2\SOFTWARE-DEVELOPMENT-2\share_V3.sqlite')
        sqlquery = f"""SELECT DISTINCT i.Symbol,i.Sname,m.Mname,s.Full_Sector,ind.Full_Industry FROM Information as i
                        INNER JOIN Category as c ON c.SymbolId = i.SymbolId
                        INNER JOIN Sector as s ON c.SectorId = s.SectorId
                        INNER JOIN Industry as ind ON c.IndustryId = ind.IndustryId
                        INNER JOIN Market as m ON m.MarketId = i.MarketId
                        WHERE i.Symbol = '{str(selected_item)}';"""
        result = conn.execute(sqlquery)
        self.tableWidget_searchnasdaq.setRowCount(0)
        for row_num, row_data in enumerate(result):
            self.tableWidget_searchnasdaq.insertRow(row_num)
            for column_num, data in enumerate(row_data):
                self.tableWidget_searchnasdaq.setItem(row_num, column_num, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()
    def load_datacrypto(self):
        selected_item = self.comboBox_datacrypto.currentText()
        conn = sqlite3.connect(r'C:\Users\Admin\Desktop\SOFTDEV2\SOFTWARE-DEVELOPMENT-2\share_V3.sqlite')
        sqlquery = f"""SELECT DISTINCT i.Symbol,i.Sname,m.Mname FROM Information as i
                        INNER JOIN Market as m ON m.MarketId = i.MarketId
                        WHERE i.Symbol = '{str(selected_item)}';"""
        result = conn.execute(sqlquery)
        self.tableWidget_searchcrypto.setRowCount(0)
        for row_num, row_data in enumerate(result):
            self.tableWidget_searchcrypto.insertRow(row_num)
            for column_num, data in enumerate(row_data):
                self.tableWidget_searchcrypto.setItem(row_num, column_num, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()
#---------------------------------------------------------------- Load Financial Select
    def load_fncset(self):
        selected_item = self.comboBox_fncset.currentText()
        conn = sqlite3.connect(r'C:\Users\Admin\Desktop\SOFTDEV2\SOFTWARE-DEVELOPMENT-2\share_V3.sqlite')
        sqlquery = f"""SELECT DISTINCT fq.Asset,fq.TotalDebt,fq.Equity,fq.Revenue,fq.NetProfit,fq.ROA,fq.ROE,fq.Period,i.Symbol FROM Financial_quarterly as fq
                        INNER JOIN Information as i ON fq.SymbolId = i.SymbolId
                        WHERE i.Symbol = '{str(selected_item)}'
                        ORDER BY Period DESC;"""
        result = conn.execute(sqlquery)
        self.tableWidget_searchfncset.setRowCount(0)
        for row_num, row_data in enumerate(result):
            self.tableWidget_searchfncset.insertRow(row_num)
            for column_num, data in enumerate(row_data):
                self.tableWidget_searchfncset.setItem(row_num, column_num, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()
    def load_fncnasdaq(self):
        selected_item = self.comboBox_fncnasdaq.currentText()
        conn = sqlite3.connect(r'C:\Users\Admin\Desktop\SOFTDEV2\SOFTWARE-DEVELOPMENT-2\share_V3.sqlite')
        sqlquery = f"""SELECT DISTINCT fq.Asset,fq.TotalDebt,fq.Equity,fq.Revenue,fq.NetProfit,fq.ROA,fq.ROE,fq.Period,i.Symbol FROM Financial_quarterly as fq
                        INNER JOIN Information as i ON fq.SymbolId = i.SymbolId
                        WHERE i.Symbol = '{str(selected_item)}'
                        ORDER BY Period DESC;"""
        result = conn.execute(sqlquery)
        self.tableWidget_searchfncnasdaq.setRowCount(0)
        for row_num, row_data in enumerate(result):
            self.tableWidget_searchfncnasdaq.insertRow(row_num)
            for column_num, data in enumerate(row_data):
                self.tableWidget_searchfncnasdaq.setItem(row_num, column_num, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()
#---------------------------------------------------------------- Load News All
    def load_newsall(self):
            selected_time = self.comboBox_timenewsall.currentText()
            today = datetime.today()
            last_3_days = today - timedelta(days=3)
            last_week = today - timedelta(weeks=1)
            last_month = today - timedelta(days=30)
            conn = sqlite3.connect(r'C:\Users\Admin\Desktop\SOFTDEV2\SOFTWARE-DEVELOPMENT-2\share_V3.sqlite')
            sqlquery = """SELECT DISTINCT n.Date, n.Title, n.Description, n.Link, n.Source 
                        FROM News AS n INNER JOIN Share_in_News AS sn ON sn.NewsId = n.NewsId
                        INNER JOIN Information AS i ON i.SymbolId = sn.SymbolId"""
            result = conn.execute(sqlquery)
            rows_day = []
            rows_3day = []
            rows_week = []
            rows_month = []
            rows_all = []
            for row_num, row_data in enumerate(result):
                date_str = row_data[0]
                date = datetime.strptime(date_str, '%d/%m/%Y')
                row_data = (date,) + row_data[1:]
                if row_data[0] >= last_3_days:
                    rows_3day.append(row_data)
                if row_data[0] >= today:
                    rows_day.append(row_data)
                if row_data[0] >= last_week:
                    rows_week.append(row_data)
                if row_data[0] >= last_month:
                    rows_month.append(row_data)
                rows_all.append(row_data)
            if selected_time == 'Today':
                rows_sorted = sorted(rows_day, key=lambda x: x[0], reverse=True)
            elif selected_time == '3 Days':
                rows_sorted = sorted(rows_3day, key=lambda x: x[0], reverse=True)
            elif selected_time == 'Weekly': 
                rows_sorted = sorted(rows_week, key=lambda x: x[0], reverse=True)
            elif selected_time == 'Monthly':   
                rows_sorted = sorted(rows_month, key=lambda x: x[0], reverse=True)  
            elif selected_time == 'All':   
                rows_sorted = sorted(rows_all, key=lambda x: x[0], reverse=True)
            self.tableWidget_allnews.setRowCount(0)
            for row_num, row_data in enumerate(rows_sorted):
                self.tableWidget_allnews.insertRow(row_num)
                for column_num, data in enumerate(row_data):
                    self.tableWidget_allnews.setItem(row_num, column_num, QtWidgets.QTableWidgetItem(str(data)))
            conn.close()
#---------------------------------------------------------------- Load News Select
    def load_newsset(self):
        selected_item = self.comboBox_newsset.currentText()
        selected_time = self.comboBox_timenewsset.currentText()
        today = datetime.today()
        last_3_days = today - timedelta(days=3)
        last_week = today - timedelta(weeks=1)
        last_month = today - timedelta(days=30)
        conn = sqlite3.connect(r'C:\Users\Admin\Desktop\SOFTDEV2\SOFTWARE-DEVELOPMENT-2\share_V3.sqlite')
        sqlquery = f"""SELECT DISTINCT n.Date,n.Title,n.Description,n.Link,n.Source FROM News as n
                        INNER JOIN Share_in_News as sn ON sn.NewsId = n.NewsId
                        INNER JOIN Information as i ON i.SymbolId = sn.SymbolId
                        WHERE i.Symbol = '{str(selected_item)}' """
        result = conn.execute(sqlquery)
        rows_day = []
        rows_3day = []
        rows_week = []
        rows_month = []
        rows_all = []
        for row_num, row_data in enumerate(result):
            date_str = row_data[0]
            date = datetime.strptime(date_str, '%d/%m/%Y')
            row_data = (date,) + row_data[1:]
            if row_data[0] >= last_3_days:
                rows_3day.append(row_data)
            if row_data[0] >= today:
                rows_day.append(row_data)
            if row_data[0] >= last_week:
                rows_week.append(row_data)
            if row_data[0] >= last_month:
                rows_month.append(row_data)
            rows_all.append(row_data)
        if selected_time == 'Today':
            rows_sorted = sorted(rows_day, key=lambda x: x[0], reverse=True)
        elif selected_time == '3 Days':
            rows_sorted = sorted(rows_3day, key=lambda x: x[0], reverse=True)
        elif selected_time == 'Weekly': 
            rows_sorted = sorted(rows_week, key=lambda x: x[0], reverse=True)
        elif selected_time == 'Monthly':   
            rows_sorted = sorted(rows_month, key=lambda x: x[0], reverse=True)  
        elif selected_time == 'All':   
            rows_sorted = sorted(rows_all, key=lambda x: x[0], reverse=True)
        self.tableWidget_newsset.setRowCount(0)
        for row_num, row_data in enumerate(rows_sorted):
            self.tableWidget_newsset.insertRow(row_num)
            for column_num, data in enumerate(row_data):
                self.tableWidget_newsset.setItem(row_num, column_num, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()
    def load_newsnasdaq(self):
        selected_item = self.comboBox_newsnasdaq.currentText()
        selected_time = self.comboBox_timenewsnasdaq.currentText()
        today = datetime.today()
        last_3_days = today - timedelta(days=3)
        last_week = today - timedelta(weeks=1)
        last_month = today - timedelta(days=30)
        conn = sqlite3.connect(r'C:\Users\Admin\Desktop\SOFTDEV2\SOFTWARE-DEVELOPMENT-2\share_V3.sqlite')
        sqlquery = f"""SELECT DISTINCT n.Date,n.Title,n.Description,n.Link,n.Source FROM News as n
                        INNER JOIN Share_in_News as sn ON sn.NewsId = n.NewsId
                        INNER JOIN Information as i ON i.SymbolId = sn.SymbolId
                        WHERE i.Symbol = '{str(selected_item)}' """
        result = conn.execute(sqlquery)
        rows_day = []
        rows_3day = []
        rows_week = []
        rows_month = []
        rows_all = []
        for row_num, row_data in enumerate(result):
            date_str = row_data[0]
            date = datetime.strptime(date_str, '%d/%m/%Y')
            row_data = (date,) + row_data[1:]
            if row_data[0] >= last_3_days:
                rows_3day.append(row_data)
            if row_data[0] >= today:
                rows_day.append(row_data)
            if row_data[0] >= last_week:
                rows_week.append(row_data)
            if row_data[0] >= last_month:
                rows_month.append(row_data)
            rows_all.append(row_data)
        if selected_time == 'Today':
            rows_sorted = sorted(rows_day, key=lambda x: x[0], reverse=True)
        elif selected_time == '3 Days':
            rows_sorted = sorted(rows_3day, key=lambda x: x[0], reverse=True)
        elif selected_time == 'Weekly': 
            rows_sorted = sorted(rows_week, key=lambda x: x[0], reverse=True)
        elif selected_time == 'Monthly':   
            rows_sorted = sorted(rows_month, key=lambda x: x[0], reverse=True)  
        elif selected_time == 'All':   
            rows_sorted = sorted(rows_all, key=lambda x: x[0], reverse=True)
        self.tableWidget_newsnasdaq.setRowCount(0)
        for row_num, row_data in enumerate(rows_sorted):
            self.tableWidget_newsnasdaq.insertRow(row_num)
            for column_num, data in enumerate(row_data):
                self.tableWidget_newsnasdaq.setItem(row_num, column_num, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()
    def load_newscrypto(self):
        selected_item = self.comboBox_newscrypto.currentText()
        selected_time = self.comboBox_timenewscrypto.currentText()
        today = datetime.today()
        last_3_days = today - timedelta(days=3)
        last_week = today - timedelta(weeks=1)
        last_month = today - timedelta(days=30)
        conn = sqlite3.connect(r'C:\Users\Admin\Desktop\SOFTDEV2\SOFTWARE-DEVELOPMENT-2\share_V3.sqlite')
        sqlquery = f"""SELECT DISTINCT n.Date,n.Title,n.Description,n.Link,n.Source FROM News as n
                        INNER JOIN Share_in_News as sn ON sn.NewsId = n.NewsId
                        INNER JOIN Information as i ON i.SymbolId = sn.SymbolId
                        WHERE i.Symbol = '{str(selected_item)}' """
        result = conn.execute(sqlquery)
        rows_day = []
        rows_3day = []
        rows_week = []
        rows_month = []
        rows_all = []
        for row_num, row_data in enumerate(result):
            date_str = row_data[0]
            date = datetime.strptime(date_str, '%d/%m/%Y')
            row_data = (date,) + row_data[1:]
            if row_data[0] >= last_3_days:
                rows_3day.append(row_data)
            if row_data[0] >= today:
                rows_day.append(row_data)
            if row_data[0] >= last_week:
                rows_week.append(row_data)
            if row_data[0] >= last_month:
                rows_month.append(row_data)
            rows_all.append(row_data)
        if selected_time == 'Today':
            rows_sorted = sorted(rows_day, key=lambda x: x[0], reverse=True)
        elif selected_time == '3 Days':
            rows_sorted = sorted(rows_3day, key=lambda x: x[0], reverse=True)
        elif selected_time == 'Weekly': 
            rows_sorted = sorted(rows_week, key=lambda x: x[0], reverse=True)
        elif selected_time == 'Monthly':   
            rows_sorted = sorted(rows_month, key=lambda x: x[0], reverse=True)  
        elif selected_time == 'All':   
            rows_sorted = sorted(rows_all, key=lambda x: x[0], reverse=True)
        self.tableWidget_newscrypto.setRowCount(0)
        for row_num, row_data in enumerate(rows_sorted):
            self.tableWidget_newscrypto.insertRow(row_num)
            for column_num, data in enumerate(row_data):
                self.tableWidget_newscrypto.setItem(row_num, column_num, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()
#---------------------------------------------------------------- Spacial Select
    def spatial_newsset(self):
        selected_item = self.comboBox_newsset.currentText()
        sql = f""" SELECT Inf.Symbol,Lin.Lname,Lin.Country,Lin.Latitude,Lin.Longitude,COUNT(Lin.Lname) as size,N.Date
        FROM Information as Inf
        INNER JOIN Share_in_News as Sin on Inf.SymbolId = Sin.SymbolId
        INNER JOIN News as N on N.NewsId = Sin.NewsId 
        INNER JOIN Location_in_News as Lin on N.NewsId = Lin.NewsId 
        WHERE Inf.Symbol = '{selected_item}'
        GROUP BY Lin.Lname;
        """
        con = sqlite3.connect(r'C:\Users\Admin\Desktop\SOFTDEV2\SOFTWARE-DEVELOPMENT-2\share_V3.sqlite')   
        df = pd.read_sql(sql, con)
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
        self.WebEngine_newsset.setHtml(html)
    def spatial_newsnasdaq(self):
            selected_item = self.comboBox_newsnasdaq.currentText()
            sql = f""" SELECT Inf.Symbol,Lin.Lname,Lin.Country,Lin.Latitude,Lin.Longitude,COUNT(Lin.Lname) as size,N.Date
            FROM Information as Inf
            INNER JOIN Share_in_News as Sin on Inf.SymbolId = Sin.SymbolId
            INNER JOIN News as N on N.NewsId = Sin.NewsId 
            INNER JOIN Location_in_News as Lin on N.NewsId = Lin.NewsId 
            WHERE Inf.Symbol = '{selected_item}'
            GROUP BY Lin.Lname;
            """
            con = sqlite3.connect(r'C:\Users\Admin\Desktop\SOFTDEV2\SOFTWARE-DEVELOPMENT-2\share_V3.sqlite')   
            df = pd.read_sql(sql, con)
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
            self.WebEngine_newsnasdaq.setHtml(html)
    def spatial_newscrypto(self):
            selected_item = self.comboBox_newscrypto.currentText()
            sql = f""" SELECT Inf.Symbol,Lin.Lname,Lin.Country,Lin.Latitude,Lin.Longitude,COUNT(Lin.Lname) as size,N.Date
            FROM Information as Inf
            INNER JOIN Share_in_News as Sin on Inf.SymbolId = Sin.SymbolId
            INNER JOIN News as N on N.NewsId = Sin.NewsId 
            INNER JOIN Location_in_News as Lin on N.NewsId = Lin.NewsId 
            WHERE Inf.Symbol = '{selected_item}'
            GROUP BY Lin.Lname;
            """
            con = sqlite3.connect(r'C:\Users\Admin\Desktop\SOFTDEV2\SOFTWARE-DEVELOPMENT-2\share_V3.sqlite')   
            df = pd.read_sql(sql, con)
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
            self.WebEngine_newscrypto.setHtml(html)
#---------------------------------------------------------------- Update Price
    def updateSetPrice(self):
        selected_item = self.comboBox_dataset.currentText()
        Update_Stock('SET').UpdatePicehours(f'{selected_item}')
        Update_Stock('SET').UpdatePiceDays(f'{selected_item}')
    def updateNasdaqPrice(self):
        selected_item = self.comboBox_datanasdaq.currentText()
        Update_Stock('NASDAQ').UpdatePicehours(f'{selected_item}')
        Update_Stock('NASDAQ').UpdatePiceDays(f'{selected_item}')
    def updateCryptoPrice(self):
        selected_item = self.comboBox_datacrypto.currentText()
        Update_Stock('CRYPTO').UpdatePicehours(f'{selected_item}')
        Update_Stock('CRYPTO').UpdatePiceDays(f'{selected_item}')
#---------------------------------------------------------------- Update Financial
    def updateSetFnc(self):
        selected_item = self.comboBox_fncset.currentText()
        driver = webdriver.Chrome(r"C:\Users\Admin\Desktop\SOFTDEV2\SOFTWARE-DEVELOPMENT-2\ML\Data\chromedriver.exe")
        Update_Stock('SET').updateFinancial(driver,f'{selected_item}')
    def updateNasdaqFnc(self):
        selected_item = self.comboBox_fncnasdaq.currentText()
        driver = webdriver.Chrome(r"C:\Users\Admin\Desktop\SOFTDEV2\SOFTWARE-DEVELOPMENT-2\ML\Data\chromedriver.exe")
        Update_Stock('NASDAQ').updateFinancial(driver,f'{selected_item}')
#---------------------------------------------------------------- Update News
    def updateSetNews(self):
        selected_item = self.comboBox_newsset.currentText()
        Update_Stock('SET').UpdateNews(f'{selected_item}')
    def updateNasdaqNews(self):
        selected_item = self.comboBox_newsnasdaq.currentText()
        Update_Stock('NASDAQ').UpdateNews(f'{selected_item}')
    def updateCryptoNews(self):
        selected_item = self.comboBox_newscrypto.currentText()
        Update_Stock('CRYPTO').UpdateNews(f'{selected_item}')




    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1820, 920)
        MainWindow.setMinimumSize(QtCore.QSize(1820, 920))
        MainWindow.setMaximumSize(QtCore.QSize(1820, 920))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.All = QtWidgets.QWidget(self.centralwidget)
        self.All.setGeometry(QtCore.QRect(0, 0, 1821, 951))
        self.All.setStyleSheet("background-color: #353535;")
        self.All.setObjectName("All")
        self.Header = QtWidgets.QFrame(self.All)
        self.Header.setGeometry(QtCore.QRect(0, 0, 1821, 71))
        self.Header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Header.setObjectName("Header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Header)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_data = QtWidgets.QPushButton(self.Header)
        self.pushButton_data.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_data.setFont(font)
        self.pushButton_data.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_data.setStyleSheet("background-color: #E9EBEF;")
        self.pushButton_data.setObjectName("pushButton_data")
        self.horizontalLayout.addWidget(self.pushButton_data)
        self.pushButton_graph = QtWidgets.QPushButton(self.Header)
        self.pushButton_graph.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_graph.setFont(font)
        self.pushButton_graph.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_graph.setStyleSheet("background-color: #E9EBEF;")
        self.pushButton_graph.setObjectName("pushButton_graph")
        self.horizontalLayout.addWidget(self.pushButton_graph)
        self.pushButton_financial = QtWidgets.QPushButton(self.Header)
        self.pushButton_financial.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_financial.setFont(font)
        self.pushButton_financial.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_financial.setStyleSheet("background-color: #E9EBEF;")
        self.pushButton_financial.setObjectName("pushButton_financial")
        self.horizontalLayout.addWidget(self.pushButton_financial)
        self.pushButton_news = QtWidgets.QPushButton(self.Header)
        self.pushButton_news.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_news.setFont(font)
        self.pushButton_news.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_news.setStyleSheet("background-color: #E9EBEF;")
        self.pushButton_news.setObjectName("pushButton_news")
        self.horizontalLayout.addWidget(self.pushButton_news)
        self.DataPage = QtWidgets.QWidget(self.All)
        self.DataPage.setGeometry(QtCore.QRect(30, 80, 1761, 791))
        self.DataPage.setStyleSheet("background-color: #353535;")
        self.DataPage.setObjectName("DataPage")
        self.Data_select = QtWidgets.QWidget(self.DataPage)
        self.Data_select.setGeometry(QtCore.QRect(0, 0, 321, 791))
        self.Data_select.setStyleSheet("background-color: #E9EBEF;")
        self.Data_select.setObjectName("Data_select")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.Data_select)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 301, 220))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_dataset = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_dataset.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_dataset.setFont(font)
        self.pushButton_dataset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_dataset.setStyleSheet("background-color: #D2D7DF;")
        self.pushButton_dataset.setObjectName("pushButton_dataset")
        self.verticalLayout.addWidget(self.pushButton_dataset)
        self.pushButton_datanasdaq = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_datanasdaq.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_datanasdaq.setFont(font)
        self.pushButton_datanasdaq.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_datanasdaq.setStyleSheet("background-color: #D2D7DF;")
        self.pushButton_datanasdaq.setObjectName("pushButton_datanasdaq")
        self.verticalLayout.addWidget(self.pushButton_datanasdaq)
        self.pushButton_datacrypto = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_datacrypto.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_datacrypto.setFont(font)
        self.pushButton_datacrypto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_datacrypto.setStyleSheet("background-color: #D2D7DF;")
        self.pushButton_datacrypto.setObjectName("pushButton_datacrypto")
        self.verticalLayout.addWidget(self.pushButton_datacrypto)
        self.pushButton_adddata = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_adddata.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_adddata.setFont(font)
        self.pushButton_adddata.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_adddata.setStyleSheet("background-color: #D2D7DF;")
        self.pushButton_adddata.setObjectName("pushButton_adddata")
        self.verticalLayout.addWidget(self.pushButton_adddata)
        self.pushButton_datanasdaq.raise_()
        self.pushButton_datacrypto.raise_()
        self.pushButton_adddata.raise_()
        self.pushButton_dataset.raise_()
        self.tablenasdaq = QtWidgets.QWidget(self.DataPage)
        self.tablenasdaq.setGeometry(QtCore.QRect(350, 0, 1411, 791))
        self.tablenasdaq.setStyleSheet("background-color: #D2D7DF;")
        self.tablenasdaq.setObjectName("tablenasdaq")
        self.tableWidget_datanasdaq = QtWidgets.QTableWidget(self.tablenasdaq)
        self.tableWidget_datanasdaq.setGeometry(QtCore.QRect(0, 0, 1411, 600))
        self.tableWidget_datanasdaq.setMaximumSize(QtCore.QSize(1411, 16777215))
        self.tableWidget_datanasdaq.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_datanasdaq.setObjectName("tableWidget_datanasdaq")
        self.tableWidget_datanasdaq.setColumnCount(5)
        self.tableWidget_datanasdaq.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_datanasdaq.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_datanasdaq.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_datanasdaq.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_datanasdaq.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_datanasdaq.setHorizontalHeaderItem(4, item)
        self.tableWidget_datanasdaq.horizontalHeader().setDefaultSectionSize(200)
        self.comboBox_datanasdaq = QtWidgets.QComboBox(self.tablenasdaq)
        self.comboBox_datanasdaq.setGeometry(QtCore.QRect(0, 620, 1241, 31))
        self.comboBox_datanasdaq.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_datanasdaq.setStyleSheet("background-color:#ffffff;")
        self.comboBox_datanasdaq.setObjectName("comboBox_datanasdaq")
        self.tableWidget_searchnasdaq = QtWidgets.QTableWidget(self.tablenasdaq)
        self.tableWidget_searchnasdaq.setGeometry(QtCore.QRect(0, 670, 1411, 121))
        self.tableWidget_searchnasdaq.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_searchnasdaq.setObjectName("tableWidget_searchnasdaq")
        self.tableWidget_searchnasdaq.setColumnCount(5)
        self.tableWidget_searchnasdaq.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_searchnasdaq.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_searchnasdaq.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_searchnasdaq.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_searchnasdaq.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_searchnasdaq.setHorizontalHeaderItem(4, item)
        self.tableWidget_searchnasdaq.horizontalHeader().setDefaultSectionSize(200)
        self.pushButton_updatenasdaq = QtWidgets.QPushButton(self.tablenasdaq)
        self.pushButton_updatenasdaq.setGeometry(QtCore.QRect(1260, 620, 141, 31))
        self.pushButton_updatenasdaq.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_updatenasdaq.setStyleSheet("background-color: rgb(225, 255, 228);")
        self.pushButton_updatenasdaq.setObjectName("pushButton_updatenasdaq")
        self.tableset = QtWidgets.QWidget(self.DataPage)
        self.tableset.setGeometry(QtCore.QRect(350, 0, 1411, 791))
        self.tableset.setStyleSheet("background-color: #D2D7DF;")
        self.tableset.setObjectName("tableset")
        self.tableWidget_dataset = QtWidgets.QTableWidget(self.tableset)
        self.tableWidget_dataset.setGeometry(QtCore.QRect(0, 0, 1411, 600))
        self.tableWidget_dataset.setMaximumSize(QtCore.QSize(1411, 16777215))
        self.tableWidget_dataset.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_dataset.setObjectName("tableWidget_dataset")
        self.tableWidget_dataset.setColumnCount(6)
        self.tableWidget_dataset.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dataset.setHorizontalHeaderItem(5, item)
        self.tableWidget_dataset.horizontalHeader().setDefaultSectionSize(150)
        self.comboBox_dataset = QtWidgets.QComboBox(self.tableset)
        self.comboBox_dataset.setGeometry(QtCore.QRect(0, 620, 1241, 31))
        self.comboBox_dataset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_dataset.setStyleSheet("background-color:#ffffff;")
        self.comboBox_dataset.setObjectName("comboBox_dataset")
        self.tableWidget_searchset = QtWidgets.QTableWidget(self.tableset)
        self.tableWidget_searchset.setGeometry(QtCore.QRect(0, 670, 1411, 121))
        self.tableWidget_searchset.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_searchset.setObjectName("tableWidget_searchset")
        self.tableWidget_searchset.setColumnCount(6)
        self.tableWidget_searchset.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_searchset.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_searchset.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_searchset.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_searchset.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_searchset.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_searchset.setHorizontalHeaderItem(5, item)
        self.tableWidget_searchset.horizontalHeader().setDefaultSectionSize(150)
        self.pushButton_updateset = QtWidgets.QPushButton(self.tableset)
        self.pushButton_updateset.setGeometry(QtCore.QRect(1260, 620, 141, 31))
        self.pushButton_updateset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_updateset.setStyleSheet("background-color: rgb(225, 255, 228);")
        self.pushButton_updateset.setObjectName("pushButton_updateset")
        self.tablecrypto = QtWidgets.QWidget(self.DataPage)
        self.tablecrypto.setGeometry(QtCore.QRect(350, 0, 1411, 791))
        self.tablecrypto.setStyleSheet("background-color: #D2D7DF;")
        self.tablecrypto.setObjectName("tablecrypto")
        self.tableWidget_datacrypto = QtWidgets.QTableWidget(self.tablecrypto)
        self.tableWidget_datacrypto.setGeometry(QtCore.QRect(0, 0, 611, 791))
        self.tableWidget_datacrypto.setMaximumSize(QtCore.QSize(1411, 16777215))
        self.tableWidget_datacrypto.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_datacrypto.setObjectName("tableWidget_datacrypto")
        self.tableWidget_datacrypto.setColumnCount(3)
        self.tableWidget_datacrypto.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_datacrypto.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_datacrypto.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_datacrypto.setHorizontalHeaderItem(2, item)
        self.tableWidget_datacrypto.horizontalHeader().setDefaultSectionSize(200)
        self.comboBox_datacrypto = QtWidgets.QComboBox(self.tablecrypto)
        self.comboBox_datacrypto.setGeometry(QtCore.QRect(650, 20, 731, 31))
        self.comboBox_datacrypto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_datacrypto.setStyleSheet("background-color:#ffffff;")
        self.comboBox_datacrypto.setObjectName("comboBox_datacrypto")
        self.tableWidget_searchcrypto = QtWidgets.QTableWidget(self.tablecrypto)
        self.tableWidget_searchcrypto.setGeometry(QtCore.QRect(700, 80, 611, 71))
        self.tableWidget_searchcrypto.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_searchcrypto.setObjectName("tableWidget_searchcrypto")
        self.tableWidget_searchcrypto.setColumnCount(3)
        self.tableWidget_searchcrypto.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_searchcrypto.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_searchcrypto.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_searchcrypto.setHorizontalHeaderItem(2, item)
        self.tableWidget_searchcrypto.horizontalHeader().setDefaultSectionSize(200)
        self.pushButton_updatecrypto = QtWidgets.QPushButton(self.tablecrypto)
        self.pushButton_updatecrypto.setGeometry(QtCore.QRect(1170, 180, 141, 31))
        self.pushButton_updatecrypto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_updatecrypto.setStyleSheet("background-color: rgb(225, 255, 228);")
        self.pushButton_updatecrypto.setObjectName("pushButton_updatecrypto")
        self.add_data = QtWidgets.QWidget(self.DataPage)
        self.add_data.setGeometry(QtCore.QRect(350, 0, 1411, 791))
        self.add_data.setStyleSheet("background-color: #D2D7DF;")
        self.add_data.setObjectName("add_data")
        self.lineEdit_inputsymbol = QtWidgets.QLineEdit(self.add_data)
        self.lineEdit_inputsymbol.setGeometry(QtCore.QRect(560, 230, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_inputsymbol.setFont(font)
        self.lineEdit_inputsymbol.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_inputsymbol.setObjectName("lineEdit_inputsymbol")
        self.label_addsymbol = QtWidgets.QLabel(self.add_data)
        self.label_addsymbol.setGeometry(QtCore.QRect(610, 170, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_addsymbol.setFont(font)
        self.label_addsymbol.setObjectName("label_addsymbol")
        self.comboBox_marketstock = QtWidgets.QComboBox(self.add_data)
        self.comboBox_marketstock.setGeometry(QtCore.QRect(560, 300, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.comboBox_marketstock.setFont(font)
        self.comboBox_marketstock.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_marketstock.setObjectName("comboBox_marketstock")
        self.comboBox_marketstock.addItem("")
        self.comboBox_marketstock.addItem("")
        self.comboBox_marketstock.addItem("")
        self.pushButton_addstock = QtWidgets.QPushButton(self.add_data)
        self.pushButton_addstock.setGeometry(QtCore.QRect(820, 380, 75, 23))
        self.pushButton_addstock.setStyleSheet("background-color: rgb(198, 255, 221);")
        self.pushButton_addstock.setObjectName("pushButton_addstock")
        self.lineEdit_addresult = QtWidgets.QLineEdit(self.add_data)
        self.lineEdit_addresult.setGeometry(QtCore.QRect(670, 420, 113, 20))
        self.lineEdit_addresult.setObjectName("lineEdit_addresult")
        self.Data_select.raise_()
        self.tablecrypto.raise_()
        self.tablenasdaq.raise_()
        self.add_data.raise_()
        self.tableset.raise_()
        self.GraphPage = QtWidgets.QWidget(self.All)
        self.GraphPage.setGeometry(QtCore.QRect(30, 80, 1761, 791))
        self.GraphPage.setStyleSheet("background-color: #353535;")
        self.GraphPage.setObjectName("GraphPage")
        self.Graph_select = QtWidgets.QWidget(self.GraphPage)
        self.Graph_select.setGeometry(QtCore.QRect(0, 0, 321, 791))
        self.Graph_select.setStyleSheet("background-color: #E9EBEF;")
        self.Graph_select.setObjectName("Graph_select")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Graph_select)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 301, 180))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_graphset = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_graphset.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_graphset.setFont(font)
        self.pushButton_graphset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_graphset.setStyleSheet("background-color: #D2D7DF;")
        self.pushButton_graphset.setObjectName("pushButton_graphset")
        self.verticalLayout_2.addWidget(self.pushButton_graphset)
        self.pushButton_graphnasdaq = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_graphnasdaq.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_graphnasdaq.setFont(font)
        self.pushButton_graphnasdaq.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_graphnasdaq.setStyleSheet("background-color: #D2D7DF;")
        self.pushButton_graphnasdaq.setObjectName("pushButton_graphnasdaq")
        self.verticalLayout_2.addWidget(self.pushButton_graphnasdaq)
        self.pushButton_graphcrypto = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_graphcrypto.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_graphcrypto.setFont(font)
        self.pushButton_graphcrypto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_graphcrypto.setStyleSheet("background-color: #D2D7DF;")
        self.pushButton_graphcrypto.setObjectName("pushButton_graphcrypto")
        self.verticalLayout_2.addWidget(self.pushButton_graphcrypto)
        self.Webview_set = QtWidgets.QWidget(self.GraphPage)
        self.Webview_set.setGeometry(QtCore.QRect(350, 0, 1411, 791))
        self.Webview_set.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.Webview_set.setObjectName("Webview_set")
        self.Webview_nasdaq = QtWidgets.QWidget(self.GraphPage)
        self.Webview_nasdaq.setGeometry(QtCore.QRect(350, 0, 1411, 791))
        self.Webview_nasdaq.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.Webview_nasdaq.setObjectName("Webview_nasdaq")
        self.Webview_crypto = QtWidgets.QWidget(self.GraphPage)
        self.Webview_crypto.setGeometry(QtCore.QRect(350, 0, 1411, 791))
        self.Webview_crypto.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.Webview_crypto.setObjectName("Webview_crypto")
        self.Graph_select.raise_()
        self.Webview_nasdaq.raise_()
        self.Webview_crypto.raise_()
        self.Webview_set.raise_()
        self.FinancialPage = QtWidgets.QWidget(self.All)
        self.FinancialPage.setGeometry(QtCore.QRect(30, 80, 1761, 791))
        self.FinancialPage.setStyleSheet("background-color: #353535;")
        self.FinancialPage.setObjectName("FinancialPage")
        self.Financial_select = QtWidgets.QWidget(self.FinancialPage)
        self.Financial_select.setGeometry(QtCore.QRect(0, 0, 321, 791))
        self.Financial_select.setStyleSheet("background-color: #E9EBEF;")
        self.Financial_select.setObjectName("Financial_select")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.Financial_select)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 301, 180))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_fncset = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_fncset.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_fncset.setFont(font)
        self.pushButton_fncset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_fncset.setStyleSheet("background-color: #D2D7DF;")
        self.pushButton_fncset.setObjectName("pushButton_fncset")
        self.verticalLayout_3.addWidget(self.pushButton_fncset)
        self.pushButton_fncnasdaq = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_fncnasdaq.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_fncnasdaq.setFont(font)
        self.pushButton_fncnasdaq.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_fncnasdaq.setStyleSheet("background-color: #D2D7DF;")
        self.pushButton_fncnasdaq.setObjectName("pushButton_fncnasdaq")
        self.verticalLayout_3.addWidget(self.pushButton_fncnasdaq)
        self.financeset = QtWidgets.QWidget(self.FinancialPage)
        self.financeset.setGeometry(QtCore.QRect(350, 0, 1411, 791))
        self.financeset.setStyleSheet("background-color: #D2D7DF;")
        self.financeset.setObjectName("financeset")
        self.comboBox_fncset = QtWidgets.QComboBox(self.financeset)
        self.comboBox_fncset.setGeometry(QtCore.QRect(0, 520, 1241, 31))
        self.comboBox_fncset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_fncset.setStyleSheet("background-color:#ffffff;")
        self.comboBox_fncset.setObjectName("comboBox_fncset")
        self.tableWidget_fncset = QtWidgets.QTableWidget(self.financeset)
        self.tableWidget_fncset.setGeometry(QtCore.QRect(0, 0, 1411, 501))
        self.tableWidget_fncset.setMaximumSize(QtCore.QSize(1411, 16777215))
        self.tableWidget_fncset.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_fncset.setObjectName("tableWidget_fncset")
        self.tableWidget_fncset.setColumnCount(9)
        self.tableWidget_fncset.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fncset.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fncset.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fncset.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fncset.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fncset.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fncset.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fncset.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fncset.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fncset.setHorizontalHeaderItem(8, item)
        self.tableWidget_fncset.horizontalHeader().setDefaultSectionSize(156)
        self.pushButton_updatefncset = QtWidgets.QPushButton(self.financeset)
        self.pushButton_updatefncset.setGeometry(QtCore.QRect(1260, 520, 141, 31))
        self.pushButton_updatefncset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_updatefncset.setStyleSheet("background-color: rgb(225, 255, 228);")
        self.pushButton_updatefncset.setObjectName("pushButton_updatefncset")
        self.tableWidget_searchfncset = QtWidgets.QTableWidget(self.financeset)
        self.tableWidget_searchfncset.setGeometry(QtCore.QRect(0, 570, 1411, 221))
        self.tableWidget_searchfncset.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_searchfncset.setObjectName("tableWidget_searchfncset")
        self.tableWidget_searchfncset.setColumnCount(9)
        self.tableWidget_searchfncset.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_searchfncset.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_searchfncset.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_searchfncset.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_searchfncset.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_searchfncset.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_searchfncset.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_searchfncset.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_searchfncset.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_searchfncset.setHorizontalHeaderItem(8, item)
        self.tableWidget_searchfncset.horizontalHeader().setDefaultSectionSize(156)
        self.tableWidget_fncset.raise_()
        self.comboBox_fncset.raise_()
        self.pushButton_updatefncset.raise_()
        self.tableWidget_searchfncset.raise_()
        self.financenasdaq = QtWidgets.QWidget(self.FinancialPage)
        self.financenasdaq.setGeometry(QtCore.QRect(350, 0, 1411, 791))
        self.financenasdaq.setStyleSheet("background-color: #D2D7DF;")
        self.financenasdaq.setObjectName("financenasdaq")
        self.comboBox_fncnasdaq = QtWidgets.QComboBox(self.financenasdaq)
        self.comboBox_fncnasdaq.setGeometry(QtCore.QRect(0, 520, 1241, 31))
        self.comboBox_fncnasdaq.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_fncnasdaq.setStyleSheet("background-color:#ffffff;")
        self.comboBox_fncnasdaq.setObjectName("comboBox_fncnasdaq")
        self.tableWidget_fncnasdaq = QtWidgets.QTableWidget(self.financenasdaq)
        self.tableWidget_fncnasdaq.setGeometry(QtCore.QRect(0, 0, 1411, 501))
        self.tableWidget_fncnasdaq.setMaximumSize(QtCore.QSize(1411, 16777215))
        self.tableWidget_fncnasdaq.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_fncnasdaq.setObjectName("tableWidget_fncnasdaq")
        self.tableWidget_fncnasdaq.setColumnCount(9)
        self.tableWidget_fncnasdaq.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fncnasdaq.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fncnasdaq.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fncnasdaq.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fncnasdaq.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fncnasdaq.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fncnasdaq.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fncnasdaq.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fncnasdaq.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_fncnasdaq.setHorizontalHeaderItem(8, item)
        self.tableWidget_fncnasdaq.horizontalHeader().setDefaultSectionSize(156)
        self.pushButton_updatefncnasdaq = QtWidgets.QPushButton(self.financenasdaq)
        self.pushButton_updatefncnasdaq.setGeometry(QtCore.QRect(1260, 520, 141, 31))
        self.pushButton_updatefncnasdaq.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_updatefncnasdaq.setStyleSheet("background-color: rgb(225, 255, 228);")
        self.pushButton_updatefncnasdaq.setObjectName("pushButton_updatefncnasdaq")
        self.tableWidget_searchfncnasdaq = QtWidgets.QTableWidget(self.financenasdaq)
        self.tableWidget_searchfncnasdaq.setGeometry(QtCore.QRect(0, 570, 1411, 221))
        self.tableWidget_searchfncnasdaq.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_searchfncnasdaq.setObjectName("tableWidget_searchfncnasdaq")
        self.tableWidget_searchfncnasdaq.setColumnCount(9)
        self.tableWidget_searchfncnasdaq.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_searchfncnasdaq.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_searchfncnasdaq.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_searchfncnasdaq.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_searchfncnasdaq.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_searchfncnasdaq.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_searchfncnasdaq.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_searchfncnasdaq.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_searchfncnasdaq.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_searchfncnasdaq.setHorizontalHeaderItem(8, item)
        self.tableWidget_searchfncnasdaq.horizontalHeader().setDefaultSectionSize(156)
        self.Financial_select.raise_()
        self.financenasdaq.raise_()
        self.financeset.raise_()
        self.NewsPage = QtWidgets.QWidget(self.All)
        self.NewsPage.setGeometry(QtCore.QRect(30, 80, 1761, 791))
        self.NewsPage.setStyleSheet("background-color: #353535;")
        self.NewsPage.setObjectName("NewsPage")
        self.News_select = QtWidgets.QWidget(self.NewsPage)
        self.News_select.setGeometry(QtCore.QRect(0, 0, 321, 791))
        self.News_select.setStyleSheet("background-color: #E9EBEF;")
        self.News_select.setObjectName("News_select")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.News_select)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 301, 220))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_allnews = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_allnews.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_allnews.setFont(font)
        self.pushButton_allnews.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_allnews.setStyleSheet("background-color: #D2D7DF;")
        self.pushButton_allnews.setObjectName("pushButton_allnews")
        self.verticalLayout_4.addWidget(self.pushButton_allnews)
        self.pushButton_newsset = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_newsset.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_newsset.setFont(font)
        self.pushButton_newsset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_newsset.setStyleSheet("background-color: #D2D7DF;")
        self.pushButton_newsset.setObjectName("pushButton_newsset")
        self.verticalLayout_4.addWidget(self.pushButton_newsset)
        self.pushButton_newsnasdaq = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_newsnasdaq.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_newsnasdaq.setFont(font)
        self.pushButton_newsnasdaq.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_newsnasdaq.setStyleSheet("background-color: #D2D7DF;")
        self.pushButton_newsnasdaq.setObjectName("pushButton_newsnasdaq")
        self.verticalLayout_4.addWidget(self.pushButton_newsnasdaq)
        self.pushButton_newscrypto = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_newscrypto.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_newscrypto.setFont(font)
        self.pushButton_newscrypto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_newscrypto.setStyleSheet("background-color: #D2D7DF;")
        self.pushButton_newscrypto.setObjectName("pushButton_newscrypto")
        self.verticalLayout_4.addWidget(self.pushButton_newscrypto)
        self.NewsSet = QtWidgets.QWidget(self.NewsPage)
        self.NewsSet.setGeometry(QtCore.QRect(350, 0, 1411, 791))
        self.NewsSet.setStyleSheet("background-color: #D2D7DF;")
        self.NewsSet.setObjectName("NewsSet")
        self.tableWidget_newsset = QtWidgets.QTableWidget(self.NewsSet)
        self.tableWidget_newsset.setGeometry(QtCore.QRect(0, 70, 1411, 371))
        self.tableWidget_newsset.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_newsset.setObjectName("tableWidget_newsset")
        self.tableWidget_newsset.setColumnCount(5)
        self.tableWidget_newsset.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_newsset.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_newsset.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_newsset.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_newsset.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_newsset.setHorizontalHeaderItem(4, item)
        self.comboBox_newsset = QtWidgets.QComboBox(self.NewsSet)
        self.comboBox_newsset.setGeometry(QtCore.QRect(100, 20, 1141, 31))
        self.comboBox_newsset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_newsset.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_newsset.setObjectName("comboBox_newsset")
        self.pushButton_updatenewsset = QtWidgets.QPushButton(self.NewsSet)
        self.pushButton_updatenewsset.setGeometry(QtCore.QRect(1260, 20, 141, 31))
        self.pushButton_updatenewsset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_updatenewsset.setStyleSheet("background-color: rgb(225, 255, 228);")
        self.pushButton_updatenewsset.setObjectName("pushButton_updatenewsset")
        self.Spatial_set = QtWidgets.QWidget(self.NewsSet)
        self.Spatial_set.setGeometry(QtCore.QRect(0, 440, 1411, 351))
        self.Spatial_set.setStyleSheet("background-color: rgb(255, 85, 127);")
        self.Spatial_set.setObjectName("Spatial_set")
        self.comboBox_timenewsset = QtWidgets.QComboBox(self.NewsSet)
        self.comboBox_timenewsset.setGeometry(QtCore.QRect(10, 20, 71, 31))
        self.comboBox_timenewsset.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_timenewsset.setObjectName("comboBox_timenewsset")
        self.comboBox_timenewsset.addItem("All")
        self.comboBox_timenewsset.addItem("Today")
        self.comboBox_timenewsset.addItem("3 Days")
        self.comboBox_timenewsset.addItem("Weekly")
        self.comboBox_timenewsset.addItem("Monthly")
        self.NewsNasdaq = QtWidgets.QWidget(self.NewsPage)
        self.NewsNasdaq.setGeometry(QtCore.QRect(350, 0, 1411, 791))
        self.NewsNasdaq.setStyleSheet("background-color: #D2D7DF;")
        self.NewsNasdaq.setObjectName("NewsNasdaq")
        self.tableWidget_newsnasdaq = QtWidgets.QTableWidget(self.NewsNasdaq)
        self.tableWidget_newsnasdaq.setGeometry(QtCore.QRect(0, 70, 1411, 371))
        self.tableWidget_newsnasdaq.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_newsnasdaq.setObjectName("tableWidget_newsnasdaq")
        self.tableWidget_newsnasdaq.setColumnCount(5)
        self.tableWidget_newsnasdaq.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_newsnasdaq.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_newsnasdaq.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_newsnasdaq.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_newsnasdaq.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_newsnasdaq.setHorizontalHeaderItem(4, item)
        self.comboBox_newsnasdaq = QtWidgets.QComboBox(self.NewsNasdaq)
        self.comboBox_newsnasdaq.setGeometry(QtCore.QRect(100, 20, 1141, 31))
        self.comboBox_newsnasdaq.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_newsnasdaq.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_newsnasdaq.setObjectName("comboBox_newsnasdaq")
        self.pushButton_updatenewsnasdaq = QtWidgets.QPushButton(self.NewsNasdaq)
        self.pushButton_updatenewsnasdaq.setGeometry(QtCore.QRect(1260, 20, 141, 31))
        self.pushButton_updatenewsnasdaq.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_updatenewsnasdaq.setStyleSheet("background-color: rgb(225, 255, 228);")
        self.pushButton_updatenewsnasdaq.setObjectName("pushButton_updatenewsnasdaq")
        self.Spatial_nasdaq = QtWidgets.QWidget(self.NewsNasdaq)
        self.Spatial_nasdaq.setGeometry(QtCore.QRect(0, 440, 1411, 351))
        self.Spatial_nasdaq.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.Spatial_nasdaq.setObjectName("Spatial_nasdaq")
        self.comboBox_timenewsnasdaq = QtWidgets.QComboBox(self.NewsNasdaq)
        self.comboBox_timenewsnasdaq.setGeometry(QtCore.QRect(10, 20, 71, 31))
        self.comboBox_timenewsnasdaq.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_timenewsnasdaq.setObjectName("comboBox_timenewsnasdaq")
        self.comboBox_timenewsnasdaq.addItem("All")
        self.comboBox_timenewsnasdaq.addItem("Today")
        self.comboBox_timenewsnasdaq.addItem("3 Days")
        self.comboBox_timenewsnasdaq.addItem("Weekly")
        self.comboBox_timenewsnasdaq.addItem("Monthly")
        self.NewsCrypto = QtWidgets.QWidget(self.NewsPage)
        self.NewsCrypto.setGeometry(QtCore.QRect(350, 0, 1411, 791))
        self.NewsCrypto.setStyleSheet("background-color: #D2D7DF;")
        self.NewsCrypto.setObjectName("NewsCrypto")
        self.tableWidget_newscrypto = QtWidgets.QTableWidget(self.NewsCrypto)
        self.tableWidget_newscrypto.setGeometry(QtCore.QRect(0, 70, 1411, 371))
        self.tableWidget_newscrypto.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_newscrypto.setObjectName("tableWidget_newscrypto")
        self.tableWidget_newscrypto.setColumnCount(5)
        self.tableWidget_newscrypto.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_newscrypto.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_newscrypto.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_newscrypto.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_newscrypto.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_newscrypto.setHorizontalHeaderItem(4, item)
        self.comboBox_newscrypto = QtWidgets.QComboBox(self.NewsCrypto)
        self.comboBox_newscrypto.setGeometry(QtCore.QRect(100, 20, 1141, 31))
        self.comboBox_newscrypto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_newscrypto.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_newscrypto.setObjectName("comboBox_newscrypto")
        self.pushButton_updatenewscrypto = QtWidgets.QPushButton(self.NewsCrypto)
        self.pushButton_updatenewscrypto.setGeometry(QtCore.QRect(1260, 20, 141, 31))
        self.pushButton_updatenewscrypto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_updatenewscrypto.setStyleSheet("background-color: rgb(225, 255, 228);")
        self.pushButton_updatenewscrypto.setObjectName("pushButton_updatenewscrypto")
        self.Spatial_crypto = QtWidgets.QWidget(self.NewsCrypto)
        self.Spatial_crypto.setGeometry(QtCore.QRect(0, 440, 1411, 351))
        self.Spatial_crypto.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.Spatial_crypto.setObjectName("Spatial_crypto")
        self.comboBox_timenewscrypto = QtWidgets.QComboBox(self.NewsCrypto)
        self.comboBox_timenewscrypto.setGeometry(QtCore.QRect(10, 20, 71, 31))
        self.comboBox_timenewscrypto.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_timenewscrypto.setObjectName("comboBox_timenewscrypto")
        self.comboBox_timenewscrypto.addItem("All")
        self.comboBox_timenewscrypto.addItem("Today")
        self.comboBox_timenewscrypto.addItem("3 Days")
        self.comboBox_timenewscrypto.addItem("Weekly")
        self.comboBox_timenewscrypto.addItem("Monthly")
        self.AllNews = QtWidgets.QWidget(self.NewsPage)
        self.AllNews.setGeometry(QtCore.QRect(350, 0, 1411, 791))
        self.AllNews.setStyleSheet("background-color: #D2D7DF;")
        self.AllNews.setObjectName("AllNews")
        self.tableWidget_allnews = QtWidgets.QTableWidget(self.AllNews)
        self.tableWidget_allnews.setGeometry(QtCore.QRect(0, 50, 1411, 741))
        self.tableWidget_allnews.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_allnews.setObjectName("tableWidget_allnews")
        self.tableWidget_allnews.setColumnCount(5)
        self.tableWidget_allnews.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_allnews.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_allnews.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_allnews.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_allnews.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_allnews.setHorizontalHeaderItem(4, item)
        self.comboBox_timenewsall = QtWidgets.QComboBox(self.AllNews)
        self.comboBox_timenewsall.setGeometry(QtCore.QRect(10, 10, 71, 31))
        self.comboBox_timenewsall.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_timenewsall.setObjectName("comboBox_timenewsall")
        self.comboBox_timenewsall.addItem("All")
        self.comboBox_timenewsall.addItem("Today")
        self.comboBox_timenewsall.addItem("3 Days")
        self.comboBox_timenewsall.addItem("Weekly")
        self.comboBox_timenewsall.addItem("Monthly")
        self.News_select.raise_()
        self.NewsNasdaq.raise_()
        self.NewsCrypto.raise_()
        self.NewsSet.raise_()
        self.AllNews.raise_()
        self.Header.raise_()
        self.FinancialPage.raise_()
        self.GraphPage.raise_()
        self.NewsPage.raise_()
        self.DataPage.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1820, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_dataset.clicked.connect(self.tableset.show) # type: ignore
        self.pushButton_datanasdaq.clicked.connect(self.tableset.hide) # type: ignore
        self.pushButton_datacrypto.clicked.connect(self.tableset.hide) # type: ignore
        self.pushButton_dataset.clicked.connect(self.tablenasdaq.hide) # type: ignore
        self.pushButton_datanasdaq.clicked.connect(self.tablenasdaq.show) # type: ignore
        self.pushButton_datacrypto.clicked.connect(self.tablenasdaq.hide) # type: ignore
        self.pushButton_dataset.clicked.connect(self.tablecrypto.hide) # type: ignore
        self.pushButton_datanasdaq.clicked.connect(self.tablecrypto.hide) # type: ignore
        self.pushButton_datacrypto.clicked.connect(self.tablecrypto.show) # type: ignore
        self.pushButton_graph.clicked.connect(self.DataPage.hide) # type: ignore
        self.pushButton_data.clicked.connect(self.DataPage.show) # type: ignore
        self.pushButton_financial.clicked.connect(self.DataPage.hide) # type: ignore
        self.pushButton_news.clicked.connect(self.DataPage.hide) # type: ignore
        self.pushButton_data.clicked.connect(self.GraphPage.hide) # type: ignore
        self.pushButton_graph.clicked.connect(self.GraphPage.show) # type: ignore
        self.pushButton_financial.clicked.connect(self.GraphPage.hide) # type: ignore
        self.pushButton_news.clicked.connect(self.GraphPage.hide) # type: ignore
        self.pushButton_news.clicked.connect(self.NewsPage.show) # type: ignore
        self.pushButton_financial.clicked.connect(self.NewsPage.hide) # type: ignore
        self.pushButton_graph.clicked.connect(self.NewsPage.hide) # type: ignore
        self.pushButton_data.clicked.connect(self.NewsPage.hide) # type: ignore
        self.pushButton_data.clicked.connect(self.FinancialPage.hide) # type: ignore
        self.pushButton_graph.clicked.connect(self.FinancialPage.hide) # type: ignore
        self.pushButton_financial.clicked.connect(self.FinancialPage.show) # type: ignore
        self.pushButton_news.clicked.connect(self.FinancialPage.hide) # type: ignore
        self.pushButton_fncset.clicked.connect(self.financeset.show) # type: ignore
        self.pushButton_fncnasdaq.clicked.connect(self.financeset.hide) # type: ignore
        self.pushButton_fncset.clicked.connect(self.financenasdaq.hide) # type: ignore
        self.pushButton_fncnasdaq.clicked.connect(self.financenasdaq.show) # type: ignore
        self.pushButton_newsset.clicked.connect(self.NewsSet.show) # type: ignore
        self.pushButton_newsnasdaq.clicked.connect(self.NewsSet.hide) # type: ignore
        self.pushButton_newscrypto.clicked.connect(self.NewsSet.hide) # type: ignore
        self.pushButton_newsset.clicked.connect(self.NewsNasdaq.hide) # type: ignore
        self.pushButton_newsnasdaq.clicked.connect(self.NewsNasdaq.show) # type: ignore
        self.pushButton_newscrypto.clicked.connect(self.NewsNasdaq.hide) # type: ignore
        self.pushButton_newsset.clicked.connect(self.NewsCrypto.hide) # type: ignore
        self.pushButton_newsnasdaq.clicked.connect(self.NewsCrypto.hide) # type: ignore
        self.pushButton_newscrypto.clicked.connect(self.NewsCrypto.show) # type: ignore
        self.pushButton_graphset.clicked.connect(self.Webview_set.show) # type: ignore
        self.pushButton_graphnasdaq.clicked.connect(self.Webview_set.hide) # type: ignore
        self.pushButton_graphcrypto.clicked.connect(self.Webview_set.hide) # type: ignore
        self.pushButton_graphset.clicked.connect(self.Webview_nasdaq.hide) # type: ignore
        self.pushButton_graphnasdaq.clicked.connect(self.Webview_nasdaq.show) # type: ignore
        self.pushButton_graphcrypto.clicked.connect(self.Webview_nasdaq.hide) # type: ignore
        self.pushButton_graphset.clicked.connect(self.Webview_crypto.hide) # type: ignore
        self.pushButton_graphnasdaq.clicked.connect(self.Webview_crypto.hide) # type: ignore
        self.pushButton_graphcrypto.clicked.connect(self.Webview_crypto.show) # type: ignore
        self.pushButton_adddata.clicked.connect(self.add_data.show) # type: ignore
        self.pushButton_datacrypto.clicked.connect(self.add_data.hide) # type: ignore
        self.pushButton_datanasdaq.clicked.connect(self.add_data.hide) # type: ignore
        self.pushButton_dataset.clicked.connect(self.add_data.hide) # type: ignore
        self.pushButton_adddata.clicked.connect(self.tableset.hide) # type: ignore
        self.pushButton_adddata.clicked.connect(self.tablecrypto.hide) # type: ignore
        self.pushButton_adddata.clicked.connect(self.tablenasdaq.hide) # type: ignore
        self.pushButton_allnews.clicked.connect(self.AllNews.show) # type: ignore
        self.pushButton_newsset.clicked.connect(self.AllNews.hide) # type: ignore
        self.pushButton_newsnasdaq.clicked.connect(self.AllNews.hide) # type: ignore
        self.pushButton_newscrypto.clicked.connect(self.AllNews.hide) # type: ignore
        self.pushButton_allnews.clicked.connect(self.NewsSet.hide) # type: ignore
        self.pushButton_allnews.clicked.connect(self.NewsNasdaq.hide) # type: ignore
        self.pushButton_allnews.clicked.connect(self.NewsCrypto.hide) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


#-------------------------------------------------------------------- Load All News
        self.load_newsall()
#-------------------------------------------------------------------- Load All Data SET
        self.load_dataset_all()
#-------------------------------------------------------------------- Load All Data NASDAQ
        self.load_datanasdaq_all()
#-------------------------------------------------------------------- Load All Data CRYPTO
        self.load_datacrypto_all()
#-------------------------------------------------------------------- Load All Fnc SET
        self.load_fncset_all()
#-------------------------------------------------------------------- Load All Fnc NASDAQ
        self.load_fncnasdaq_all()
#------------------------------------------------------------------------- WebEngine_SET
        self.WebEngine_set = QtWebEngineWidgets.QWebEngineView(self.Webview_set)
        self.WebEngine_set.setGeometry(QtCore.QRect(0, 0, 1411, 791))
        self.WebEngine_set.setMaximumSize(QtCore.QSize(1411, 16777215))
        self.WebEngine_set.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.WebEngine_set.setObjectName("WebEngine_set")
        self.WebEngine_set.load(QtCore.QUrl("http://127.0.0.1:1000/"))
#------------------------------------------------------------------------- WebEngine_NASDAQ
        self.WebEngine_nasdaq = QtWebEngineWidgets.QWebEngineView(self.Webview_nasdaq)
        self.WebEngine_nasdaq.setGeometry(QtCore.QRect(0, 0, 1411, 791))
        self.WebEngine_nasdaq.setMaximumSize(QtCore.QSize(1411, 16777215))
        self.WebEngine_nasdaq.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.WebEngine_nasdaq.setObjectName("WebEngine_nasdaq")
        self.WebEngine_nasdaq.load(QtCore.QUrl("http://127.0.0.1:2000/"))
#------------------------------------------------------------------------- WebEngine_Crypto
        self.WebEngine_crypto = QtWebEngineWidgets.QWebEngineView(self.Webview_crypto)
        self.WebEngine_crypto.setGeometry(QtCore.QRect(0, 0, 1411, 791))
        self.WebEngine_crypto.setMaximumSize(QtCore.QSize(1411, 16777215))
        self.WebEngine_crypto.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.WebEngine_crypto.setObjectName("WebEngine_crypto")
        self.WebEngine_crypto.load(QtCore.QUrl("http://127.0.0.1:3000/"))
#----------------------------------------------------------------- Combobox Search Data Set
        self.comboBox_dataset.setEditable(True)
        self.comboBox_dataset.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox_dataset.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.comboBox_dataset.currentIndexChanged.connect(self.load_dataset)
        self.comboBox_dataset.currentIndexChanged.connect(self.comboBox_fncset.setCurrentIndex)
        self.comboBox_dataset.currentIndexChanged.connect(self.comboBox_newsset.setCurrentIndex)
#----------------------------------------------------------------- Combobox Search Data Nasdaq
        self.comboBox_datanasdaq.setEditable(True)
        self.comboBox_datanasdaq.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox_datanasdaq.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.comboBox_datanasdaq.currentIndexChanged.connect(self.load_datanasdaq)
        self.comboBox_datanasdaq.currentIndexChanged.connect(self.comboBox_fncnasdaq.setCurrentIndex)
        self.comboBox_datanasdaq.currentIndexChanged.connect(self.comboBox_newsnasdaq.setCurrentIndex)
#----------------------------------------------------------------- Combobox Search Data Crypto
        self.comboBox_datacrypto.setEditable(True)
        self.comboBox_datacrypto.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox_datacrypto.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.comboBox_datacrypto.currentIndexChanged.connect(self.load_datacrypto)
        self.comboBox_datacrypto.currentIndexChanged.connect(self.comboBox_newscrypto.setCurrentIndex)
#----------------------------------------------------------------- Combobox Search Fnc Set
        self.comboBox_fncset.setEditable(True)
        self.comboBox_fncset.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox_fncset.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.comboBox_fncset.currentIndexChanged.connect(self.load_fncset)
        self.comboBox_fncset.currentIndexChanged.connect(self.comboBox_dataset.setCurrentIndex)
        self.comboBox_fncset.currentIndexChanged.connect(self.comboBox_newsset.setCurrentIndex)
#----------------------------------------------------------------- Combobox Search Fnc Nasdaq
        self.comboBox_fncnasdaq.setEditable(True)
        self.comboBox_fncnasdaq.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox_fncnasdaq.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.comboBox_fncnasdaq.currentIndexChanged.connect(self.load_fncnasdaq)
        self.comboBox_fncnasdaq.currentIndexChanged.connect(self.comboBox_datanasdaq.setCurrentIndex)
        self.comboBox_fncnasdaq.currentIndexChanged.connect(self.comboBox_newsnasdaq.setCurrentIndex)
#----------------------------------------------------------------- Combobox Search News Set
        self.comboBox_newsset.setEditable(True)
        self.comboBox_newsset.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox_newsset.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.comboBox_newsset.currentIndexChanged.connect(self.load_newsset)
        self.comboBox_newsset.currentIndexChanged.connect(self.comboBox_dataset.setCurrentIndex)
        self.comboBox_newsset.currentIndexChanged.connect(self.comboBox_fncset.setCurrentIndex)
        self.comboBox_newsset.currentIndexChanged.connect(self.spatial_newsset)
#----------------------------------------------------------------- Combobox Search News Nasdaq
        self.comboBox_newsnasdaq.setEditable(True)
        self.comboBox_newsnasdaq.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox_newsnasdaq.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.comboBox_newsnasdaq.currentIndexChanged.connect(self.load_newsnasdaq)
        self.comboBox_newsnasdaq.currentIndexChanged.connect(self.comboBox_datanasdaq.setCurrentIndex)
        self.comboBox_newsnasdaq.currentIndexChanged.connect(self.comboBox_fncnasdaq.setCurrentIndex)
        self.comboBox_newsnasdaq.currentIndexChanged.connect(self.spatial_newsnasdaq)
#----------------------------------------------------------------- Combobox Search News Crypto
        self.comboBox_newscrypto.setEditable(True)
        self.comboBox_newscrypto.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox_newscrypto.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.comboBox_newscrypto.currentIndexChanged.connect(self.load_newscrypto)
        self.comboBox_newscrypto.currentIndexChanged.connect(self.comboBox_datacrypto.setCurrentIndex)
        self.comboBox_newscrypto.currentIndexChanged.connect(self.spatial_newscrypto)
#----------------------------------------------------------------- Combobox Time News    
        self.comboBox_timenewsall.currentIndexChanged.connect(self.load_newsall)
        self.comboBox_timenewsset.currentIndexChanged.connect(self.load_newsset)
        self.comboBox_timenewsnasdaq.currentIndexChanged.connect(self.load_newsnasdaq)
        self.comboBox_timenewscrypto.currentIndexChanged.connect(self.load_newscrypto)
#------------------------------------------------------------------------- WebEngine Set News
        self.WebEngine_newsset = QtWebEngineWidgets.QWebEngineView(self.Spatial_set)
        self.WebEngine_newsset.setGeometry(QtCore.QRect(0, 0, 1411, 351))
        self.WebEngine_newsset.setMaximumSize(QtCore.QSize(1411, 16777215))
        self.WebEngine_newsset.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.WebEngine_newsset.setObjectName("WebEngine_newsset")
#------------------------------------------------------------------------- WebEngine Nasdaq News
        self.WebEngine_newsnasdaq = QtWebEngineWidgets.QWebEngineView(self.Spatial_nasdaq)
        self.WebEngine_newsnasdaq.setGeometry(QtCore.QRect(0, 0, 1411, 351))
        self.WebEngine_newsnasdaq.setMaximumSize(QtCore.QSize(1411, 16777215))
        self.WebEngine_newsnasdaq.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.WebEngine_newsnasdaq.setObjectName("WebEngine_newsnasdaq")
#------------------------------------------------------------------------- WebEngine Crypto News
        self.WebEngine_newscrypto = QtWebEngineWidgets.QWebEngineView(self.Spatial_crypto)
        self.WebEngine_newscrypto.setGeometry(QtCore.QRect(0, 0, 1411, 351))
        self.WebEngine_newscrypto.setMaximumSize(QtCore.QSize(1411, 16777215))
        self.WebEngine_newscrypto.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.WebEngine_newscrypto.setObjectName("WebEngine_newscrypto")
# #------------------------------------------------------------------------- Update Stock Price
        self.pushButton_updateset.clicked.connect(self.updateSetPrice)
        self.pushButton_updatenasdaq.clicked.connect(self.updateNasdaqPrice)
        self.pushButton_updatecrypto.clicked.connect(self.updateCryptoPrice)
#------------------------------------------------------------------------- Update Financial
        self.pushButton_updatefncset.clicked.connect(self.updateSetFnc)
        self.pushButton_updatefncnasdaq.clicked.connect(self.updateNasdaqFnc)
# #------------------------------------------------------------------------- Update News
        self.pushButton_updatenewsset.clicked.connect(self.updateSetNews)
        self.pushButton_updatenewsnasdaq.clicked.connect(self.updateNasdaqNews)
        self.pushButton_updatenewscrypto.clicked.connect(self.updateCryptoNews)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_data.setText(_translate("MainWindow", "Data"))
        self.pushButton_graph.setText(_translate("MainWindow", "Graph"))
        self.pushButton_financial.setText(_translate("MainWindow", "Financial"))
        self.pushButton_news.setText(_translate("MainWindow", "News"))
        self.pushButton_dataset.setText(_translate("MainWindow", "SET"))
        self.pushButton_datanasdaq.setText(_translate("MainWindow", "NASDAQ"))
        self.pushButton_datacrypto.setText(_translate("MainWindow", "CRYPTO"))
        self.pushButton_adddata.setText(_translate("MainWindow", "ADD DATA"))
        item = self.tableWidget_datanasdaq.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Symbol"))
        item = self.tableWidget_datanasdaq.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_datanasdaq.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Market"))
        item = self.tableWidget_datanasdaq.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Sector"))
        item = self.tableWidget_datanasdaq.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Industry"))
        item = self.tableWidget_searchnasdaq.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Symbol"))
        item = self.tableWidget_searchnasdaq.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_searchnasdaq.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Market"))
        item = self.tableWidget_searchnasdaq.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Sector"))
        item = self.tableWidget_searchnasdaq.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Industry"))
        self.pushButton_updatenasdaq.setText(_translate("MainWindow", "Update"))
        item = self.tableWidget_dataset.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Symbol"))
        item = self.tableWidget_dataset.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_dataset.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Market"))
        item = self.tableWidget_dataset.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Sector"))
        item = self.tableWidget_dataset.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Industry"))
        item = self.tableWidget_dataset.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Description"))
        item = self.tableWidget_searchset.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Symbol"))
        item = self.tableWidget_searchset.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_searchset.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Market"))
        item = self.tableWidget_searchset.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Sector"))
        item = self.tableWidget_searchset.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Industry"))
        item = self.tableWidget_searchset.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Description"))
        self.pushButton_updateset.setText(_translate("MainWindow", "Update"))
        item = self.tableWidget_datacrypto.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Symbol"))
        item = self.tableWidget_datacrypto.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_datacrypto.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Market"))
        item = self.tableWidget_searchcrypto.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Symbol"))
        item = self.tableWidget_searchcrypto.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_searchcrypto.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Market"))
        self.pushButton_updatecrypto.setText(_translate("MainWindow", "Update"))
        self.label_addsymbol.setText(_translate("MainWindow", "Add Stock & Crypto"))
        self.comboBox_marketstock.setItemText(0, _translate("MainWindow", "SET"))
        self.comboBox_marketstock.setItemText(1, _translate("MainWindow", "NASDAQ"))
        self.comboBox_marketstock.setItemText(2, _translate("MainWindow", "CRYPTO"))
        self.pushButton_addstock.setText(_translate("MainWindow", "Submit"))
        self.pushButton_graphset.setText(_translate("MainWindow", "SET"))
        self.pushButton_graphnasdaq.setText(_translate("MainWindow", "NASDAQ"))
        self.pushButton_graphcrypto.setText(_translate("MainWindow", "CRYPTO"))
        self.pushButton_fncset.setText(_translate("MainWindow", "SET"))
        self.pushButton_fncnasdaq.setText(_translate("MainWindow", "NASDAQ"))
        item = self.tableWidget_fncset.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Asset"))
        item = self.tableWidget_fncset.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "TotalDebt"))
        item = self.tableWidget_fncset.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Equity"))
        item = self.tableWidget_fncset.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Revenue"))
        item = self.tableWidget_fncset.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "NetProfit"))
        item = self.tableWidget_fncset.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "ROA"))
        item = self.tableWidget_fncset.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "ROE"))
        item = self.tableWidget_fncset.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Period"))
        item = self.tableWidget_fncset.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Symbol"))
        self.pushButton_updatefncset.setText(_translate("MainWindow", "Update"))
        item = self.tableWidget_searchfncset.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Asset"))
        item = self.tableWidget_searchfncset.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "TotalDebt"))
        item = self.tableWidget_searchfncset.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Equity"))
        item = self.tableWidget_searchfncset.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Revenue"))
        item = self.tableWidget_searchfncset.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "NetProfit"))
        item = self.tableWidget_searchfncset.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "ROA"))
        item = self.tableWidget_searchfncset.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "ROE"))
        item = self.tableWidget_searchfncset.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Period"))
        item = self.tableWidget_searchfncset.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Symbol"))
        item = self.tableWidget_fncnasdaq.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Asset"))
        item = self.tableWidget_fncnasdaq.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "TotalDebt"))
        item = self.tableWidget_fncnasdaq.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Equity"))
        item = self.tableWidget_fncnasdaq.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Revenue"))
        item = self.tableWidget_fncnasdaq.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "NetProfit"))
        item = self.tableWidget_fncnasdaq.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "ROA"))
        item = self.tableWidget_fncnasdaq.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "ROE"))
        item = self.tableWidget_fncnasdaq.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Period"))
        item = self.tableWidget_fncnasdaq.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Symbol"))
        self.pushButton_updatefncnasdaq.setText(_translate("MainWindow", "Update"))
        item = self.tableWidget_searchfncnasdaq.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Asset"))
        item = self.tableWidget_searchfncnasdaq.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "TotalDebt"))
        item = self.tableWidget_searchfncnasdaq.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Equity"))
        item = self.tableWidget_searchfncnasdaq.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Revenue"))
        item = self.tableWidget_searchfncnasdaq.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "NetProfit"))
        item = self.tableWidget_searchfncnasdaq.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "ROA"))
        item = self.tableWidget_searchfncnasdaq.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "ROE"))
        item = self.tableWidget_searchfncnasdaq.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Period"))
        item = self.tableWidget_searchfncnasdaq.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Symbol"))
        self.pushButton_allnews.setText(_translate("MainWindow", "All News"))
        self.pushButton_newsset.setText(_translate("MainWindow", "SET"))
        self.pushButton_newsnasdaq.setText(_translate("MainWindow", "NASDAQ"))
        self.pushButton_newscrypto.setText(_translate("MainWindow", "CRYPTO"))
        item = self.tableWidget_newsset.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget_newsset.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Title"))
        item = self.tableWidget_newsset.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Description"))
        item = self.tableWidget_newsset.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Link"))
        item = self.tableWidget_newsset.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Source"))
        self.pushButton_updatenewsset.setText(_translate("MainWindow", "Update"))
        self.comboBox_timenewsset.setItemText(0, _translate("MainWindow", "All"))
        self.comboBox_timenewsset.setItemText(1, _translate("MainWindow", "Today"))
        self.comboBox_timenewsset.setItemText(2, _translate("MainWindow", "3 Days"))
        self.comboBox_timenewsset.setItemText(3, _translate("MainWindow", "Weekly"))
        self.comboBox_timenewsset.setItemText(4, _translate("MainWindow", "Monthly"))
        item = self.tableWidget_newsnasdaq.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget_newsnasdaq.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Title"))
        item = self.tableWidget_newsnasdaq.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Description"))
        item = self.tableWidget_newsnasdaq.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Link"))
        item = self.tableWidget_newsnasdaq.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Source"))
        self.pushButton_updatenewsnasdaq.setText(_translate("MainWindow", "Update"))
        self.comboBox_timenewsnasdaq.setItemText(0, _translate("MainWindow", "All"))
        self.comboBox_timenewsnasdaq.setItemText(1, _translate("MainWindow", "Today"))
        self.comboBox_timenewsnasdaq.setItemText(2, _translate("MainWindow", "3 Days"))
        self.comboBox_timenewsnasdaq.setItemText(3, _translate("MainWindow", "Weekly"))
        self.comboBox_timenewsnasdaq.setItemText(4, _translate("MainWindow", "Monthly"))
        item = self.tableWidget_newscrypto.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget_newscrypto.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Title"))
        item = self.tableWidget_newscrypto.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Description"))
        item = self.tableWidget_newscrypto.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Link"))
        item = self.tableWidget_newscrypto.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Source"))
        self.pushButton_updatenewscrypto.setText(_translate("MainWindow", "Update"))
        self.comboBox_timenewscrypto.setItemText(0, _translate("MainWindow", "All"))
        self.comboBox_timenewscrypto.setItemText(1, _translate("MainWindow", "Today"))
        self.comboBox_timenewscrypto.setItemText(2, _translate("MainWindow", "3 Days"))
        self.comboBox_timenewscrypto.setItemText(3, _translate("MainWindow", "Weekly"))
        self.comboBox_timenewscrypto.setItemText(4, _translate("MainWindow", "Monthly"))
        item = self.tableWidget_allnews.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget_allnews.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Title"))
        item = self.tableWidget_allnews.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Description"))
        item = self.tableWidget_allnews.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Link"))
        item = self.tableWidget_allnews.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Source"))
        self.comboBox_timenewsall.setItemText(0, _translate("MainWindow", "All"))
        self.comboBox_timenewsall.setItemText(1, _translate("MainWindow", "Today"))
        self.comboBox_timenewsall.setItemText(2, _translate("MainWindow", "3 Days"))
        self.comboBox_timenewsall.setItemText(3, _translate("MainWindow", "Weekly"))
        self.comboBox_timenewsall.setItemText(4, _translate("MainWindow", "Monthly"))


#------------------------------------------------------------------ Column Width Datanasdaq
        self.tableWidget_datanasdaq.setColumnWidth(1, 350)
        self.tableWidget_datanasdaq.setColumnWidth(4, 450)
#------------------------------------------------------------------ Column Width Data Search nasdaq
        self.tableWidget_searchnasdaq.setColumnWidth(1, 350)
        self.tableWidget_searchnasdaq.setColumnWidth(4, 450)
#------------------------------------------------------------------ Column Width Data set
        self.tableWidget_dataset.setColumnWidth(1, 250)
        self.tableWidget_dataset.setColumnWidth(4, 250)
        self.tableWidget_dataset.setColumnWidth(5, 450)
#------------------------------------------------------------------ Column Width Datasearch set
        self.tableWidget_searchset.setColumnWidth(1, 250)
        self.tableWidget_searchset.setColumnWidth(4, 250)
        self.tableWidget_searchset.setColumnWidth(5, 450)
#------------------------------------------------------------------ Column Width News Set
        self.tableWidget_newsset.setColumnWidth(0, 150)
        self.tableWidget_newsset.setColumnWidth(1, 500)
        self.tableWidget_newsset.setColumnWidth(2, 500)
        self.tableWidget_newsset.setColumnWidth(3, 200)
        self.tableWidget_newsset.setColumnWidth(4, 200)
#------------------------------------------------------------------ Column Width News Nasdaq
        self.tableWidget_newsnasdaq.setColumnWidth(0, 150)
        self.tableWidget_newsnasdaq.setColumnWidth(1, 500)
        self.tableWidget_newsnasdaq.setColumnWidth(2, 500)
        self.tableWidget_newsnasdaq.setColumnWidth(3, 200)
        self.tableWidget_newsnasdaq.setColumnWidth(4, 200)
#------------------------------------------------------------------ Column Width News Crypto
        self.tableWidget_newscrypto.setColumnWidth(0, 150)
        self.tableWidget_newscrypto.setColumnWidth(1, 500)
        self.tableWidget_newscrypto.setColumnWidth(2, 500)
        self.tableWidget_newscrypto.setColumnWidth(3, 200)
        self.tableWidget_newscrypto.setColumnWidth(4, 200)
#------------------------------------------------------------------ Column Width All news
        self.tableWidget_allnews.setColumnWidth(0, 150)
        self.tableWidget_allnews.setColumnWidth(1, 500)
        self.tableWidget_allnews.setColumnWidth(2, 500)
        self.tableWidget_allnews.setColumnWidth(3, 200)
        self.tableWidget_allnews.setColumnWidth(4, 200)


#------------------------------------------------------ Name of Stock and Crypto
def combobox_SET():
    conn = sqlite3.connect(r'C:\Users\Admin\Desktop\SOFTDEV2\SOFTWARE-DEVELOPMENT-2\share_V3.sqlite')
    cursor = conn.cursor()
    cursor.execute("""SELECT Symbol FROM Information WHERE MarketId = 1 ORDER BY Symbol ASC""")
    result = cursor.fetchall()
    values = [item[0] for item in result]
    return values
def combobox_NASDAQ():
    conn = sqlite3.connect(r'C:\Users\Admin\Desktop\SOFTDEV2\SOFTWARE-DEVELOPMENT-2\share_V3.sqlite')
    cursor = conn.cursor()
    cursor.execute("""SELECT Symbol FROM Information WHERE MarketId = 2 ORDER BY Symbol ASC""")
    result = cursor.fetchall()
    values = [item[0] for item in result]
    return values
def combobox_CRYPTO():
    conn = sqlite3.connect(r'C:\Users\Admin\Desktop\SOFTDEV2\SOFTWARE-DEVELOPMENT-2\share_V3.sqlite')
    cursor = conn.cursor()
    cursor.execute("""SELECT Symbol FROM Information WHERE MarketId = 3 ORDER BY Symbol ASC""")
    result = cursor.fetchall()
    values = [item[0] for item in result]
    return values

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
#------------------------------------------------------- Set Value Combobox
    ui.comboBox_dataset.addItems(combobox_SET())
    ui.comboBox_fncset.addItems(combobox_SET())
    ui.comboBox_newsset.addItems(combobox_SET())
    ui.comboBox_datanasdaq.addItems(combobox_NASDAQ())
    ui.comboBox_fncnasdaq.addItems(combobox_NASDAQ())
    ui.comboBox_newsnasdaq.addItems(combobox_NASDAQ())
    ui.comboBox_datacrypto.addItems(combobox_CRYPTO())
    ui.comboBox_newscrypto.addItems(combobox_CRYPTO())
    MainWindow.show()
    sys.exit(app.exec_())