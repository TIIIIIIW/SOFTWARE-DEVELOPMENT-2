import spacy
import en_core_web_sm
import numpy
import unittest
from unittest.mock import Mock
from unittest.mock import patch
from googletrans import Translator
from unittest.mock import MagicMock

class nlp():

    ents = ''
    def __init__(self,s) :
        pass

    
class Foo():

    def Separate_words(self,text):

        nlp = spacy.load('en_core_web_sm')
        nlp = en_core_web_sm.load()
        doc = nlp(text)
        print(doc.ents)
        word = []

        for token in doc.ents:
        
            
            if token.label_ != 'DATE' and token.label_ !='CARDINAL' and token.label_ !='TIME':
                # print(token.text,token.label_) 

                if token.text not in ['1st','2nd','3rd','first','second','thrid'] and "%" not in token.text and  "/" not in token.text and  "percent" not in token.text and  "billion" not in token.text:
                    
                    word += token.text.split('"')

        return list(numpy.unique(word))
    


        
class AdditionTestCase(unittest.TestCase):


    def test_Translate_main(self):

        text = """ฉันชอบกินข้าวผัด"""

        real = Foo()

        spacy.load = MagicMock(side_effect=[""])
        en_core_web_sm.load = MagicMock(side_effect=[nlp])
  
        result = real.Separate_words(text)

        assert result == "I like to eat fried rice."



if __name__ == '__main__':
    unittest.main()