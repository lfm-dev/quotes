import os
from components.read_data import read_md_file

def make_update_db(db):
    create_tables(db)
    quotes_files = sorted([xfile for xfile in os.listdir(os.curdir) if xfile.endswith('.md')])
    for md_file_name in quotes_files:
        books, quotes = read_md_file(md_file_name)
        add_data_to_db(db, books, quotes)

def create_tables(db):
    db.create_table('books', 'book_id TEXT PRIMARY KEY', 'book_name TEXT', 'author TEXT', 'n_quotes INTEGER')
    db.create_table('quotes', 'quote_id TEXT PRIMARY KEY', 'book_id TEXT', 'quote TEXT')

def add_data_to_db(db, books, quotes):
    books_data = [(book.id_, book.book_name, book.author, book.n_quotes) for book in books]
    quotes_data = [(f'{n}-{quote.book_id}', quote.book_id, quote.quote) for n, quote in enumerate(quotes)]
    db.insert_data('books', books_data)
    db.insert_data('quotes', quotes_data)