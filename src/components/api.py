import sys
from components.utils import make_books, make_quotes

def insert_data(table, entries):
    entries_data = [entry.get_data() for entry in entries]
    table.insert_data(entries_data)

def retrieve_data(table, query):
    data = table.retrieve_data(query)
    if not data:
        print(f"'{query}' not found")
        sys.exit(1)

    entries = make_books(data) if table.TABLE_NAME == 'books' else make_quotes(data) if table.TABLE_NAME == 'quotes' else []

    return entries
