import sqlite3

class DB:
    DB_NAME = 'book_quotes.db'

    def get_conection(self):
        con = sqlite3.connect(self.DB_NAME)
        return con

    def get_cursor_con(self):
        con = self.get_conection()
        cursor = con.cursor()
        return cursor, con

    def commit_and_close(self, con):
        con.commit()
        con.close()