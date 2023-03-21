import pandas as pd
import html5lib
import time
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import mplfinance as mpf
from datetime import datetime, timedelta
import datetime
import pandas as pd
import module
import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from module import Manage_share_database

class AdditionTestCase(unittest.TestCase):


    def test_updateData_hours_main(self):

        data_f = {'Datetime':["2023-01-11 00:00:00+00:00"],'Open':[2.68],'High':[2.68],'Low':[2.64],'Close':[2.66],'Adj Close':[2.66],'Volume':[20062600]}
        data_f['Datetime']= pd.to_datetime(data_f['Datetime'])

        tool = module.Manage_share_database()
        tool.get_max_date = MagicMock(return_value=datetime.datetime.strptime("2023-01-10", '%Y-%m-%d'))
        tool.get_symbol_id = MagicMock(return_value={'BGRIM.BK':'386'})
        yf.download = MagicMock(return_value=pd.DataFrame(data_f).set_index('Datetime'))
        
        result = tool.updateData_hours('BGRIM.BK','SET')

        ans = pd.DataFrame({'Datetime':["2023-01-11 07:00:00"],'Open':[2.68],'High':[2.68],'Low':[2.64],'Close':[2.66],'Adj Close':[2.66],'Volume':[20062600],'SymbolId':['386']})
        ans['Datetime']= pd.to_datetime(ans['Datetime'])

        assert str(result) == str(ans)

    def test_updateData_hours_name_not_found(self):

        data_f = {'Datetime':["2023-01-11 00:00:00+00:00"],'Open':[2.68],'High':[2.68],'Low':[2.64],'Close':[2.66],'Adj Close':[2.66],'Volume':[20062600]}

        tool = module.Manage_share_database()
        tool.get_max_date = MagicMock(return_value=datetime.datetime.strptime("2023-01-10", '%Y-%m-%d'))
        tool.get_symbol_id = MagicMock(return_value={'BGRIM.BK':'386'})
        yf.download = MagicMock(return_value=pd.DataFrame(data_f).set_index('Datetime'))

        result = tool.updateData_hours('DEMO','SET')

        assert result.equals(pd.DataFrame({'Datetime':[],'Open':[],'High':[],'Low':[],'Close':[],'Adj Close':[],'Volume':[],'SymbolId':[]}))


    def test_updateData_hours_Null(self):

        data_f = {'Datetime':[],'Open':[],'High':[],'Low':[],'Close':[],'Adj Close':[],'Volume':[]}

        tool = module.Manage_share_database()
        tool.get_max_date = MagicMock(return_value=datetime.datetime.strptime("2023-01-10", '%Y-%m-%d'))
        tool.get_symbol_id = MagicMock(return_value={'BGRIM.BK':'386'})
        yf.download = MagicMock(return_value=pd.DataFrame(data_f).set_index('Datetime'))

        result = tool.updateData_hours('DEMO','SET')

        assert result.equals(pd.DataFrame({'Datetime':[],'Open':[],'High':[],'Low':[],'Close':[],'Adj Close':[],'Volume':[],'SymbolId':[]}))

    
    def test_updateData_hours_Start_morethan(self):

        data_f = {'Datetime':[],'Open':[],'High':[],'Low':[],'Close':[],'Adj Close':[],'Volume':[]}

        tool = module.Manage_share_database()
        tool.get_max_date = MagicMock(return_value=datetime.datetime.strptime("2024-01-10", '%Y-%m-%d'))
        tool.get_symbol_id = MagicMock(return_value={'BGRIM.BK':'386'})
        yf.download = MagicMock(return_value=pd.DataFrame(data_f).set_index('Datetime'))

        result = tool.updateData_hours('BGRIM.BK','SET')

        assert result.equals(pd.DataFrame({'Datetime':[],'Open':[],'High':[],'Low':[],'Close':[],'Adj Close':[],'Volume':[],'SymbolId':[]}))



if __name__ == '__main__':
    unittest.main()