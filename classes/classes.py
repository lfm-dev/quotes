import sqlite3

class Entry:
    def __init__(self, id_, book_name, author):
        self.id_ = id_
        self.book_name = book_name
        self.author = author
        self.quotes = []
        self.n_quotes = 0

    def add_quote(self, quote):
        self.quotes.append(quote)
        self.n_quotes += 1

    def __repr__(self):
        return f'{self.id_} {self.book_name} {self. author} {self.n_quotes}'

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
        try:
            cursor.execute(f"""CREATE TABLE {table_name}({columns})""")
        except sqlite3.OperationalError as e: # table already exists
            print('Error:', e)
        self.commit_and_close(con)

    def insert_data(self, table_name, data_list):
        data_schema = '(' + ('?,'*len(data_list[0]))[:-1] + ')' # e.g (?,?,?)
        con = self.get_conection()
        cursor = self.get_cursor(con)
        try:
            cursor.executemany(f'INSERT INTO {table_name} VALUES {data_schema}', data_list)
        except sqlite3.IntegrityError as e:
            print('Error:', e)
        self.commit_and_close(con)