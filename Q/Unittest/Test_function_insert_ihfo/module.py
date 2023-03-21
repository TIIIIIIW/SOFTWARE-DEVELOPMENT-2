import pandas as pd
import time
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import unittest
from unittest.mock import Mock
from unittest.mock import patch

class Foo():

    def insert_share(self,data):

        conn = sqlite3.connect(r'AA')
        cur = conn.cursor()
        check_industry_Sector = f"""SELECT count(*) as Have,CategoryShare.IndustryId,CategoryShare.SectorId FROM Industry INNER JOIN  CategoryShare ON Industry.IndustryId = CategoryShare.IndustryId INNER JOIN Sector on Sector.SectorId = CategoryShare.SectorId WHERE Short_Industry = '{data['Industry']}' AND Short_Sector = '{data['Sector']}';"""
        cur.execute(check_industry_Sector)
        records = cur.fetchone()
        print(records)
    
        if records[0] == 0 :

            return "Industry and Sector not match"

        data['IndustryId'],data['SectorId'] = records[1],records[2]
        check_query = f"""SELECT count(*) FROM Information WHERE Symbol = "{data['Symbol']}";"""
        cur.execute(check_query)
        result = cur.fetchone()
        print(result)
        if result[0] == 0:
            # Data does not exist, insert it
            insert_data = f""" INSERT INTO Information("Symbol","Market","Dividend Policy","Business Type","SectorId","IndustryId") VALUES ("{data['Symbol']}","{data['Market']}","{data['Dividend Policy']}","{data['Business Type']}","{data['SectorId']}","{data['IndustryId']}")"""
            cur.execute(insert_data)
            conn.commit()
            conn.close()

            return "Create sussces"

        conn.close()
        return "Symbol already exists"

    def insert_shareV2(self,data,marketId):

        conn = sqlite3.connect(r'')
        cur = conn.cursor()

        check_query = f"""SELECT count(*) FROM Information WHERE Symbol = "{data['Symbol']}" and Sname = "{data['Name']}";"""
        cur.execute(check_query)
        result = cur.fetchone()

        if result[0] == 0:
            # Data does not exist, insert it
            insert_data = f""" INSERT INTO Information("Symbol","Sname",'Description','MarketId') VALUES("{data['Symbol']}","{data['Name']}","{marketId}")"""
            cur.execute(insert_data)
            conn.commit()
            conn.close()
            return "1",data['Symbol']
            
        return "0",data['Symbol']