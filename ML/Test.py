import pandas as pd
import yfinance as yf
from datetime import datetime
import unittest
from unittest.mock import patch

#--------------------------------------------------------------------------------------------------------#

def getData(tickers) :
    data = []
    if tickers == [] :
        return 'No stock name'
    for ticker in tickers:
        detail = yf.download(ticker, interval='1d')
        detail['Symbol'] = ticker[:-3]
        table_price = detail.reset_index()
        data.append(table_price)
    return data


class Testgetdata(unittest.TestCase):
    def test_getData(self):
        tickers = ['ACE.BK', 'KBANK.BK']
        data = getData(tickers)
        self.assertIsInstance(data, list)
        self.assertIsInstance(data[0], pd.DataFrame)
        
        for ticker, df in zip(tickers, data):
            symbol = ticker[:-3]
            self.assertEqual(df['Symbol'].unique()[0], symbol)

    def test_getDataNoInput(self):
        tickers = []
        data = getData(tickers)
        self.assertEqual(data, 'No stock name')

#--------------------------------------------------------------------------------------------------------#

def updateData(tickers):
    if tickers == []:
        return 'No stock name'
    stock_data = pd.read_csv('stock_dataTest.csv')
    new_data = [stock_data]
    stock_data['Datetime'] = pd.to_datetime(stock_data['Datetime'], format='%Y/%m/%d')
    start_date = max(stock_data['Datetime'])
    today_date = datetime.now()
    for ticker in tickers:
        detail = yf.download(ticker, interval='1h', start=start_date, end=today_date)
        detail['Symbol'] = ticker[:-3]
        table_price = detail.reset_index()
        new_data.append(table_price)
    new_table = pd.concat(new_data)
    duplicate = new_table[['Datetime','Symbol']].duplicated(keep='first')
    new_table = new_table.drop(new_table[duplicate].index)
    new_table = new_table.sort_values(by=['Symbol', 'Datetime'], ascending=True)
    new_table.to_csv('stock_dataTest.csv', index=False)


class Testupdatedata(unittest.TestCase):
    def test_updateNoInput(self):
        result = updateData([])
        self.assertEqual(result, 'No stock name')

    # @patch('stock_dataTest.csv')
    # @patch('yf.download')
    # def test_updateData(self, mock_yf_download, mock_csv):


#--------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
    unittest.main()