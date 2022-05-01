import mysql.connector
from mysql.connector import Error


class Database():
    state = False

    def __init__(self, host_name, database_name, user_name, password_name):
        self.host_name = host_name
        self.database_name = database_name
        self.user_name = user_name
        self.password_name = password_name

        self.connection = mysql.connector.connect(host=self.host_name,
                                                  database=self.database_name,
                                                  user=self.user_name,
                                                  password=self.password_name)
        self.cursor = self.connection.cursor()

    def checkPassword(self, login, password):
        sql_Query = "SELECT * FROM info"
        self.cursor.execute(sql_Query)
        records = self.cursor.fetchall()

        for row in records:
            if login == row[1] and password == row[2]:
                print("SUCCESSFULLY LOGIN")
                Database.state = True
        if not Database.state:
            print("WRONG LOGIN OR NUMBER")

    def closeConnection(self):
        self.connection.close()
        self.cursor.close()
        print("Closed connection to SQL DB")

    def addRecord(self, login, password):
        sql = "INSERT INTO info (login, password) VALUES( %s, %s)"
        val = (login, password)
        self.cursor.execute(sql, val)

    def listRecords(self):
        sql_Query = "SELECT * FROM info"
        self.cursor.execute(sql_Query)
        records = self.cursor.fetchall()
        return records

    def updateRecords(self):
        self.connection.commit()


# dakodadkopa




base = Database("localhost", "users", "root", "Jakumo123")
records = base.listRecords()
base.closeConnection()
