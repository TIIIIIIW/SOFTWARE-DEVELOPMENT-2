import sqlite3


class Foo() :

    def search_share_in_table(self,words,NewsId,source):
        # connect to the database
        conn = sqlite3.connect(r'')
        c = conn.cursor()
        share = []
        loss = []

        for word in words : 

            w = word
            if source == 'Kaohoon': w = word + '.BK'

            # search for words in the table
            c.execute(f"""SELECT * FROM Information WHERE Symbol="{w}" or Sname="{word}"; """)
            results = c.fetchall()

            if results != []:
                data = {}
                data['SymbolId'],data['NewsId'] = results[0][0],NewsId
                share.append(data)

            else :

                loss.append(word)

        # close the database connection
        conn.close()

        return share,loss