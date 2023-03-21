# from module import Foo
import unittest
from unittest.mock import Mock
from unittest.mock import patch
from googletrans import Translator
from unittest.mock import MagicMock
from geopy.geocoders import Nominatim

class location():

    def __init__(self,la,lo,) :
        self.latitude = la
        self.longitude = lo
        self.raw    = {'address':{'country':'Thai'}}


class Foo():

    def find_location(self,words,NewsId):

        geolocator = Nominatim(user_agent="Geolocation")
        loca = []
        for i in words :

            location = geolocator.geocode(f"{i}", exactly_one=True, namedetails=True, addressdetails=True,timeout=10000, language='en')
            print(location)
            if str(location) != 'None' :

                data = {}
                if i in['Africa', 'Europe', 'Asia', 'North America', 'South America', 'Antarctica', 'Australia'] :
                    data['Lname'],data['Country'],data['point'],data['NewsId'] = i,'',(location.latitude, location.longitude),NewsId
                else:
                    data['Lname'],data['Country'],data['point'],data['NewsId'] = i,location.raw['address']['country'],(location.latitude, location.longitude),NewsId

                loca.append(data)

        return loca
    
class AdditionTestCase(unittest.TestCase):


    def test_Translate_main(self):

        words = ['A','B','C']

        real = Foo()
        Nominatim.geocode = MagicMock(side_effect=['None',location(''),'None'])
        result = real.find_location(words,'0')

        assert result == "I like to eat fried rice."


    # def test_Translate_null(self):

    #     text = """"""

    #     real = Foo()
    #     Translator.translate = MagicMock(side_effect=[texts(""),])
    #     result = real.translate_text(text)

    #     assert result == ""

if __name__ == '__main__':
    unittest.main()