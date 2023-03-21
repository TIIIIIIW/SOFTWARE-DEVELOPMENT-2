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
import module
import unittest
from unittest.mock import MagicMock



class AdditionTestCase(unittest.TestCase):


    def test_get_max_date_main(self):

        # Mock Function 
        tool = module.Manage_share_database()
        data_f = {'Datetime':["2023-01-09 11:00:00"]}
        pd.read_sql = MagicMock(return_value=pd.DataFrame(data_f))

        result = str(tool.get_max_date('Stock_price_hours',"374"))

        assert result == "2023-01-09 11:00:00"

    def test_get_max_date_main2(self):

        tool = module.Manage_share_database()
        data_f = {'Date':["2023-01-09"]}
        pd.read_sql = MagicMock(return_value=pd.DataFrame(data_f))

        result = str(tool.get_max_date('Stock_price_day',"374"))
        assert result == "2023-01-09 00:00:00"
     
    def test_get_max_date_main3(self):

        tool = module.Manage_share_database()
        data_f = {'Date':["2023-01-09"]}
        pd.read_sql = MagicMock(return_value=pd.DataFrame(data_f))

        result = str(tool.get_max_date('',""))
        assert result == "Table or Share incorret"

    def test_updateData_Day_main(self):

        data_f = {'Date':["2023-01-09 11:00:00"],'Open':[2.68],'High':[2.68],'Low':[2.64],'Close':[2.66],'Adj Close':[2.66],'Volume':[20062600]}

        tool = module.Manage_share_database()
        self.symbol_id = MagicMock(return_value={'BGRIM':'384'})
        self.get_max_date = MagicMock(return_value=datetime.datetime.strptime("2023-01-09", '%Y-%m-%d'))
        yf.download = MagicMock(return_value=pd.DataFrame(data_f).set_index('Date'))

        result = tool.updateData_Day('BGRIM.BK')

        assert result.equals(pd.DataFrame({'Date':["2023-01-09 11:00:00"],'Open':[2.68],'High':[2.68],'Low':[2.64],'Close':[2.66],'Adj Close':[2.66],'Volume':[20062600],'SymbolId':[384]}))


    def test_updateData_Day_main1(self):

        data_f = {'Date':["2023-01-09 11:00:00"],'Open':[2.68],'High':[2.68],'Low':[2.64],'Close':[2.66],'Adj Close':[2.66],'Volume':[20062600]}

        tool = module.Manage_share_database()
        self.symbol_id = MagicMock(return_value={'BGRIM':'384'})
        self.get_max_date = MagicMock(return_value=datetime.datetime.strptime("2023-01-09", '%Y-%m-%d'))
        yf.download = MagicMock(return_value=pd.DataFrame(data_f).set_index('Date'))

        result = tool.updateData_Day('DEMO')

        assert result.equals(pd.DataFrame({'Date':[],'Open':[],'High':[],'Low':[],'Close':[],'Adj Close':[],'Volume':[],'SymbolId':[]}))

    def test_updateData_Day_main2(self):

        data_f = {'Date':[],'Open':[],'High':[],'Low':[],'Close':[],'Adj Close':[],'Volume':[]}

        tool = module.Manage_share_database()
        self.symbol_id = MagicMock(return_value={'BGRIM':'384'})
        self.get_max_date = MagicMock(return_value=datetime.datetime.strptime("2023-01-09", '%Y-%m-%d'))
        yf.download = MagicMock(return_value=pd.DataFrame(data_f).set_index('Date'))

        result = tool.updateData_Day('BGRIM')

        assert result.equals(pd.DataFrame({'Date':[],'Open':[],'High':[],'Low':[],'Close':[],'Adj Close':[],'Volume':[],'SymbolId':[]}))


if __name__ == '__main__':
    unittest.main()