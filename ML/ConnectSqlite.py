import sqlite3
import pandas as pd
import plotly.graph_objects as go

conn = sqlite3.connect('share.sqlite')
cursor = conn.cursor()


df = pd.read_sql("""SELECT SP."Date",SP.Open,Sp.High,SP.Low,SP.Close,SP."Adj Close",SP.Volume,I.Symbol 
                    FROM Stock_price_day as SP 
                    INNER JOIN Information as I 
                    on I.SymbolId = SP.SymbolId 
                    WHERE I.Symbol = 'AOT';
                    """,conn)
conn.close()

df = df.tail(100)

print(df)