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
from sqlite3 import IntegrityError

class AdditionTestCase(unittest.TestCase):

    def test_updateData_info_main(self):

        data = {'Symbol':"ADA","Market":"SET","Dividend Policy":"reduce","Business Type":"make enegy","Industry":"AGRO","Sector":"FOOD","SymbolId":628}

        with patch('module.sqlite3') as mocksql:

            mocksql.connect().cursor().fetchone.side_effect = [(1,1,1),(1,)]
            mocksql.commit().return_value = ''
            tool = Foo()
            result = tool.update_share_info(data)
            assert result ==  "Update succeed"

    def test_updateData_info_industry_Sector_not_match(self):

        data = {'Symbol':"ADA","Market":"SET","Dividend Policy":"reduce","Business Type":"make enegy","Industry":"AGRO","Sector":"กาพ","SymbolId":628}

        with patch('module.sqlite3') as mocksql:

            mocksql.connect().cursor().fetchone.side_effect = [(0,None,None)]
            mocksql.commit().return_value = ''
            tool = Foo()
            result = tool.update_share_info(data)

            assert result == "Industry and Sector not match" 

    def test_updateData_Symbol_already_with_another_share(self):

        data = {'Symbol':"TU","Market":"SET","Dividend Policy":"reduce","Business Type":"make enegy","Industry":"AGRO","Sector":"FOOD","SymbolId":628}

        with patch('module.sqlite3') as mocksql:

            mocksql.connect().cursor().fetchone.side_effect = [(1,1,1),(1,0,0)]
            mocksql.connect().commit.side_effect = IntegrityError
            tool = Foo()
            result = tool.update_share_info(data)

            assert result == "This Symbol already exist."


    def test_updateData_SymbolId_not_exist(self):

        data = {'Symbol':"ADA","Market":"SET","Dividend Policy":"reduce","Business Type":"make enegy","Industry":"AGRO","Sector":"FOOD","SymbolId":628}

        with patch('module.sqlite3') as mocksql:

            mocksql.connect().cursor().fetchone.side_effect = [(1,1,1),(0,0,0)]
            tool = Foo()
            result = tool.update_share_info(data)

            assert result == "SymbolId does not exist in the system."
            
if __name__ == '__main__':
    unittest.main()