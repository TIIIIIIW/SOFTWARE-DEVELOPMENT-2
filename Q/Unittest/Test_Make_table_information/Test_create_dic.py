import unittest

class AdditionTestCase(unittest.TestCase):

    def test_create_dic_main(self):

        result = create_dic('Detail of Security\nMarket\nSET\nIndustry\nProperty & Construction\nFirst Trade Date\n08 Nov 2012\nSector\nProperty Development\nForeign Limit\n49.00000% (As of 30 Dec 2022)\nDividend Policy\nAt least 40 per cent of the net profit pursuant to the separated financial statement of the Company after the deductions of legal reserves for each year (with additional conditions)\nISIN Number\nLocal\nTH3871010Z01\nForeign\nTH3871010Z19\nNVDR\nTH3871010R19\nFiscal End\n31 Dec\nThe person taking the highest responsibility in finance and accounting\nMr. Mr. Natthapatt Tanboon-ek (Start date 01 Sep 2020)\nCompany Auditor (Effective Until 31 Dec 2022)\nMR. PAIBOON TUNKOON (PRICEWATERHOUSE COOPERS ABAS LIMITED)\nMR. BOONRUENG LERDWISESWIT (PRICEWATERHOUSE COOPERS ABAS LIMITED)\nMr. KAN TANTHAWIRAT (PRICEWATERHOUSE COOPERS ABAS LIMITED)\nThe person supervising accounting\nMr. Somsak Boonchoyruengchai (Start date 01 Jan 2017)','WHA')

        assert result == {'Symbol': 'WHA','Market': 'SET','Industry': 'Property & Construction','Sector': 'Property Development','Dividend Policy': 'At least 40 per cent of the net profit pursuant to the separated financial statement of the Company after the deductions of legal reserves for each year (with additional conditions)'}

    def test_create_dic_Null_1(self):

        result = create_dic('','WHA')

        assert result == {'Symbol': 'WHA','Market': 'Null','Industry': 'Null','Sector': 'Null','Dividend Policy': 'Null'}

    def test_create_dic_Null_2(self):

        result = create_dic('','')

        assert result == {'Symbol': '','Market': 'Null','Industry': 'Null','Sector': 'Null','Dividend Policy': 'Null'}


def create_dic(content,stock):

    try:
        data_info,n = {},0
        data_info["Symbol"] = stock
        data = content.split("\n")[1:13]

        while n < 12:

            if n == 4 or n == 8 :
                n += 2
                continue        
            data_info[data[n]] = data[n+1]
            n += 2

        return data_info

    except IndexError:
        
        return {'Symbol': stock,
         'Market': 'Null',
         'Industry': 'Null',
         'Sector': 'Null',
         'Dividend Policy': 'Null'}


if __name__ == '__main__':
    unittest.main()