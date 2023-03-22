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
import plotly
import plotly.graph_objs as go
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import spacy
import numpy
from googletrans import Translator
from geopy.geocoders import Nominatim
from alpha_vantage.fundamentaldata import FundamentalData
from selenium.common.exceptions import NoSuchElementException

class Update_Stock():
    def __init__(self,market) :
        self.location_db = r'C:\Users\JourneyQ\OneDrive - kmutnb.ac.th\Desktop\Quick_file\year_2-S_2\Project_sofedev_2\Manage_Share\Database_convert\share_V3.sqlite'
        self.location_driver = r"C:/Users/JourneyQ/OneDrive - kmutnb.ac.th/Desktop/Quick_file/year_2-S_2/Project_sofedev_2/Schap/chromedriver.exe"
        self.Market = str(market)

    def get_symbol_id(self):
        con = sqlite3.connect(self.location_db)
        cur = con.cursor()
        sql = f"""select Information.Symbol,Information.SymbolId  
                from Information Inner join Market on Market.MarketId = Information.MarketId
                where Market.Mname = "{self.Market}"
                """
        print(sql)
        cur.execute(sql)
        records = cur.fetchall()
        con.close()
        symbol_id = {}
        for share in records: symbol_id[share[0]] = share[1]
        return symbol_id
    
    # ดึงราคหุ้นจาก yfinance รายวัน
    def updateData_Day(self,share):
        if share in self.get_symbol_id().keys():
            start_date = self.get_max_date('Stock_price_day',self.get_symbol_id()[share]) + datetime.timedelta(days=1)
            end_date = (datetime.datetime.now()).strftime('%Y-%m-%d')
            if start_date < (datetime.datetime.strptime(end_date, '%Y-%m-%d')) :
                detail = yf.download(share, interval='1D', start=start_date, end=end_date)
                if not(detail.empty):
                    detail['SymbolId'] = str(int(self.get_symbol_id()[share]))
                    table_price = detail
                    table_price = detail.reset_index()
                    return table_price
        return pd.DataFrame({'Date':[],'Open':[],'High':[],'Low':[],'Close':[],'Adj Close':[],'Volume':[],'SymbolId':[]})
    
    # ดึงราคหุ้นจาก yfinance รายชั่วโมง
    def updateData_hours(self,share):
        if share in self.get_symbol_id().keys():
            max_date = self.get_max_date('Stock_price_hours',self.get_symbol_id()[share])
            start_date =  max_date + datetime.timedelta(hours=1)
            detail = yf.download(share, interval='1h', start=start_date )
            if not(detail.empty):
                # In the case of Python versioin 3.10 and up, comment 2 below.
                # detail.index = detail.index.tz_convert('Asia/Bangkok')
                # detail.index = detail.index.tz_localize(None)
                detail['SymbolId'] = int(self.get_symbol_id()[share])
                table_price = detail.reset_index()
                return table_price
        return pd.DataFrame({'Datetime':[],'Open':[],'High':[],'Low':[],'Close':[],'Adj Close':[],'Volume':[],'SymbolId':[]})

    # นำ dataframe มาเพิ่มลงใน database 
    def combineData(self,stock_name,table_price):
        try :
            if table_price.empty: return ''
            con = sqlite3.connect(self.location_db)
            cur = con.cursor()
            column = {'Stock_price_hours':'Datetime','Stock_price_day':'Date'}
            sql = """ select * from {} where {} = "{}" and SymbolId = "{}" """.format(stock_name,column[stock_name],table_price.iloc[0][column[stock_name]],int(table_price.iloc[0]['SymbolId']))
            cur.execute(sql)
            con.close
            records = cur.fetchall()
            if records == []:
                table_price[column[stock_name]] = pd.to_datetime(table_price[column[stock_name]], format='%Y/%m/%d %H:%M:%S')
                # !!!!!! sensitive function !!!!!!!!!
                new_table = table_price.to_sql(stock_name,con,index=False,if_exists='append')
                con.commit()
                con.close()
                return 'Done Update : ',table_price
            else : return 'Data already in database',pd.DataFrame({'Datetime':[],'Open':[],'High':[],'Low':[],'Close':[],'Adj Close':[],'Volume':[],'SymbolId':[]})
        except KeyError: return 'Table name incorrect',pd.DataFrame({'Datetime':[],'Open':[],'High':[],'Low':[],'Close':[],'Adj Close':[],'Volume':[],'SymbolId':[]})
            
            
    def get_max_date(self,table,share):
        try :
            con = sqlite3.connect(self.location_db)
            cur = con.cursor()
            column = {'Stock_price_hours':'Datetime','Stock_price_day':'Date'}
            sql = """select {} From {} where SymbolId = '{}' ORDER BY {} DESC LIMIT 1;""".format(column[table],table,share,column[table])
            stock_data = pd.read_sql(sql,con)
            con.close()
            stock_data[column[table]] = pd.to_datetime(stock_data[column[table]], format='%Y/%m/%d')
            return max(stock_data[column[table]])
        except ValueError: 
            reverse = {'Date' : 360*50,'Datetime' : 720}
            stock_data = pd.DataFrame(['0'],columns =[column[table]])
            stock_data[column[table]][0] = pd.to_datetime(date.today() - timedelta(days=reverse[column[table]]), format='%Y/%m/%d %H:%M:%S')
            return max(stock_data[f'{column[table]}'])

    def UpdatePicehours(self,share):
        if self.Market in ['SET','NASDAQ','CRYPTO']: return self.combineData('Stock_price_hours',self.updateData_hours(share))
        else : return pd.DataFrame({'Date':[],'Title':[],'NewsId':[],'Date':[],'Title':[],'Description':[],'Img':[],'Link':[],'Source':[],'Content':[]}),{}

    def UpdatePiceDays(self,share):
        if self.Market in ['SET','NASDAQ','CRYPTO']: return self.combineData('Stock_price_day',self.updateData_Day(share))
        else : return pd.DataFrame({'Date':[],'Title':[],'NewsId':[],'Date':[],'Title':[],'Description':[],'Img':[],'Link':[],'Source':[],'Content':[]}),{}
        
    # ----------------------------------------------------------- For News -----------------------------------

    def KaohoonNews(self,share):

        chest,I,tag_share_news  = [],0,{}
        url = requests.get(f"https://www.kaohoon.com/?s={share}")
        soup = BeautifulSoup(url.text, 'html')
        for ultag in soup.find_all('ul', {'class': 'posts-items'}):
            for li in ultag.find_all('li'):
                df,st,tags  = {},'',[]
                text = (li.text).split('\n')
                df['Date'],df['Title'],df['Description'],df['Img'],df['Link'],df['Source'] = text[3],text[4],text[5],li.find('img')['src'],li.find('a')['href'],'kaohoon'
                soup = BeautifulSoup((requests.get(f"{df['Link']}")).text, 'html')
                div = soup.find('div', {'class': 'entry-content entry clearfix'})
                if str(div) == 'None' :  
                    df['Date'],df['Title'],df['Description'],df['Img'],df['Link'],df['Source'],df['Content'] = '','','','','','',''
                    chest.append(df)
                    tag_share_news[df['Title']] = tags
                    break

                for li in div.find_all('p'):
                    text = li.text
                    if text != '':
                        st += li.text + '\n'
                df['Content'] = st
                span = soup.find('span', {'class': 'tagcloud'})
                tags = []
                if str(span) != 'None': tags = [i.text for i in span.find_all('a')]
                tag_share_news[df['Title']] = tags

                if st != '': chest.append(df)
        return  pd.DataFrame(chest),tag_share_news

    def YahooNews(self,share):
        url = requests.get(f"https://finance.yahoo.com/quote/{share}")
        chest,tag_share_news  = [],{}
        soup = BeautifulSoup(url.text, 'html')
        for div_all in soup.find_all('div', {'id': 'quoteNewsStream-0-Stream'}):
            for li in div_all.find_all('li', {'class': 'js-stream-content Pos(r)'}):
                for l in li.find_all('div', {'class': 'Py(14px) Pos(r)'}):
                    df,st,share_tag  = {},'',{}
                    tag_a = l.find('a')
                    # Img
                    tag_img = l.find('img')
                    if str(tag_img) != 'None': url_img = l.find('img')['src']
                    else : url_img = 'https://www.lifewire.com/thmb/yx5oJUJ4fA1TQ0h0pl9FM7Kc4Fo=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/yahoo-logo-2019-879b7bed612d4bbc97065dce2a0f2d73.png'
                    # Get Content -----------------------------------------------------
                    soup_content = BeautifulSoup((requests.get('https://finance.yahoo.com/' + tag_a['href'])).text, 'html')
                    for li_ in soup_content.find_all('p'):
                        text = li_.text
                        if text != '': st += li_.text + '\n'
                    try :        
                        df['Date'],df['Title'],df['Description'],df['Img'],df['Link'],df['Source'],df['Content']  = datetime.datetime.strptime(soup_content.find('time')['datetime'], '%Y-%m-%dT%H:%M:%S.%f%z').strftime('%d/%m/%Y'),tag_a.text,l.find('p').text,url_img,'https://finance.yahoo.com/' + tag_a['href'],'yahoo',st
                        share_news = [i.text for i in soup_content.find_all('div', {'class': 'xray-card-row-title'})]
                        tag_share_news[df['Title']] = share_news
                        chest.append(df)
                    except TypeError: pass
        return pd.DataFrame(chest),tag_share_news
       
    def get_id_News(self,title):
        # connect to the database
        conn,id = sqlite3.connect(self.location_db),''
        c = conn.cursor()
        # search for words in the table
        c.execute(f"""SELECT * FROM News WHERE title="{title}" """)
        results = c.fetchall()
        conn.close()
        if results != []: return str(results[0][0])   
        else : return 'None'

    def Share_finder(self,words,NewsId,source):
        # connect to the database
        words = list(numpy.unique(words))
        conn = sqlite3.connect(self.location_db)
        c = conn.cursor()
        share = []
        for word in words : 
            w = word
            if source == 'kaohoon': 
                if word == 'BAT-3K': word = '3K-BAT'
                w = word + '.BK'
            # search for words in the table
            c.execute(f"""SELECT * FROM Information WHERE Symbol="{w}" or Sname="{word}"; """)
            results = c.fetchall()
            if results != []:
                data = {}
                data['SymbolId'],data['NewsId'] = results[0][0],NewsId
                share.append(data)
        # close the database connection
        conn.close()
        return share
    
    def End_point_FindderNews(self,chest):
        print('--------------------',chest)
        # การใช้งานจริง เลิก comment 3 function sensitive function
        df_news,tag = chest[0],chest[1]
        shareNews = []
        locaNew = []
        column = 'Date,Title,Description,Img,Link,Source,Content'
        data = list(df_news.itertuples(index=False, name=None))
        tool = Update_Stock('SET')
        for i in range(len(data)):

            # ตรวจสอบ News ว่ามีใน database รึยัง
            NewsId = tool.get_id_News(df_news['Title'][i])
            
            if NewsId == 'None':
                # # ถ้าไม่มีจะเพิ่ม แต่ถ้ามีจะแสดงว่าเคยดึงสถานที่กับหุ้นไปแล้วจะหยุดการทำงาน !!!!!! sensitive function !!!!!!!!!
                tool.InsertDB_SqlCommand('News',column,data[i])
                # # # ดึง id ใหม่อีกครั้งจากหุ้นที่พึงเพิ่มเข้าไป
                NewsId = tool.get_id_News(df_news['Title'][i])
                en = Location_finder( df_news['Content'][i] + df_news['Title'][i])

                words = en.Separate_words()
                words = en.filter_special_2(words)
                words += tag[df_news['Title'][i]]
                print(words)
                share = tool.Share_finder(words,NewsId,df_news['Source'][i])
                print(share)
                shareNews += share
                
                loca = en.find_location(words,NewsId)
                locaNew += loca
                
        locainNews = pd.DataFrame(locaNew)
        shareinNews = pd.DataFrame(shareNews)
        # !!!!!! sensitive function !!!!!!!!!
        tool.InsertDB_Pandas('Location_in_News',locainNews)
        # !!!!!! sensitive function !!!!!!!!!
        tool.InsertDB_Pandas('Share_in_News',shareinNews)
        print(locainNews,shareinNews)

        return df_news,locainNews,shareinNews
    
    def UpdateNews(self,share):
        if self.Market == 'SET': return self.End_point_FindderNews(self.KaohoonNews(share.split('.BK')[0]))
        elif self.Market == 'NASDAQ' or self.Market == 'CRYPTO' : return self.End_point_FindderNews(self.YahooNews(share))
        else : return pd.DataFrame({'Date':[],'Title':[],'NewsId':[],'Date':[],'Title':[],'Description':[],'Img':[],'Link':[],'Source':[],'Content':[]}),{}
 
    # ----------------------------------------------------------- For Financial -----------------------------------

    def getStockDetails(self,driver,name):
        sections = ['stock-financial-report','stock-financial-ratio']
        url = 'https://www.finnomena.com/stock/' + name
        driver.get(url)
        quarters = []
        data = []
        for section in sections:
                obj = {}
                keys = []
                headerElements = driver.find_element(By.CSS_SELECTOR,
            f'#{section}>div>div>div>div>div.table-overflow-wrapper>div.topic-wrapper.user-select-none.float-left.overflow-shadow')
                for topic in headerElements.find_elements(By.CLASS_NAME,'topic')[1:]:
                    key = BeautifulSoup(topic.get_attribute('id')).get_text()
                    keys.append(key)
                contentElements = driver.find_element(By.CSS_SELECTOR, 
                                    f'#{section}>div>div>div>div>div.table-overflow-wrapper>div.content-wrapper.user-select-none')
                contentHTML = BeautifulSoup(contentElements.get_attribute('innerHTML'), 'html.parser')
                dataWrapper = contentHTML.find_all('div', {'class': 'data-wrapper'})
                if len(quarters) == 0:
                    for div in contentHTML.find_all('div', {'class': 'year'}):
                        quarters.append(div.get_text())
                for i in range(len(dataWrapper)): 
                    values = [data.get_text() for data in dataWrapper[i].find_all('div', {'class': 'data-each'})]
                    key = f"{keys[i]}"
                    obj[key] = values
                    data.append(obj)
        return (quarters,data)

    def getFinancialDetails(self,symbol,driver):
        quarterlyOrAnnual,responseData = self.getStockDetails(driver,name=symbol)
        data = {}
        for d in responseData:
            data = dict(list(data.items()) + list(d.items()))
        data = {key: data[key] for key in ['Asset', 'TotalDebt', 'Equity', 'Revenue', 'NetProfit', 'ROA', 'ROE']}
        data['Period'] = quarterlyOrAnnual
        data['SymbolId'] = str(int(self.get_symbol_id()[symbol + '.BK']))
        df = pd.DataFrame(data)
        df = df.replace('', '0')
        df = df.iloc[:-1]
        df.iloc[:, :7] = df.iloc[:, :7].applymap(lambda x: x.replace(',', '')).astype(float)
        df = df.replace(0.00, numpy.nan)
        return df

    def FinnomenaDetail(self,driver):
        values = list(self.get_symbol_id().keys())
        nameNoData = ['AURA', 'COMM', 'TRUE']
        details = []
        for name in values:
            name = name[:-3]
            print(name)
            response = requests.get('https://www.finnomena.com/stock/' + name)
            if (response.status_code == 404) or (name in nameNoData):
                continue
            else:
                df = self.getFinancialDetails(driver,symbol=name)
                details.append(df)
        df_new = pd.concat(details)
        return df_new
    
    def updateFinnomena(self,symbol,driver):
        conn = sqlite3.connect(self.location_db)
        df_db = pd.read_sql_query("""SELECT Asset,TotalDebt,Equity,Revenue,NetProfit,ROA,ROE,Period,Symbol,fq.SymbolId FROM Financial_quarterly as fq INNER JOIN Information as i on i.SymbolId = fq.SymbolId""", conn)
        if symbol in ['AURA', 'COMM', 'TRUE']:
            return 'There is no information for this stock.'
        else:
            df_check = pd.read_sql_query(f"""SELECT Asset,TotalDebt,Equity,Revenue,NetProfit,ROA,ROE,Period,Symbol,fq.SymbolId FROM Financial_quarterly as fq INNER JOIN Information as i on i.SymbolId = fq.SymbolId WHERE Symbol = '{str(symbol)+'.BK'}' """, conn)
            data_put = self.getFinancialDetails(symbol,driver).tail(1)
            df_db = df_db.drop(columns=['Symbol'])
            if data_put['Period'].unique() not in df_check['Period'].unique():
                data_put.to_sql('Financial_quarterly', conn, if_exists='append', index=False)
                conn.close()
                return 'Update Success'
            else:
                return 'This data is up to date.'
        
    # ------------------------------------------------------------------------------------------
    def alphaVantage_data(self,symbol):
        apikey = '4YLKM5SFV5RXMQCG'
        fd = FundamentalData(apikey, output_format = 'pandas')
        balance_sheet = fd.get_balance_sheet_quarterly(symbol)
        income_state = fd.get_income_statement_quarterly(symbol)
        balance_sheet = balance_sheet[0].T
        income_state = income_state[0].T
        return (balance_sheet, income_state)

    def calInfo(self,data):
        Equity = (data['totalAssets'] - data['totalLiabilities'])
        NetProfit = (data['grossProfit'] - data['operatingExpenses'])
        ROA_value = (data['netIncome'] / data['totalAssets']) * 100
        ROE_value = (data['netIncome'] / data['totalShareholderEquity']) * 100
        data['Equity'] = Equity
        data['NetProfit'] = NetProfit
        data['ROA'] = ROA_value
        data['ROE'] = ROE_value
        return data
    
    def arrangeAlphaVantageDetail(self,symbol):
        data_balance, data_income = self.alphaVantage_data(symbol)
        result = pd.concat([data_balance, data_income])
        result = result.T.reset_index()
        new_result = result.loc[:,~result.columns.duplicated(keep='first')]
        new_result = new_result.drop(new_result.columns[[0,2]], axis=1)
        new_result['netIncome'] = result['netIncome']
        new_result.iloc[:, 1:] = new_result.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')
        new_result = self.calInfo(new_result)
        new_result['SymbolId'] = str(int(self.get_symbol_id()[symbol]))
        result_after = new_result.drop(new_result.columns[[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,30,
                                            31,32,33,34,35,36,37,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]]
                                            , axis=1)
        result_after = result_after.round(3)
        result_after = result_after.rename(columns={"fiscalDateEnding": "Period", "totalAssets": "Asset", "totalLiabilities": "TotalDebt",
                                    "totalRevenue": "Revenue"})
        result_after = result_after[['Asset', 'TotalDebt', 'Equity', 'Revenue', 'NetProfit', 'ROA', 'ROE', 'Period', 'SymbolId']]
        result_after['Period'] = pd.to_datetime(result_after['Period'])
        result_after = result_after[~(result_after['Period'].isna())]
        result_after = result_after.sort_values(by=['Period'], ascending=True).reset_index(drop=True)
        result_after['Period'] = result_after['Period'].dt.quarter.astype(str) +'Q'+ result_after['Period'].dt.year.astype(str)
        return result_after

    def AlphaVantageDetail(self):
        values = list(self.get_symbol_id().keys())[:50] #ต่อไป 50-100
        nameNoData = ['ACAC', 'ACACU']
        details_alpha = []
        count = 0
        for name in values:
            if name in nameNoData:
                continue
            elif (count == 2):
                time.sleep(65)
                df = self.arrangeAlphaVantageDetail(name)
                details_alpha.append(df)
                count = 0
            else:
                df2 = self.arrangeAlphaVantageDetail(name)
                details_alpha.append(df2)
            count+=1
        df_new = pd.concat(details_alpha)
        return df_new

    def updateAlphaVantage(self,symbol):
        conn = sqlite3.connect(self.location_db)
        df_db = pd.read_sql_query("""SELECT Asset,TotalDebt,Equity,Revenue,NetProfit,ROA,ROE,Period,Symbol,fq.SymbolId FROM Financial_quarterly as fq INNER JOIN Information as i on i.SymbolId = fq.SymbolId ;""", conn)
        if symbol in ['ACAC','ACACU']:
            return 'There is no information for this stock.'
        elif symbol not in df_db['Symbol'].unique():
            data = self.arrangeAlphaVantageDetail(symbol)
            df_db = df_db.drop(columns=['Symbol'])
            df_new = pd.concat([df_db, data])
            df_new.to_sql('Financial_quarterly', conn, if_exists='append', index=False)
            conn.close()
            return 'Update Success.'
        else:
            df_check = pd.read_sql_query(f"""SELECT Asset,TotalDebt,Equity,Revenue,NetProfit,ROA,ROE,Period,Symbol,fq.SymbolId FROM Financial_quarterly as fq INNER JOIN Information as i on i.SymbolId = fq.SymbolId WHERE Symbol = '{str(symbol)}' ;""", conn)
            data_put = self.arrangeAlphaVantageDetail(symbol).tail(1)
            df_db = df_db.drop(columns=['Symbol'])
            if data_put['Period'].unique() not in df_check['Period'].unique():
                data_put.to_sql('Financial_quarterly', conn, if_exists='append', index=False)
                conn.close()
                return 'Update Success.'
            else: return 'This data is up to date.'
                
    def updateFinancial(self,drive,symbol):

        if self.Market == 'SET': return self.updateFinnomena(symbol,drive)
        elif self.Market == 'NASDAQ'  : return self.updateAlphaVantage(symbol)
        else : return 'We have SET and NASDAQ.'
       
    # ----------------------------------------------------------- For all -----------------------------------
    def InsertDB_SqlCommand(self,table_name, column ,data):
        conn = sqlite3.connect(self.location_db)
        c = conn.cursor()
        # Create a string with placeholders for each value in the data tuple
        placeholders = ",".join(["?" for _ in data])
        # Construct the SQL query string
        query_string = f"INSERT INTO {table_name} ({column}) VALUES ({placeholders})"
        # Execute the query and commit the changes
        c.execute(query_string, data)
        conn.commit()
        # Close the connection
        conn.close()
        return 'Succes to add {}'

    def InsertDB_Pandas(self,table,dic):
        df = pd.DataFrame(dic)
        con = sqlite3.connect(self.location_db)
        cur = con.cursor()    
        newshare = df.to_sql(table,con,if_exists='append', index=False)
        con.commit()
        con.close


#--------------------------------------- NASDAQ CRYPTO------------------------------------------------------------


    def Set_up_WebScraping_Info_NASDAQ_CRYPTO(self,share):
        
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(self.location_driver, chrome_options=options)
        driver.get(f"https://finance.yahoo.com/quote/{str(share)}/profile")
        time.sleep(2)

        try :
            driver.find_element(By.XPATH, '//*[@id="myLightboxContainer"]/section/button[2]').click()
            return str(driver.page_source)
        
        except NoSuchElementException :

            return ''

    def get_new_NASDAQ_CRYPTO_info(self,share):
        
        info = {}
        html = self.Set_up_WebScraping_Info_NASDAQ_CRYPTO(share)
        soup = BeautifulSoup(html, 'html')
        company = soup.find('h1', {'class': 'D(ib) Fz(18px)'})

        if str(company) == 'None' : return {}

        info['Symbol'],info['Sname'] = share,(company.text).split(f'({share})')[0][:-1]
        target =  soup.find('div', {'class': 'Pt(10px) smartphone_Pt(20px) Lh(1.7)'})
        info['MarketId'] = 3

        if self.Market == 'NASDAQ' : info['Sector'],info['Industry'],info['MarketId'] = '','',2

        if str(target) != str(None) :

            ind_sec = target.find_all('p',{'class':'D(ib) Va(t)'})
            chest = ind_sec[0].find_all('span',{'class':'Fw(600)'})[:-1]
            info['Sector'] = chest[0].text
            info['Industry'] = chest[1].text

        return info

#--------------------------------------- SET ------------------------------------------------------------
# SET 
    def Set_up_WebScraping_info_SET(self,url):
        
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(self.location_driver, chrome_options=options)
        driver.get(url)
        
        return str(driver.page_source)

    def filter_info(self,text):
        company = ''
        fil = text.replace('\n','').split(' ')
        for word in fil : 
            if word != '' : 
                company += word + ' '

        return company[:-1]

    def get_SET_info(self,share):
        
        info,share = {},str(share)
        html = self.Set_up_WebScraping_info_SET(f"https://www.settrade.com/en/equities/quote/{share}/company-profile/profile")
        soup = BeautifulSoup(html, 'html')
        company_data = soup.find('div', {'class': 'company-cover bg-white border rounded box-shadow p-4 pt-0'})

        if str(company_data) == 'None' : return {}

        info['Symbol'],info['Sname'],info['MarketId'] = share+'.BK',self.filter_info(company_data.find('h3').text),1
        
        Industry_data = soup.find('div', {'class': 'col-12 col-md-6 order-3 order-md-3 mb-3'})
        info['Industry'] = self.filter_info(Industry_data.find('div', {'class': 'fs-14px text-middle-gray m-0'}).text)
        Sector_data = soup.find('div', {'class': 'col-12 col-md-6 order-4 order-md-4 mb-3'})
        info['Sector'] = self.filter_info(Sector_data.find('div', {'class': 'fs-14px text-middle-gray m-0'}).text)

        return info

#--------------------------------------- For all------------------------------------------------------------
    def add_share_info(self,data):
        
        conn = sqlite3.connect(self.location_db)
        
        cur = conn.cursor()
        cur.execute(f"""SELECT count(*) FROM Information WHERE Symbol = '{data['Symbol']}'""")
        records = cur.fetchone()
        
        if records[0] == 0 and data['Symbol'] != '' :

            cur.execute(f"""INSERT INTO Information (Symbol,Sname,MarketId) VALUES (?,?,?)""",(data['Symbol'],data['Sname'],data['MarketId']))
            conn.commit()
            cur.execute(f"Select SymbolId from Information where Symbol = '{data['Symbol']}'")
            records = cur.fetchone()
            
            data['SymbolId'] = records[0]
            conn.close()

            return data
        
        conn.close()
        return {}

    def get_sector(self,data):

        conn = sqlite3.connect(self.location_db)
        
        cur = conn.cursor()
        cur.execute(f"""SELECT count(*),SectorId FROM Sector WHERE Short_Sector = '{data['Sector']}' or Full_Sector = '{data['Sector']}' and MarketId = '{data['MarketId']}' """)
        print(f"""SELECT count(*),SectorId FROM Sector WHERE Short_Sector = '{data['Sector']}' or Full_Sector = '{data['Sector']}' and MarketId = '{data['MarketId']}' """)
        records = cur.fetchone()
        data['SectorId'] = None
        conn.close()
        if records[0] == 1 :
            data['SectorId'] = records[1]

            return data
        
        return data

    def get_Industry(self,data):

        conn = sqlite3.connect(self.location_db)
        
        cur = conn.cursor()
        cur.execute(f"""SELECT count(*),IndustryId FROM Industry WHERE Short_Industry = '{data['Industry']}' or Full_Industry = '{data['Industry']}' and MarketId = '{data['MarketId']}' """)
        records = cur.fetchone()
        data['IndustryId'] = None
        conn.close()
        if records[0] == 1 :
            data['IndustryId'] = records[1]

            return data
        
        return data

    def add_Category_share(self,data):

        conn = sqlite3.connect(self.location_db)
        
        cur = conn.cursor()

        cur.execute(f"""INSERT INTO Category (SymbolId,SectorId,IndustryId) VALUES (?,?,?)""",(data['SymbolId'],data['SectorId'],data['IndustryId']))

        conn.commit()
        cur.execute(f"Select SymbolId from Information where Symbol = '{data['Symbol']}'")
        records = cur.fetchone()
            
        data['SymbolId'] = records[0]

        return data
    
    def add_new_symbol(self,share):

        if self.Market not in ['SET','NASDAQ','CRYPTO'] : return 'Available markets include: SET, NASDAQ, CRYPTO'
        if self.Market == 'SET' : data = self.get_SET_info(share)
        if self.Market == 'NASDAQ' : data = self.get_new_NASDAQ_CRYPTO_info(share)
        if self.Market == 'CRYPTO'  : data = self.get_new_NASDAQ_CRYPTO_info(share+'-USD')
        
        if data == {}: return 'Something wrong'

        data = self.add_share_info(data) 
        
        if data == {}: return f'{share} already in database'
        print(data)
        if self.Market != 'CRYPTO' :

            data = self.get_sector(data)
            data = self.get_Industry(data)
            print(data)
            data = self.add_Category_share(data)

        return f'Add {share} success in database'
        
class Location_finder():
    def __init__(self,text) :      
        self.text = self.translate_text(text)

    def translate_text(self,text):
        detector = Translator()
        dec_lan = ''
        for sec in range(int(len(text)/1000)+1):

            dec_lan += detector.translate(text[1000*sec:1000*(sec+1)],des='en').text
        return dec_lan
    def Separate_words(self):
        w = self.text.split(r'\n')
        for content in w : self.text += content + ' '
        nlp = spacy.load('en_core_web_sm')
        # nlp = en_core_web_sm.load()
        doc = nlp(self.text)
        word = []
        for token in doc.ents:           
            if token.label_ != 'DATE' and token.label_ !='CARDINAL' and token.label_ !='TIME':
                # print(token.text,token.label_)     
                word += token.text.split('"')
        return list(numpy.unique(word))
    
    def filter_special_2(self,words):
    # Define regular expression pattern to match words
        word_filter = []
        # Find all matches of the pattern in the text
        for word in words :
            s = 0
            for ch in word:
                if isinstance(ch , str) and ch.isnumeric(): s = 1
            if s == 0: word_filter.append(word)                  
        return list(numpy.unique(word_filter))

    def find_location(self,words,NewsId):
        geolocator = Nominatim(user_agent="Geolocation")
        loca,extra = [],[]
        for i in words :   
            location = geolocator.geocode(f"{i}", exactly_one=True, namedetails=True, addressdetails=True,timeout=12000, language='en')
            if str(location) != 'None' :
                data = {}
                try :
                    if i in ['Africa', 'Europe', 'Asia', 'North America', 'South America', 'Antarctica', 'Australia','South Pole','North pole'] :
                        data['Lname'],data['Country'],data['Latitude'],data['Longitude'],data['NewsId'] = i,'',location.latitude, location.longitude,NewsId
                    else:
                        data['Lname'],data['Country'],data['Latitude'],data['Longitude'],data['NewsId'] = i,location.raw['address']['country'],location.latitude, location.longitude,NewsId
                    loca.append(data)
                except KeyError: extra.append(i)                   
        return loca
