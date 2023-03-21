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
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium.webdriver.chrome.options import Options

class Stock_Share():
    
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
    
    def get_set50_100_from_web(self,amoung):

        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome(r"C:\Users\JourneyQ\OneDrive - kmutnb.ac.th\Desktop\Quick_file\year_2-S_2\softdev-2\week2\chromedriver.exe", chrome_options=options)
        driver.get("https://www.set.or.th/en/market/index/set{}/overview".format(amoung))
        data = driver.page_source
        data_df = pd.read_html(data)[2]

        return data_df['Symbol  (Click to sort Ascending)'].tolist()

    def get_set50_100(self,amoung):

        datas = self.get_set50_100_from_web(amoung)
        share = []

        for data in datas:

            share.append(data.split()[0])

        return share
    
    def get_share_info(self,share):
        
        sql = """select I.Symbol,I.Market,I."Dividend Policy",I."Business Type",Ind.Full_Industry,S.Full_Sector
                from ((Information as I
                inner join Sector as S on I.SectorId = S.SectorId)
                inner join Industry as Ind on I.IndustryId = Ind.IndustryId)
                where Symbol = "{}"
                """.format(share)
        self.cur.execute(sql)
        records = self.cur.fetchall()
        
        if records != [] :
            
            return records[0]
        
        return 'Stock information not found.'
    
    def get_share_Financial(self,share):
        
        sql = """select F."Period as of",F."Assets",F."Liabilities",F."Equity" ,F."Paid-up Capital",F."Revenue",
                F."Profit (Loss) from Other Activities",F."Net Profit",F."EPS (Baht)",F."ROA (%)",F."ROE (%)",F."Net Profit Margin (%)",Ind.Symbol
                from (Financial as F 
                inner join Information as Ind on F.SymbolId = Ind.SymbolId )
                where Symbol = '{}'
                """.format(share)
        
        stock_data = pd.read_sql(sql,self.con)
    
        return stock_data
    
    def get_share_Satistics(self,share):
        
        sql = """select S."Statistics as of",S."Last Price (Baht)",S."Market Cap. (M.Baht)",S."F/S Period (As of date)",S."P/E",
                S."P/BV",S."Book Value per share (Baht)",S."Dividend Yield (%)",Ind."Symbol"
                from (Satistics as S
                inner join Information as Ind on S.SymbolId = Ind.SymbolId )
                where Symbol = '{}'
                """.format(share)
        
        stock_data = pd.read_sql(sql,self.con)
    
        return stock_data
    
    # plot --------------------------------------------------------------------------
    
    def Plot_Candle_hours(self,share):

        sql = """
        select * From Stock_price_hours
        Inner join Information
        on Information.SymbolId = Stock_price_hours.SymbolId
        Where Symbol = "{}"
        ORDER BY Datetime DESC
        LIMIT 100;
        """.format(share)

        df1h = pd.read_sql(sql,self.con)

        df1h['Datetime'] = pd.to_datetime(df1h['Datetime'])
        my_range = pd.date_range(start= min(df1h['Datetime']), end= max(df1h['Datetime']), freq='H')
        missing_datetime = my_range.difference(df1h['Datetime']).strftime("%Y-%m-%d H%:m%:s%").tolist()
        fig = go.Figure(data=[go.Candlestick(
                                x=df1h['Datetime'],
                                open=df1h['Open'],
                                high=df1h['High'],
                                low=df1h['Low'],
                                close=df1h['Close']
        )])

        fig.update_xaxes(
            rangebreaks=[
                dict(bounds=[17, 10], pattern="hour"),
                dict(values=missing_datetime, dvalue=3600000)
            ])

        fig.show()
        
    def Plot_Candle_Day(self,share):

        sql = """
        select * From Stock_price_day
        Inner join Information
        on Information.SymbolId = Stock_price_day.SymbolId
        Where Symbol = "{}"
        ORDER BY Date DESC
        LIMIT 100;
        """.format(share)
        df1d = pd.read_sql(sql,self.con)

        df1d['Date'] = pd.to_datetime(df1d['Date'])
        my_range = pd.date_range(start= min(df1d['Date']), end= max(df1d['Date']), freq='B')
        missing_date = my_range.difference(df1d['Date']).strftime("%Y-%m-%d").tolist()

        fig = go.Figure(data=[go.Candlestick(
                                x=df1d['Date'],
                                open=df1d['Open'],
                                high=df1d['High'],
                                low=df1d['Low'],
                                close=df1d['Close']
        )])

        fig.update_xaxes(
            rangebreaks=[
                dict(bounds=["sat", "mon"]),
                dict(values=missing_date) 
        ])

        fig.show()