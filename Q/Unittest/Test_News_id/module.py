import pandas as pd
import time
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import unittest
from unittest.mock import Mock
from unittest.mock import patch

class Foo():

    def get_id_News(self,title):
        # connect to the database
        conn = sqlite3.connect(r'')
        c = conn.cursor()
        id = ''
        # search for words in the table
        c.execute(f"""SELECT * FROM News WHERE title="{title}" """)
        results = c.fetchall()

        if results != []: id = str(results[0][0])
            
        else : id = 'None'

        # close the database connection
        conn.close()

        return id