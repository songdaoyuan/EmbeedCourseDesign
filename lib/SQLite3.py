import sqlite3


class SQLITE():
    def __init__(self):
        #self.conn = sqlite3.connect(r'../SQLite/EmbeedOSPracticum.db')
        self.conn = sqlite3.connect(r"C:\Users\Songdaoyuan\Documents\Visual Studio Code\嵌入式课设\SQLite\EmbeedOSPracticum.db")
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def returnTableContent(self):
        Query = "Select * from Users"
        result = self.cursor.execute(Query)
        result = result.fetchall()

        return(result)

    def ExecQuery(self, Query):
        self.cursor.execute(Query)
        result = self.cursor.execute(Query)
        result = result.fetchall()

        return(result)

    def ExecNonQuery(self, Query):
        self.cursor.execute(Query)
        self.conn.commit()


if __name__ == '__main__':
    pass
    #DB = SQLITE()
    #DB.ExecNonQuery("INSERT INTO 'Users' (ID, FirstName, LastName, Phone) VALUES (NULL, 'Wei', 'chenxi', '18627234952');")
    #a = DB.returnTableContent()
    #b = DB.ExecQuery("SELECT * FROM Users WHERE ID=1")
    #print(b[0][1])
    # print(a)
