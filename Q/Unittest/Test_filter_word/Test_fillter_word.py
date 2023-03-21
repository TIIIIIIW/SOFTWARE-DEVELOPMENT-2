# from module import Foo
import unittest
from unittest.mock import Mock
from unittest.mock import patch
from googletrans import Translator
from unittest.mock import MagicMock
import numpy

class Foo():

    def filter_special_2(self,words):
        # Define regular expression pattern to match words
        word_filter = []

        # Find all matches of the pattern in the text
        for word in words :
            s = 0
            word = str(word)
            for ch in word:

                if isinstance(ch , str) and ch.isnumeric(): s = 1

            if s == 0: word_filter.append(word)
                    
        return list(numpy.unique(word_filter))
    
class AdditionTestCase(unittest.TestCase):


    def test_filter_main(self):

        real = Foo()
        word = ['FRBK', 'FRC', '$2.1 billion','18.85','26', '27%']
        result = real.filter_special_2(word)

        assert result == ['FRBK', 'FRC']

    def test_filter_main2(self):

        real = Foo()
        word = ['FRBK', 'FRBK','FRC', '$2.1 billion','18.85','26', '27%']
        result = real.filter_special_2(word)

        assert result == ['FRBK', 'FRC']

    def test_filter_not_found(self):

        real = Foo()
        word = ['$2.1 billion','18.85',26, '27%']
        result = real.filter_special_2(word)

        assert result == []

    def test_filter_null(self):

        real = Foo()
        word = []
        result = real.filter_special_2(word)

        assert result == []

if __name__ == '__main__':
    unittest.main()