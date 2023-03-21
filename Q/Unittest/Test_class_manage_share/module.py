import pandas as pd
import html5lib
import time
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import mplfinance as mpf
from datetime import datetime, timedelta
import plotly
import plotly.graph_objs as go
import datetime
import pandas as pd

class Manage_share_database():
    
    def __init__(self):
        
        self.con = sqlite3.connect( r'C:\Users\JourneyQ\OneDrive - kmutnb.ac.th\Desktop\Quick_file\year_2-S_2\softdev-2\Set_dataframe_to_sqlite3\share.sqlite')
        self.cur = self.con.cursor()
        self.symbol_id =  self.get_symbol_id()
        
    def get_symbol_id(self):
        
        sql = """select Symbol,SymbolId 
                from Information
                """
        self.cur.execute(sql)
        records = self.cur.fetchall()
        symbol_id = {}
        
        for share in records:
            
            symbol_id[share[0]] = share[1]
        
        return symbol_id
    
    def updateData_Day(self,ticker):
    
        if ticker[:-3] in self.symbol_id.keys():
            
            
            start_date = self.get_max_date('Stock_price_day',self.symbol_id[ticker[:-3]]) + datetime.timedelta(days=1)
            end_date = (datetime.datetime.now()).strftime('%Y-%m-%d')

            if start_date < (datetime.datetime.strptime(end_date, '%Y-%m-%d')) :
                detail = yf.download(ticker, interval='1D', start=start_date, end=end_date)
                detail['SymbolId'] = self.symbol_id[ticker[:-3]]
                table_price = detail.reset_index()
                return table_price

        return pd.DataFrame({'Date':[],'Open':[],'High':[],'Low':[],'Close':[],'Adj Close':[],'Volume':[],'SymbolId':[]})

    def updateData_hours(self,ticker):

        if ticker[:-3] in self.symbol_id.keys():
            
            start_date = self.get_max_date('Stock_price_hours',self.symbol_id[ticker[:-3]]) + datetime.timedelta(hours=1)

            detail = yf.download(ticker, interval='1h', start=start_date )
            detail['SymbolId'] = self.symbol_id[ticker[:-3]]
            table_price = detail.reset_index()
            return table_price
          
        return pd.DataFrame({'Datetime':[],'Open':[],'High':[],'Low':[],'Close':[],'Adj Close':[],'Volume':[],'SymbolId':[]})


    def combineData(self,stock_name,table_price):
        
        try :
            column = {'Stock_price_hours':'Datetime','Stock_price_day':'Date'}
            sql = """
                    select * 
                    from {}
                    where {} = "{}" and SymbolId = "{}"

                    """.format(stock_name,column[stock_name],table_price.iloc[0][column[stock_name]],str(table_price.iloc[0]['SymbolId']))
            self.cur.execute(sql)
            records = self.cur.fetchall()

            if records == []:

                new_table = table_price.to_sql(stock_name,self.con,index=False,if_exists='append')
                self.con.commit()
                return new_table

            else :

                return 'Data already in database'

        except KeyError:
            
            return 'Table name incorrect'
        
    def get_max_date(self,table,share):
    
        
        try :
            column = {'Stock_price_hours':'Datetime','Stock_price_day':'Date'}

            sql = """select {} From {} where SymbolId = '{}' ORDER BY {} DESC LIMIT 1;
            """.format(column[table],table,share,column[table])

            stock_data = pd.read_sql(sql,self.con)
            stock_data[column[table]] = pd.to_datetime(stock_data[column[table]], format='%Y/%m/%d')

            return max(stock_data[column[table]])
        
        except KeyError:
            
            return "Table or Share incorret"
