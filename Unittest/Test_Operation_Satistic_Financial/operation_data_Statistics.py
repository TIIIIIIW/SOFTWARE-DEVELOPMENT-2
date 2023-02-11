import pandas as pd
import numpy as np
import unittest


class AdditionTestCase(unittest.TestCase):

    def test_operation_data_main(self):

        data = {'Statistics as of': ['Last Price (Baht)', 'Market Cap. (M.Baht)', 'F/S Period (As of date)', 'P/E', 'P/BV', 'Book Value per share (Baht)', 'Dividend Yield (%)']
        , '30 Dec 2019': ['53.25', '126085.94', '30 Sep 2019', '-', '5.17', '10.30', '1.90']
        , '30 Dec 2020': ['33.25', '78729.72', '30 Sep 2020', '14.78', '3.27', '10.16', '8.63'], '30 Dec 2021': ['45.75', '108327.35', '30 Sep 2021', '31.26', '5.42', '8.44', '6.54'], '30 Dec 2022': ['46.75', '110695.16', '30 Sep 2022', '46.33', '6.19', '7.55', '4.49'], '06 Jan 2023': ['46.50', '110103.21', '30 Sep 2022', '46.08', '6.16', '7.55', '4.52']}
        
        # Create DataFrame
        df = pd.DataFrame(data)
        result = operation_data('DTAC',df)

        assert result.equals(pd.DataFrame({'Statistics as of': ['30 Dec 2019', '30 Dec 2020', '30 Dec 2021', '30 Dec 2022', '06 Jan 2023']
        , 'Last Price (Baht)': ['53.25', '33.25', '45.75', '46.75', '46.50']
        , 'Market Cap. (M.Baht)': ['126085.94', '78729.72', '108327.35', '110695.16', '110103.21']
        , 'F/S Period (As of date)': ['30 Sep 2019', '30 Sep 2020', '30 Sep 2021', '30 Sep 2022', '30 Sep 2022']
        , 'P/E': ['-', '14.78', '31.26', '46.33', '46.08'], 'P/BV': ['5.17', '3.27', '5.42', '6.19', '6.16']
        , 'Book Value per share (Baht)': ['10.30', '10.16', '8.44', '7.55', '7.55'], 'Dividend Yield (%)': ['1.90', '8.63', '6.54', '4.49', '4.52']
        , 'Symbol': ['DTAC', 'DTAC', 'DTAC', 'DTAC', 'DTAC']}))



def operation_data(stock,dataframe):
    
    Statistics_df = (dataframe.set_index("Statistics as of")).T

    Statistics_df['Symbol'] = stock
    Statistics_df = Statistics_df.reset_index()
    Statistics_df = Statistics_df.rename(columns = {"index":"Statistics as of"})

    return Statistics_df

def cha(df):

    d = {}
    m = [df['Statistics as of'].tolist(),df['Last Price (Baht)'].tolist(),
        df['Market Cap. (M.Baht)'].tolist(),df['F/S Period (As of date)'].tolist()
        ,df['P/E'].tolist(),df['P/BV'].tolist(),df['Book Value per share (Baht)'].tolist()
        ,df['Dividend Yield (%)'].tolist(),df['Symbol'].tolist()]
    k = 0
    for i in df.columns:
        
        d[i] = m[k]
        k+=1
    
    return pd.DataFrame(d)

    
if __name__ == '__main__':
    unittest.main()