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
from geopy.geocoders import Nominatim
class AdditionTestCase(unittest.TestCase):

    def test_insertData_info_main(self):

        data = {'Symbol':"ADAG","Name":"Adagene Inc. American Depositary Shares","Description":"make enegy"}

        with patch('module.sqlite3') as mocksql:

            mocksql.connect().cursor().fetchone.side_effect = [(0,)]
            mocksql.commit().return_value = ''
            tool = Foo()
            result = tool.insert_shareV2(data,1)
     
            assert (result)==  ("1",'ADAG')


    def test_insertData_already(self):

        data = {'Symbol':"ADAG","Name":"Adagene Inc. American Depositary Shares","Description":"make enegy"}

        with patch('module.sqlite3') as mocksql:

            mocksql.connect().cursor().fetchone.side_effect = [(1,)]
            mocksql.commit().return_value = ''
            tool = Foo()
            result = tool.insert_shareV2(data,1)
 
            assert (result)==  ("0",'ADAG')

    def test_insertData_Null(self):

        data = {'Symbol':"","Name":"","Description":""}

        with patch('module.sqlite3') as mocksql:

            mocksql.connect().cursor().fetchone.side_effect = [(1,)]
            mocksql.commit().return_value = ''
            tool = Foo()
            result = tool.insert_shareV2(data,1)
 
            assert (result)==  ("0",'')

if __name__ == '__main__':
    unittest.main()