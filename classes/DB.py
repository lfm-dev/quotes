import sqlite3
import sys
from classes.Book import Book
from classes.Quote import Quote

class DB:
    def __init__(self, db_name):
        self.db_name = db_name
        self.create_db()

    def create_db(self):
        sqlite3.connect(self.db_name)

    def get_conection(self):
        con = sqlite3.connect(self.db_name)
        return con

    def get_cursor(self, con):
        cursor = con.cursor()
        return cursor

    def commit_and_close(self, con):
        con.commit()
        con.close()

    def create_table(self, table_name, *columns):
        columns = (', ').join(columns)
        con = self.get_conection()
        cursor = self.get_cursor(con)
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name}({columns})""")
        self.commit_and_close(con)

    def check_table_exists(self, table_name):
        con = self.get_conection()
        cursor = self.get_cursor(con)
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        tables = cursor.fetchall()
        self.commit_and_close(con)
        if not tables:
            print(f'Table "{table_name}" doesnt exists')
            sys.exit(1)

    def insert_data(self, table_name, data_list):
        data_schema = '(' + ('?,'*len(data_list[0]))[:-1] + ')' # e.g (?,?,?)
        con = self.get_conection()
        cursor = self.get_cursor(con)
        try:
            cursor.executemany(f'INSERT OR IGNORE INTO {table_name} VALUES {data_schema}', data_list)
        except sqlite3.IntegrityError as e:
            print('Warning:', e)
        self.commit_and_close(con)

    def get_books_data(self, query):
        self.check_table_exists('books')
        con = self.get_conection()
        cursor = self.get_cursor(con)
        if query == 'all':
            cursor.execute("SELECT * FROM books")
        else:
            cursor.execute(f"SELECT * FROM books WHERE book_name LIKE '%{query}%' OR author LIKE '%{query}%'")
        books = cursor.fetchall()
        self.commit_and_close(con)
        books = [Book(book_id = book[0], book_name = book[1], author = book[2], n_quotes = book[3]) for book in books]
        return books

    def get_book_quotes(self, book_id):
        self.check_table_exists('quotes')
        con = self.get_conection()
        cursor = self.get_cursor(con)
        cursor.execute(f"SELECT * FROM quotes WHERE book_id LIKE '{book_id}'")
        quotes = cursor.fetchall()
        self.commit_and_close(con)
        quotes = [Quote(quote_id = quote[0], book_id = quote[1], quote = quote[2]) for quote in quotes]
        return quotes