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


    def test_updateData_hours_main(self):

        data_f = {'Datetime':["2023-01-09 11:00:00"],'Open':[2.68],'High':[2.68],'Low':[2.64],'Close':[2.66],'Adj Close':[2.66],'Volume':[20062600]}

        tool = module.Manage_share_database()
        self.symbol_id = MagicMock(return_value={'BGRIM':'384'})
        self.get_max_date = MagicMock(return_value=datetime.datetime.strptime("2023-01-09 11:00:00", '%Y-%m-%d %H:%M:%S'))
        yf.download = MagicMock(return_value=pd.DataFrame(data_f).set_index('Datetime'))
 
        result = tool.updateData_hours('BGRIM.BK')

        assert result.equals(pd.DataFrame({'Datetime':["2023-01-09 11:00:00"],'Open':[2.68],'High':[2.68],'Low':[2.64],'Close':[2.66],'Adj Close':[2.66],'Volume':[20062600],'SymbolId':[384]}))


if __name__ == '__main__':
    unittest.main()