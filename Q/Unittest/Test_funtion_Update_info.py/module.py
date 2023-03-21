import pandas as pd
import time
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from sqlite3 import IntegrityError
import unittest
from unittest.mock import Mock
from unittest.mock import patch


class Foo():

    def update_share_info(self,data):
        
        conn = sqlite3.connect(r'AA')
        
        cur = conn.cursor()
        cur.execute(f"""SELECT count(*) as Have,CategoryShare.IndustryId,CategoryShare.SectorId FROM Industry INNER JOIN  CategoryShare ON Industry.IndustryId = CategoryShare.IndustryId INNER JOIN Sector on Sector.SectorId = CategoryShare.SectorId WHERE Short_Industry = '{data['Industry']}' AND Short_Sector = '{data['Sector']}';""")
        records = cur.fetchone()
        if records[0] == 0 :

            return "Industry and Sector not match"
        
        data['IndustryId'],data['SectorId'] = records[1],records[2]
        cur.execute(f"""SELECT count(*) FROM Information WHERE SymbolId = {data['SymbolId']}""")
        records = cur.fetchone()
        
        if records[0] == 0 :

            return "SymbolId does not exist in the system."

        try :
        
            cur.execute( f"""UPDATE Information SET  Symbol = "{data['Symbol']}", Market = "{data['Market']}", "Dividend Policy" = "{data['Dividend Policy']}","Business Type" = "{data['Business Type']}","SectorId" = "{data['SectorId']}","IndustryId" = "{data['IndustryId']}" WHERE SymbolId = {data['SymbolId']};""")
            conn.commit()
            conn.close()
            return "Update succeed"
            
        except IntegrityError :
            
            return "This Symbol already exist."