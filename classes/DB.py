import sqlite3
import sys

class DB:
    def __init__(self, db_name):
        self.db_name = db_name

    def get_conection(self):
        con = sqlite3.connect(self.db_name)
        return con

    def get_cursor(self, con):
        cursor = con.cursor()
        return cursor

    def commit_and_close(self, con):
        con.commit()
        con.close()

    def check_table_exists(self, table_name):
        con = self.get_conection()
        cursor = self.get_cursor(con)
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        tables = cursor.fetchall()
        self.commit_and_close(con)
        if not tables:
            print(f'Table "{table_name}" doesnt exists')
            sys.exit(1)