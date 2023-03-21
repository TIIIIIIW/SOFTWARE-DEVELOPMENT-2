import pandas as pd
import html5lib
import time
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import mplfinance as mpf
from datetime import datetime, timedelta,date
import datetime
import plotly.graph_objs as go
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options



class Manage_share_database():
    
    def __init__(self):
                
        self.location_db = r'C:\Users\JourneyQ\OneDrive - kmutnb.ac.th\Desktop\Quick_file\year_2-S_2\Project_sofedev_2\Manage_Share\Database_convert\share_V2.sqlite'
        
    def get_symbol_id(self,market):
        
        con = sqlite3.connect(self.location_db)
        cur = con.cursor()
        
        sql = f"""select Information.Symbol,Information.SymbolId  
                from Information Inner join Market on Market.MarketId = Information.MarketId
                where Market.Mname = "{market}"
                """

        cur.execute(sql)
        records = cur.fetchall()
        con.close()
        symbol_id = {}
        
        for share in records:
            
            symbol_id[share[0]] = share[1]
        
        return symbol_id
    
    # ดึงราคหุ้นจาก yfinance รายวัน
    def updateData_Day(self,ticker,market):

        if ticker in self.get_symbol_id(market).keys():
            
            start_date = self.get_max_date('Stock_price_day',self.get_symbol_id(market)[ticker]) + datetime.timedelta(days=1)
            
            end_date = (datetime.datetime.now()).strftime('%Y-%m-%d')

            if start_date < (datetime.datetime.strptime(end_date, '%Y-%m-%d')) :

                detail = yf.download(ticker, interval='1D', start=start_date, end=end_date)

                if not(detail.empty):

                    detail['SymbolId'] = str(int(self.get_symbol_id(market)[ticker]))
                    table_price = detail
                    table_price = detail.reset_index()

                    return table_price

        return pd.DataFrame({'Date':[],'Open':[],'High':[],'Low':[],'Close':[],'Adj Close':[],'Volume':[],'SymbolId':[]})
    
    # ดึงราคหุ้นจาก yfinance รายชั่วโมง
    def updateData_hours(self,ticker,market):

        if ticker in self.get_symbol_id(market).keys():
            
            
            max_date = self.get_max_date('Stock_price_hours',self.get_symbol_id(market)[ticker])
            start_date =  max_date + datetime.timedelta(hours=1)
       
            detail = yf.download(ticker, interval='1h', start=start_date )

            if not(detail.empty):

                detail.index = detail.index.tz_convert('Asia/Bangkok')
                detail.index = detail.index.tz_localize(None)
                detail['SymbolId'] = int(self.get_symbol_id(market)[ticker])
                table_price = detail.reset_index()
            
                return table_price
          
        return pd.DataFrame({'Datetime':[],'Open':[],'High':[],'Low':[],'Close':[],'Adj Close':[],'Volume':[],'SymbolId':[]})

    # นำ dataframe มาเพิ่มลงใน database 
    def combineData(self,stock_name,table_price):
        
        try :
            
            if table_price.empty:
                return ''
            
            con = sqlite3.connect(self.location_db)
            cur = con.cursor()
            column = {'Stock_price_hours':'Datetime','Stock_price_day':'Date'}
            sql = """ select * from {} where {} = "{}" and SymbolId = "{}" """.format(stock_name,column[stock_name],table_price.iloc[0][column[stock_name]],int(table_price.iloc[0]['SymbolId']))
            print(sql)
            cur.execute(sql)
            con.close
            records = cur.fetchall()

            if records == []:

                table_price[column[stock_name]] = pd.to_datetime(table_price[column[stock_name]], format='%Y/%m/%d %H:%M:%S')
                new_table = table_price.to_sql(stock_name,con,index=False,if_exists='append')
                con.commit()
                
                return 'Done Update : ',new_table

            else :

                return 'Data already in database'

        except KeyError:
            
            return 'Table name incorrect'
        
    def get_max_date(self,table,share):
    
        
        try :
            
            con = sqlite3.connect(self.location_db)
            cur = con.cursor()
            
            column = {'Stock_price_hours':'Datetime','Stock_price_day':'Date'}

            sql = """select {} From {} where SymbolId = '{}' ORDER BY {} DESC LIMIT 1;
            """.format(column[table],table,share,column[table])

            stock_data = pd.read_sql(sql,con)
            con.close()

            stock_data[column[table]] = pd.to_datetime(stock_data[column[table]], format='%Y/%m/%d')

            return max(stock_data[column[table]])
        
        except ValueError: 
            reverse = {'Date' : 360*50,'Datetime' : 720}
            stock_data = pd.DataFrame(['0'],columns =[column[table]])
            stock_data[column[table]][0] = pd.to_datetime(date.today() - timedelta(days=reverse[column[table]]), format='%Y/%m/%d %H:%M:%S')
            return max(stock_data[f'{column[table]}'])
    
          
# Update Statistics--------------------------------------------------

    def Check_Statistics(self,table,df,time):

        location_db = r'C:\Users\JourneyQ\OneDrive - kmutnb.ac.th\Desktop\Quick_file\year_2-S_2\softdev-2\Set_dataframe_to_sqlite3\share.sqlite'
        con = sqlite3.connect(location_db)
        cur = con.cursor()

        sql = """select "{}" From {} where SymbolId = '{}' and "{}" = '{}' LIMIT 1
        """.format("Statistics as of",table,int(df.iloc[[0]]['SymbolId']),
                   "Statistics as of",str(time))

        cur.execute(sql)
        records = cur.fetchall()
        con.close()

        return not(bool(records))

    def new_Statistics(self,Statistics_df):
        data_new_year = []
        r = 0
        for time in (Statistics_df['Statistics as of'].tolist())[:-1]:

            Nhave = self.Check_Statistics('Satistics_year',Statistics_df.iloc[[r]],time)

            if Nhave :

                data_new_year.append(Statistics_df.iloc[[r]])

            r+=1

        if data_new_year :

            return pd.concat(data_new_year)

        return pd.DataFrame({'Statistics as of': []
            , 'Last Price (Baht)': []
            , 'Market Cap. (M.Baht)': []
            , 'F/S Period (As of date)': []
            , 'P/E': [], 'P/BV': []
            , 'Book Value per share (Baht)': [], 'Dividend Yield (%)': []
            , 'SymbolId': []})

#-----------------------------------------------------------------------------------------
