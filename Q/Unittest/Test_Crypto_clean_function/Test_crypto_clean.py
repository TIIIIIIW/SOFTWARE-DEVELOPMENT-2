import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import unittest
from unittest.mock import Mock
from unittest.mock import patch
from module import Foo


class AdditionTestCase(unittest.TestCase):

    def test_main(self):

        df = pd.DataFrame({'Unnamed: 0':'NaN','#':[1],'ชื่อ':['Bitcoin1BTC'],'ราคา':['฿848,831.70']
            ,'1h %':['0.22%'],'24h %':['0.33%'],'7d %':['11.37%'],'มูลค่าตามราคาตลาด':['฿16.38T฿16,382,068,054,821']
            ,'Volume(24h)':['฿623,877,196,085735,250 BTC'],'อุปทานหมุนเวียน':['19,295,925 BTC'],'7 วันล่าสุด':['NaN'],'Unnamed: 11':['NaN']})

        tool = Foo()
        result = tool.Crypto_clean(df,1)
    
        assert result.equals(pd.DataFrame({'Symbol':['BTC'],'Name':['Bitcoin'],'Market':['CRYPTO']}))


    def test_none(self):

        df_ = pd.DataFrame({'Unnamed: 0':'','#':[],'ชื่อ':[],'ราคา':[]
        ,'1h %':[],'24h %':[],'7d %':[],'มูลค่าตามราคาตลาด':[]
        ,'Volume(24h)':[],'อุปทานหมุนเวียน':[],'7 วันล่าสุด':[],'Unnamed: 11':[]})

        tool = Foo()
        result = tool.Crypto_clean(df_,1)

        assert str(result) == str(pd.DataFrame({'Symbol':[],'Name':[],'Market':[]}))



if __name__ == '__main__':
    unittest.main()