import pandas as pd
import yfinance as yf
import unittest

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


class Test(unittest.TestCase):
    def test_getData(self):
        tickers = ['ACE.BK', 'KBANK.BK']
        data = getData(tickers)
        self.assertIsInstance(data, list)
        self.assertIsInstance(data[0], pd.DataFrame)
        
        for ticker, df in zip(tickers, data):
            symbol = ticker[:-3]
            self.assertEqual(df['Symbol'].unique()[0], symbol)

    def test_getData_noInput(self):
        result = getData([])
        assert result == 'No stock name'

if __name__ == '__main__':
    unittest.main()