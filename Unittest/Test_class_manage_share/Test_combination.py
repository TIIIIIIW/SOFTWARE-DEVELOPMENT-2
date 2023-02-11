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

        table_price = pd.DataFrame({'Datetime':["2023-01-09 11:00:00"],'Open':[2.68],'High':[2.68],'Low':[2.64],'Close':[2.66],'Adj Close':[2.66],'Volume':[20062600],'SymbolId':[384]})

        tool = module.Manage_share_database()
        self.symbol_id = MagicMock(return_value={''})
        sqlite3.connect = MagicMock(return_value={''})

        tool.self.con = MagicMock(return_value={''})
        tool.self.cur = MagicMock(return_value={''})
        tool.self.cur.execute = MagicMock(return_value={''})
        tool.self.cur.fetchall = MagicMock(return_value='')

        self.cur.fetchall = MagicMock(return_value=[])
        table_price.to_sql = MagicMock(return_value=2)

        result = tool.combineData('Stock_price_hours',table_price)
        print(result)
        assert result.equals(pd.DataFrame({'Datetime':["2023-01-09 11:00:00"],'Open':[2.68],'High':[2.68],'Low':[2.64],'Close':[2.66],'Adj Close':[2.66],'Volume':[20062600],'SymbolId':[384]}))


if __name__ == '__main__':
    unittest.main()