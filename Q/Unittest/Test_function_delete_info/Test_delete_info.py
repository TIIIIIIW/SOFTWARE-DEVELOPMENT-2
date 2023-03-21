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

    def test_deleteData_info_main(self):

        id = 628

        with patch('module.sqlite3') as mocksql:

            mocksql.connect().cursor().fetchone.side_effect = [(1,)]
            mocksql.commit().return_value = ''
            tool = Foo()
            result = tool.delete_share(id)
            assert result ==  "Delete successfully"


    def test_deleteData_info_id_misformed(self):

        id = 'ก'

        with patch('module.sqlite3') as mocksql:

            mocksql.connect().cursor().fetchone.side_effect = [(0,)]
            mocksql.commit().return_value = ''
            tool = Foo()
            result = tool.delete_share(id)
            assert result ==  "SymbolId does not exist."

if __name__ == '__main__':
    unittest.main()