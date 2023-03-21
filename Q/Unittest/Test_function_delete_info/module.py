import pandas as pd
import time
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


class Foo():
        
    def delete_share(self,id):

        conn = sqlite3.connect(r'AA')
        cur = conn.cursor()

        cur.execute(f"""SELECT count(*) FROM Information WHERE SymbolId = '{id}'""")
        records = cur.fetchone()

        if records[0] == 0 :

            return "SymbolId does not exist."

        de_query =  f"""DELETE FROM Information WHERE SymbolId='{id}'"""

        cur.execute(de_query)
        conn.commit()
        conn.close()

        return "Delete successfully"