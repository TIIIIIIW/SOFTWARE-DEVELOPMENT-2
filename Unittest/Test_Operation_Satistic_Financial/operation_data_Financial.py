import pandas as pd
import numpy as np
import unittest


class AdditionTestCase(unittest.TestCase):

    def test_operation_data_main(self):

        data = {'Period as of': ['Financial Data', 'Assets', 'Liabilities', 'Equity', 'Paid-up Capital', 'Revenue', 'Profit (Loss) from Other Activities', 'Net Profit', 'EPS (Baht)', 'Financial Ratio', 'ROA (%)', 'ROE (%)', 'Net Profit Margin (%)'],
                "Y/E 2018 31 Dec 2018": [np.nan, 150957.66, 129027.98, 21929.06, 4735.62, 75539.25, -5.32, -4368.69, -1.85, np.nan, -3.35, -17.08, -5.78],
                'Y/E 2019 31 Dec 2019': [np.nan, 167338.82, 142372.4, 24966.41, 4735.62, 81228.2, -23.97, 5421.89, 2.29, np.nan, 6.07, 23.12, 6.67],
                'Y/E 2020 31 Dec 2020': [np.nan, 174280.39, 149964.96, 24315.42, 4735.62, 78883.4, 317.97, 5107.12, 2.16, np.nan, 5.16, 20.73, 6.47],
                'Y/E 2021 31 Dec 2021': [np.nan, 164314.65, 144147.17, 20167.48, 4735.62, 81458.06, -148.62, 3355.93, 1.42, np.nan, 4.0, 15.09, 4.12],
                '9M/2022 30 Sep 2022': [np.nan, 157189.26, 139302.23, 17887.03, 4735.62, 60141.27, -32.72, 2218.27, 0.94, np.nan, 3.51, 12.61, 3.69],       
            }
        
        # Create DataFrame
        df = pd.DataFrame(data)
        result = operation_data('AAV',df)

        assert result.equals(pd.DataFrame({'Period as of': ['Y/E 2018 31 Dec 2018', 'Y/E 2019 31 Dec 2019', 'Y/E 2020 31 Dec 2020', 'Y/E 2021 31 Dec 2021', '9M/2022 30 Sep 2022'],
        "Assets": [150957.66, 167338.82, 174280.39, 164314.65, 157189.26],
        'Liabilities': [129027.98, 142372.4, 149964.96, 144147.17, 139302.23],
        'Equity': [21929.06, 24966.41, 24315.42, 20167.48, 17887.03],
        'Paid-up Capital': [4735.62, 4735.62, 4735.62, 4735.62, 4735.62],
        'Revenue': [75539.25, 81228.2, 78883.4, 81458.06, 60141.27],
        'Profit (Loss) from Other Activities': [-5.32, -23.97, 317.97, -148.62, -32.72],
        "Net Profit": [-4368.69, 5421.89, 5107.12, 3355.93, 2218.27],
        "EPS (Baht)": [-1.85, 2.29, 2.16, 1.42, 0.94],
        "ROA (%)": [-3.35, 6.07, 5.16, 4.0, 3.51],
        "ROE (%)": [-17.08, 23.12, 20.73, 15.09, 12.61],
        "Net Profit Margin (%)": [-5.78, 6.67, 6.47, 4.12, 3.69],
        "Symbol": ['AAV', 'AAV', 'AAV', 'AAV', 'AAV']
       }))



def operation_data(stock,dataframe):
    
    Financial_df = (dataframe.set_index("Period as of")).T
    Financial_df = Financial_df.drop(["Financial Data","Financial Ratio"], axis=1)

    Financial_df['Symbol'] = stock
    Financial_df = Financial_df.reset_index()
    Financial_df = Financial_df.rename(columns = {'index':"Period as of"},index = {"Period as of" : " "})

    return Financial_df

if __name__ == '__main__':
    unittest.main()