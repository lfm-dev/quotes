import sys
from classes.Book import Book
from classes.Quote import Quote

def make_books(books):
    return [Book(book_id = book[0], book_name = book[1], author = book[2], n_quotes = book[3]) for book in books]

def make_quotes(quotes):
    return [Quote(quote_id = quote[0], book_id = quote[1], book_name = quote[2], quote = quote[3]) for quote in quotes]

def get_sql_cmd(table, query):
    if table == 'books':
        sql_cmd = '' if query == 'all' else f"WHERE book_name LIKE '%{query}%' OR author LIKE '%{query}%'"
    elif table == 'quotes':
        sql_cmd = f"WHERE book_id LIKE '{query}'"

    return sql_cmd

def create_table(db, table_name, *columns):
    columns = (', ').join(columns)
    con = db.get_conection()
    cursor = db.get_cursor(con)
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name}({columns})""")
    db.commit_and_close(con)

def insert_data(db, table_name, entries):
    entries_data = [entry.get_data() for entry in entries]
    data_schema = '(' + ('?,'*len(entries_data[0]))[:-1] + ')' # e.g (?,?,?)
    con = db.get_conection()
    cursor = db.get_cursor(con)
    cursor.executemany(f'INSERT OR IGNORE INTO {table_name} VALUES {data_schema}', entries_data)
    db.commit_and_close(con)

def retrieve_data(db, table, query):
    db.check_table_exists(table)
    con = db.get_conection()
    cursor = db.get_cursor(con)
    sql_cmd = get_sql_cmd(table, query)
    cursor.execute(f"SELECT * FROM {table} {sql_cmd}")
    data = cursor.fetchall()
    db.commit_and_close(con)

    if not data:
        print(f"'{query}' not found")
        sys.exit(1)

    entries = make_books(data) if table == 'books' else make_quotes(data) if table == 'quotes' else []

    return entries
