import pandas as pd
import yfinance as yf
from datetime import datetime
import unittest
from unittest.mock import patch, MagicMock

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

def readCSV(name):
    stock_data = pd.read_csv(name)
    stock_data['Datetime'] = pd.to_datetime(stock_data['Datetime'], format='%Y/%m/%d')
    start_date = max(stock_data['Datetime'])
    return start_date, stock_data

def updateData(ticker, start_date):
    detail = yf.download(ticker, interval='1h', start=start_date)
    detail['Symbol'] = ticker[:-3]
    table_price = detail.reset_index()
    return table_price

def combineData(stock_data, table_price):
    new_data = [stock_data]
    new_data.append(table_price)
    new_table = pd.concat(new_data)
    duplicate = new_table[['Datetime','Symbol']].duplicated(keep='first')
    new_table = new_table.drop(new_table[duplicate].index)
    new_table = new_table.sort_values(by=['Symbol', 'Datetime'], ascending=True)
    # new_table.to_csv('stock_dataTest.csv', index=False)
    return new_table


class Testupdatedata(unittest.TestCase):
    def test_updateData(self):
        mock_yfinance = MagicMock()
        yf.download = mock_yfinance
        mock_yfinance.download.return_value = pd.DataFrame({
            'Open': [10],'High': [15],'Low': [5],'Close': [10],
            'Adj Close': [10],'Volume': [100]},
             index=[pd.to_datetime('2020-01-01', format='%Y/%m/%d')]).rename_axis('Datetime')

        with unittest.mock.patch('yfinance.download', mock_yfinance.download):

            result = updateData('test.bk', pd.to_datetime('2022-12-30', format='%Y/%m/%d'))

            assert result.equals(pd.DataFrame({
                'Datetime': [pd.to_datetime('2020-01-01', format='%Y/%m/%d')],
                'Open': [10],'High': [15],'Low': [5],'Close': [10],
                'Adj Close': [10],'Volume': [100],'Symbol': ['test']
            }))

    def test_combineData(self):
        table_price = pd.DataFrame({
                'Datetime': [pd.to_datetime('2020-01-01', format='%Y/%m/%d')],
                'Open': [10], 'High': [15], 'Low': [5], 'Close': [10],'Adj Close': [10], 
                'Volume': [100], 'Symbol': ['test']})

        stock_data = pd.DataFrame({
                'Datetime': [pd.to_datetime('2020-01-02', format='%Y/%m/%d')],
                'Open': [10], 'High': [15], 'Low': [5], 'Close': [10], 'Adj Close': [10],
                'Volume': [100], 'Symbol': ['test']})

        result = combineData(stock_data, table_price).reset_index(drop=True)

        assert result.equals(pd.DataFrame({
                'Datetime': [pd.to_datetime('2020-01-01', format='%Y/%m/%d'), 
                             pd.to_datetime('2020-01-02', format='%Y/%m/%d')],
                'Open': [10,10], 'High': [15,15], 'Low': [5,5],
                'Close': [10,10], 'Adj Close': [10,10], 'Volume': [100,100],
                'Symbol': ['test','test']
            }))

#--------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
    unittest.main()