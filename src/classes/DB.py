import sqlite3
import sys
from classes.Table import Table

class DB:
    def __init__(self, db_name):
        self.db_name = db_name
        self.books_table = Table('books')
        self.quotes_table = Table('quotes')

    def get_conection(self):
        con = sqlite3.connect(self.db_name)
        return con

    def get_cursor_con(self):
        con = self.get_conection()
        cursor = con.cursor()
        return cursor, con

    def commit_and_close(self, con):
        con.commit()
        con.close()

    def check_table_exists(self, table):
        cursor, con = self.get_cursor_con()
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table.value}'")
        tables = cursor.fetchall()
        self.commit_and_close(con)
        if not tables:
            print(f'Table "{table.value}" doesnt exists')
            sys.exit(1)

    def create_table(self, table_name, columns):
        columns = (', ').join(columns)
        cursor, con = self.get_cursor_con()
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name}({columns})""")
        self.commit_and_close(con)

    def insert_data(self, table_name, entries_data):
        data_schema = '(' + ('?,'*len(entries_data[0]))[:-1] + ')' # e.g (?,?,?)
        cursor, con = self.get_cursor_con()
        cursor.executemany(f'INSERT OR IGNORE INTO {table_name} VALUES {data_schema}', entries_data)
        self.commit_and_close(con)

    def retrieve_data(self, table, query):
        self.check_table_exists(table)
        cursor, con = self.get_cursor_con()
        sql_cmd = self.get_sql_cmd(table, query)
        cursor.execute(f"SELECT * FROM {table.value} {sql_cmd}")
        data = cursor.fetchall()
        self.commit_and_close(con)

        return data

    def get_sql_cmd(self, table, query):
        if table.value == 'books':
            sql_cmd = '' if query == 'all' else f"WHERE book_name LIKE '%{query}%' OR author LIKE '%{query}%'"
        elif table.value == 'quotes':
            sql_cmd = f"WHERE book_id LIKE '{query}'"

        return sql_cmd