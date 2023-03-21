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

    def test_get_id_main(self):
        # "NewId","Date","Title",'Description','Img','Link','Source','Content'
        Title = "Sunrun’s Connection to SVB  May Be Hurting Its Stock"

        with patch('module.sqlite3') as mocksql:

            mocksql.connect().cursor().fetchall.side_effect = [[((2,"Date","Title",'Description','Img','Link','Source','Content'))]]
            mocksql.commit().return_value = ''
            
            tool = Foo()
            result = tool.get_id_News(Title)
     
            assert result ==  '2'

    def test_get_id_Null(self):
        # "NewId","Date","Title",'Description','Img','Link','Source','Content'
        Title = ""

        with patch('module.sqlite3') as mocksql:

            mocksql.connect().cursor().fetchall.side_effect = [[]]
            mocksql.commit().return_value = ''
            
            tool = Foo()
            result = tool.get_id_News(Title)
     
            assert result ==  'None'

    def test_get_id_Not_found(self):
        # "NewId","Date","Title",'Description','Img','Link','Source','Content'
        Title = "Sunrun’s Connection to SVB  May Be Hurting Its Stock"

        with patch('module.sqlite3') as mocksql:

            mocksql.connect().cursor().fetchall.side_effect = [[]]
            mocksql.commit().return_value = ''
            
            tool = Foo()
            result = tool.get_id_News(Title)
     
            assert result ==  'None'

if __name__ == '__main__':
    unittest.main()