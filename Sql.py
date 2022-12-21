import mysql.connector as mysql

class Sql:
    def __init__(self):
        self.connection = mysql.connect(host="localhost", user="root", passwd="123456789", database="animal")
        self.cursor = self.connection.cursor()
    def connection_close(self):
        self.connection.close()
    def get_connection(self):
        return self.connection
    def get_cursor(self):
        return self.cursor
    def execute_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()

