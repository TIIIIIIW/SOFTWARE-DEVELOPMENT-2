
import pandas as pd


class Foo():
    def Crypto_clean(self,df,p):

        Symbol,Name = [],[]
        round = (len(df['ชื่อ'])*p)

        n = 0
        for i in range(round-int(round/p),round):

            t = df['ชื่อ'][n].split(f'{i+1}')
            print(t)
            n+=1
            Symbol.append(t[1])
            Name.append(t[0])

        table = {}
        table['Symbol'] = Symbol
        table['Name'] = Name
        table['Market'] = 'CRYPTO'
        df = pd.DataFrame(table)

        return df