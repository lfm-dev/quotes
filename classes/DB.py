import sqlite3
from classes.Book import Book

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
        con = self.get_conection()
        cursor = self.get_cursor(con)
        if query == 'all':
            cursor.execute("SELECT * FROM books")
        else:
            cursor.execute(f"SELECT * FROM books WHERE book_name LIKE '%{query}%' OR author LIKE '%{query}%'")
        books = cursor.fetchall()
        self.commit_and_close(con)
        books = [Book(id_ = entry[0], book_name = entry[1], author = entry[2], n_quotes = entry[3]) for entry in books]
        return books

    def get_book_quotes(self, book_id):
        con = self.get_conection()
        cursor = self.get_cursor(con)
        cursor.execute(f"SELECT quote FROM quotes WHERE book_id LIKE '{book_id}'")
        quotes = cursor.fetchall()
        self.commit_and_close(con)
        quotes = [quote[0] for quote in quotes] # fetchall returns list of tuples
        return quotes