import sys
from components.utils import make_books, make_quotes

def create_table(db, table_name, *columns):
    db.create_table(table_name, columns)

def insert_data(db, table_name, entries):
    entries_data = [entry.get_data() for entry in entries]
    db.insert_data(table_name, entries_data)

def retrieve_data(db, table, query):
    data = db.retrieve_data(table, query)
    if not data:
        print(f"'{query}' not found")
        sys.exit(1)

    entries = make_books(data) if table.value == 'books' else make_quotes(data) if table.value == 'quotes' else []

    return entries
