import pandas as pd
from googletrans import Translator

class Foo():


    def translate_text(self,text):

        detector = Translator()
        rate = 1000
        dec_lan = ''
        for sec in range(int(len(text)/rate)+1):

            dec_lan += detector.translate(text[rate*sec:rate*(sec+1)],des='en').text
            print(dec_lan,"-------------------------------------------")
        return dec_lan