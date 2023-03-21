# from module import Foo
import unittest
from unittest.mock import Mock
from unittest.mock import patch
from googletrans import Translator
from unittest.mock import MagicMock

class texts():

    def __init__(self,s) :
        self.text = s

class Foo():

    def translate_text(self,text):

        detector = Translator()
        rate = 1000
        dec_lan = ''
        for sec in range(int(len(text)/rate)+1):
            print(text[rate*sec:rate*(sec+1)])
            dec_lan += detector.translate(text[rate*sec:rate*(sec+1)],des='en').text
            # print(dec_lan,"-------------------------------------------")
        return dec_lan
    
class AdditionTestCase(unittest.TestCase):


    def test_Translate_main(self):

        text = """ฉันชอบกินข้าวผัด"""

        real = Foo()
        Translator.translate = MagicMock(side_effect=[texts("I like to eat fried rice."),])
        result = real.translate_text(text)

        assert result == "I like to eat fried rice."


    def test_Translate_null(self):

        text = """"""

        real = Foo()
        Translator.translate = MagicMock(side_effect=[texts(""),])
        result = real.translate_text(text)

        assert result == ""

if __name__ == '__main__':
    unittest.main()