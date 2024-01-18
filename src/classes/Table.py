import sys
from classes.DB import DB
from classes.Book import Book
from classes.Quote import Quote

class Table:

    DB = DB()

    def create_table(self, table_name, *columns):
        columns = (', ').join(columns)
        cursor, con = self.DB.get_cursor_con()
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name}({columns})""")
        self.DB.commit_and_close(con)

    def insert_data(self, table_name, entries):
        entries_data = [entry.get_data() for entry in entries]
        data_schema = '(' + ('?,'*len(entries_data[0]))[:-1] + ')' # e.g (?,?,?)
        cursor, con = self.DB.get_cursor_con()
        cursor.executemany(f'INSERT OR IGNORE INTO {table_name} VALUES {data_schema}', entries_data)
        self.DB.commit_and_close(con)

    def retrieve_data(self, table_name, sql_cmd):
        cursor, con = self.DB.get_cursor_con()
        cursor.execute(f"SELECT * FROM {table_name} {sql_cmd}")
        data = cursor.fetchall()
        self.DB.commit_and_close(con)
        return data

    def entry_not_found(self, query):
        print(f"'{query}' not found")
        sys.exit(1)

class BooksTable(Table):

    TABLE_NAME = 'books'

    def __init__(self):
        self.create_table(self.TABLE_NAME,
        'book_id TEXT PRIMARY KEY',
        'book_name TEXT',
        'author TEXT',
        'n_quotes INTEGER'
        )

    def add_books(self, books):
        super().insert_data(self.TABLE_NAME, books)

    def get_books(self, query):
        sql_cmd = self.get_sql_cmd(query)
        data = super().retrieve_data(self.TABLE_NAME, sql_cmd)

        if not data:
            super().entry_not_found(query)

        books = [Book(book_id = book[0], book_name = book[1], author = book[2], n_quotes = book[3]) for book in data]
        return books

    def get_sql_cmd(self, query):
        return '' if query == 'all' else f"WHERE book_name LIKE '%{query}%' OR author LIKE '%{query}%'"

class QuotesTable(Table):

    TABLE_NAME = 'quotes'

    def __init__(self):
        self.create_table(self.TABLE_NAME,
        'quote_id TEXT PRIMARY KEY',
        'book_id TEXT',
        'book_name TEXT',
        'quote TEXT'
        )

    def add_quotes(self, quotes):
        super().insert_data(self.TABLE_NAME, quotes)

    def get_quotes_by_bookid(self, query):
        sql_cmd = self.get_sql_cmd(query)
        data = super().retrieve_data(self.TABLE_NAME, sql_cmd)

        if not data:
            super().entry_not_found(query)

        quotes = [Quote(quote_id = quote[0], book_id = quote[1], book_name = quote[2], quote = quote[3]) for quote in data]
        return quotes

    def get_sql_cmd(self, query):
        return f"WHERE book_id LIKE '{query}'"