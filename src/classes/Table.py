from classes.DB import DB

class Table:
    DB = DB()

    def create_table(self, table_name, *columns):
        columns = (', ').join(columns)
        cursor, con = self.DB.get_cursor_con()
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name}({columns})""")
        self.DB.commit_and_close(con)

    def insert_data(self, entries_data):
        data_schema = '(' + ('?,'*len(entries_data[0]))[:-1] + ')' # e.g (?,?,?)
        cursor, con = self.DB.get_cursor_con()
        cursor.executemany(f'INSERT OR IGNORE INTO {self.TABLE_NAME} VALUES {data_schema}', entries_data)
        self.DB.commit_and_close(con)

    def retrieve_data(self, sql_cmd):
        cursor, con = self.DB.get_cursor_con()
        cursor.execute(f"SELECT * FROM {self.TABLE_NAME} {sql_cmd}")
        data = cursor.fetchall()
        self.DB.commit_and_close(con)
        return data

class BooksTable(Table):
    TABLE_NAME = 'books'

    def __init__(self):
        self.create_table(self.TABLE_NAME, 'book_id TEXT PRIMARY KEY', 'book_name TEXT', 'author TEXT', 'n_quotes INTEGER')

    def retrieve_data(self, query):
        sql_cmd = self.get_sql_cmd(query)
        return super().retrieve_data(sql_cmd)

    def get_sql_cmd(self, query):
        return '' if query == 'all' else f"WHERE book_name LIKE '%{query}%' OR author LIKE '%{query}%'"


class QuotesTable(Table):
    TABLE_NAME = 'quotes'

    def __init__(self):
        self.create_table(self.TABLE_NAME, 'quote_id TEXT PRIMARY KEY', 'book_id TEXT', 'book_name TEXT', 'quote TEXT')

    def retrieve_data(self, query):
        sql_cmd = self.get_sql_cmd(query)
        return super().retrieve_data(sql_cmd)

    def get_sql_cmd(self, query):
        return f"WHERE book_id LIKE '{query}'"