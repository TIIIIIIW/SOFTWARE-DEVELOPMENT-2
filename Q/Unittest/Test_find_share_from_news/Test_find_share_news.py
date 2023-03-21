# from module import Foo
import unittest
import sqlite3
from unittest.mock import Mock
from unittest.mock import patch
from googletrans import Translator
from unittest.mock import MagicMock
from module import Foo

class AdditionTestCase(unittest.TestCase):

    def test_insertData_info_main(self):

        data = ['Cat','Dog','ADVAN']

        with patch('module.sqlite3') as mocksql:

            mocksql.connect().cursor().fetchall.side_effect = [[],[],[(0,'ADVAN','Sname','Description','1')]]
            tool = Foo()
            result = tool.search_share_in_table(data,1,'kaohoon')
   
            assert (result) ==  ([{'SymbolId': 0, 'NewsId': 1}], ['Cat', 'Dog'])


    def test_insertData_info_not_found(self):

        data = ['Cat','Dog','Fox']

        with patch('module.sqlite3') as mocksql:

            mocksql.connect().cursor().fetchall.side_effect = [[],[],[]]
            tool = Foo()
            result = tool.search_share_in_table(data,1,'kaohoon')

            assert (result) ==  ([], ['Cat', 'Dog','Fox'])

    def test_insertData_Null(self):

        data = []

        with patch('module.sqlite3') as mocksql:

            mocksql.connect().cursor().fetchall.side_effect = []
            tool = Foo()
            result = tool.search_share_in_table(data,1,'kaohoon')

            assert (result) ==  ([], [])

if __name__ == '__main__':
    unittest.main()