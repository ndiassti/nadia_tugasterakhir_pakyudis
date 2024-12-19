import mysql.connector

class Data:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",        # Ganti dengan user database MySQL Anda
            password="",        # Ganti dengan password database MySQL Anda
            database="karyawan" # Nama database
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def get_data(self, query, values=()):
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        return result

    def insert_data(self, query, values):
        self.cursor.execute(query, values)
        self.conn.commit()
