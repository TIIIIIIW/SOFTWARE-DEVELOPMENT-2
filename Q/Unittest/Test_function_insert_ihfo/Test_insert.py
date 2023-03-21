import pandas as pd
import time
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import unittest
from unittest.mock import Mock
from unittest.mock import patch
from module import Foo

class AdditionTestCase(unittest.TestCase):

    def test_insertData_info_main(self):

        data = {'Symbol':"ADA","Market":"SET","Dividend Policy":"reduce","Business Type":"make enegy","Industry":"AGRO","Sector":"FOOD"}

        with patch('module.sqlite3') as mocksql:

            mocksql.connect().cursor().fetchone.side_effect = [(1,1,1),(0,)]
            mocksql.commit().return_value = ''
            tool = Foo()
            result = tool.insert_share(data)
            assert result ==  "Create sussces"

    def test_insertData_info_industry_Sector_not_match(self):

        data = {'Symbol':"ADA","Market":"SET","Dividend Policy":"reduce","Business Type":"make enegy","Industry":"AGRO","Sector":"กาพ"}

        with patch('module.sqlite3') as mocksql:

            mocksql.connect().cursor().fetchone.side_effect = [(0,None,None)]
            mocksql.commit().return_value = ''
            tool = Foo()
            result = tool.insert_share(data)
            print(result)
            assert result == "Industry and Sector not match" 

    def test_insertData_already(self):

        data = {'Symbol':"ADA","Market":"SET","Dividend Policy":"reduce","Business Type":"make enegy","Industry":"AGRO","Sector":"FOOD"}

        with patch('module.sqlite3') as mocksql:

            mocksql.connect().cursor().fetchone.side_effect = [(1,1,1),(1,0,0)]
            mocksql.commit().return_value = ''
            tool = Foo()
            result = tool.insert_share(data)
            print(result)
            assert result == "Symbol already exists" 

if __name__ == '__main__':
    unittest.main()