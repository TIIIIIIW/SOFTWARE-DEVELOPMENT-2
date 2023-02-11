import pandas as pd
import html5lib
import time
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import datetime
import pandas as pd
import module
import unittest
from unittest.mock import Mock
from unittest.mock import patch

class upda():

    def Check_Statistics(self,table,df,time):
        
        location_db = r'C:\Users\JourneyQ\OneDrive - kmutnb.ac.th\Desktop\Quick_file\year_2-S_2\softdev-2\Set_dataframe_to_sqlite3\share.sqlite'
        con = sqlite3.connect(location_db)
        cur = con.cursor()
        
        sql = """select "{}" From {} where SymbolId = '{}' and "{}" = '{}' LIMIT 1
        """.format("Statistics as of",table,int(df.iloc[[0]]['SymbolId']),
                "Statistics as of",str(time))

        cur.execute(sql)
        records = cur.fetchall()
        con.close()

        return not(bool(records))

    def new_Statistics(self,Statistics_df):
        data_new_year = []
        r = 0
        for time in (Statistics_df['Statistics as of'].tolist())[:-1]:

            Nhave = self.Check_Statistics('Satistics_year',Statistics_df.iloc[[r]],time)

            if Nhave :

                data_new_year.append(Statistics_df.iloc[[r]])

            r+=1
        
        if data_new_year :
            
            return pd.concat(data_new_year)
        
        return pd.DataFrame({'Statistics as of': []
            , 'Last Price (Baht)': []
            , 'Market Cap. (M.Baht)': []
            , 'F/S Period (As of date)': []
            , 'P/E': [], 'P/BV': []
            , 'Book Value per share (Baht)': [], 'Dividend Yield (%)': []
            , 'SymbolId': []})


class AdditionTestCase(unittest.TestCase):

    def test_updateData_Statistics_main(self):

        data = {'Statistics as of': ['2019-12-30', '2020-12-30', '2021-12-30', '2022-12-30', '2023-01-06']
        , 'Last Price (Baht)': ['53.25', '33.25', '45.75', '46.75', '46.50']
        , 'Market Cap. (M.Baht)': ['126085.94', '78729.72', '108327.35', '110695.16', '110103.21']
        , 'F/S Period (As of date)': ['2019-09-30', '2020-09-30', '2021-09-30', '2022-09-30','2023-01-06']
        , 'P/E': ['-', '14.78', '31.26', '46.33', '46.08']
        , 'P/BV': ['5.17', '3.27', '5.42', '6.19', '6.16']
        , 'Book Value per share (Baht)': ['10.30', '10.16', '8.44', '7.55', '7.55']
        , 'Dividend Yield (%)': ['1.90', '8.63', '6.54', '4.49', '4.52']
        , 'SymbolId': ['4', '4', '4', '4', '4']}
                
        df = pd.DataFrame(data)

        with patch.object(upda, 'Check_Statistics', side_effect=[True,True,True,True]) as mock_method:

            tool = upda()
            result = tool.new_Statistics(df)

            assert result.equals(pd.DataFrame({'Statistics as of': ['2019-12-30', '2020-12-30', '2021-12-30', '2022-12-30']
                    , 'Last Price (Baht)': ['53.25', '33.25', '45.75', '46.75']
                    , 'Market Cap. (M.Baht)': ['126085.94', '78729.72', '108327.35', '110695.16']
                    , 'F/S Period (As of date)': ['2019-09-30', '2020-09-30', '2021-09-30', '2022-09-30']
                    , 'P/E': ['-', '14.78', '31.26', '46.33'] 
                    , 'P/BV': ['5.17', '3.27', '5.42', '6.19']
                    , 'Book Value per share (Baht)': ['10.30', '10.16', '8.44', '7.55']
                    , 'Dividend Yield (%)': ['1.90', '8.63', '6.54', '4.49']
                    , 'SymbolId': ['4', '4', '4', '4']}))

    
    def test_updateData_Statistics_main1(self):

        data = {'Statistics as of': ['2019-12-30', '2020-12-30', '2021-12-30', '2022-12-30', '2023-01-06']
        , 'Last Price (Baht)': ['53.25', '33.25', '45.75', '46.75', '46.50']
        , 'Market Cap. (M.Baht)': ['126085.94', '78729.72', '108327.35', '110695.16', '110103.21']
        , 'F/S Period (As of date)': ['2019-09-30', '2020-09-30', '2020-09-30', '2021-03-31', '30 Sep 2022']
        , 'P/E': ['-', '14.78', '31.26', '46.33', '46.08']
        , 'P/BV': ['5.17', '3.27', '5.42', '6.19', '6.16']
        , 'Book Value per share (Baht)': ['10.30', '10.16', '8.44', '7.55', '7.55']
        , 'Dividend Yield (%)': ['1.90', '8.63', '6.54', '4.49', '4.52']
        , 'SymbolId': ['4', '4', '4', '4', '4']}

        df = pd.DataFrame(data)
        with patch.object(upda, 'Check_Statistics', side_effect=[False,False,True,True]) as mock_method:

            tool = upda()
            result = tool.new_Statistics(df)
            result = result.reset_index()
            del result['index']
            
            assert result.equals(pd.DataFrame({'Statistics as of': ['2021-12-30', '2022-12-30']
                    , 'Last Price (Baht)': ['45.75', '46.75']
                    , 'Market Cap. (M.Baht)': ['108327.35', '110695.16']
                    , 'F/S Period (As of date)': ['2020-09-30', '2021-03-31']
                    , 'P/E': ['31.26', '46.33'] 
                    , 'P/BV': ['5.42', '6.19']
                    , 'Book Value per share (Baht)': ['8.44', '7.55']
                    , 'Dividend Yield (%)': ['6.54', '4.49']
                    , 'SymbolId': ['4', '4']}))

    def test_updateData_Statistics_main2(self):

        data = {'Statistics as of': ['2019-12-30', '2020-12-30', '2021-12-30', '2022-12-30', '2023-01-06']
        , 'Last Price (Baht)': ['53.25', '33.25', '45.75', '46.75', '46.50']
        , 'Market Cap. (M.Baht)': ['126085.94', '78729.72', '108327.35', '110695.16', '110103.21']
        , 'F/S Period (As of date)': ['2019-09-30', '2020-09-30', '2020-09-30', '2021-03-31', '30 Sep 2022']
        , 'P/E': ['-', '14.78', '31.26', '46.33', '46.08']
        , 'P/BV': ['5.17', '3.27', '5.42', '6.19', '6.16']
        , 'Book Value per share (Baht)': ['10.30', '10.16', '8.44', '7.55', '7.55']
        , 'Dividend Yield (%)': ['1.90', '8.63', '6.54', '4.49', '4.52']
        , 'SymbolId': ['4', '4', '4', '4', '4']}

        df = pd.DataFrame(data)
        with patch.object(upda, 'Check_Statistics', side_effect=[False,False,False,False]) as mock_method:

            tool = upda()
            result = tool.new_Statistics(df)
            result = result.reset_index()
            del result['index']
            
            assert result.equals(pd.DataFrame({'Statistics as of': []
            , 'Last Price (Baht)': []
            , 'Market Cap. (M.Baht)': []
            , 'F/S Period (As of date)': []
            , 'P/E': [], 'P/BV': []
            , 'Book Value per share (Baht)': [], 'Dividend Yield (%)': []
            , 'SymbolId': []}))



if __name__ == '__main__':
    unittest.main()




