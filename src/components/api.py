import sys
from components.utils import make_books, make_quotes

def insert_data(table, entries):
    entries_data = [entry.get_data() for entry in entries]
    table.insert_data(entries_data)

def get_books(books_table, query):
    data = books_table.retrieve_data(query)
    if not data:
        print(f"'{query}' not found")
        sys.exit(1)
    books = make_books(data)

    return books

def get_quotes(quotes_table, query):
    data = quotes_table.retrieve_data(query)
    if not data:
        print(f"'{query}' not found")
        sys.exit(1)
    quotes = make_quotes(data)

    return quotes
