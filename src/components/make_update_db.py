import os
from classes.Quote import Quote
from classes.Book import Book
from components.api import create_table, insert_data

def read_md_file(md_file_name):
    quotes = {}
    books = {}
    with open(md_file_name) as file_handle:
        for line in file_handle:
            if not line.strip():
                continue
            if line.startswith('#'):
                book_id, book_name, author = get_book_data(line)
                quotes[book_id] = []
                book = Book(book_id, book_name, author)
                books[book.book_id] = book
            elif line.startswith('*'):
                book.n_quotes += 1
                quotes[book_id].append('')
                quotes[book_id][-1] += line.lstrip('* ')
            else:
                quotes[book_id][-1] += line
    quotes = [Quote(f'{n}-{book_id}', book_id, books[book_id].book_name, quote) for book_id in quotes for n, quote in enumerate(quotes[book_id])]
    books = [books[book_id] for book_id in books]
    return books, quotes

def get_book_data(line):
    return line[1:].strip().split('/')

def create_tables(db):
    create_table(db, 'books', 'book_id TEXT PRIMARY KEY', 'book_name TEXT', 'author TEXT', 'n_quotes INTEGER')
    create_table(db, 'quotes', 'quote_id TEXT PRIMARY KEY', 'book_id TEXT', 'book_name TEXT', 'quote TEXT')

def add_data_to_db(db, books, quotes):
    books_data = [(book.book_id, book.book_name, book.author, book.n_quotes) for book in books]
    quotes_data = [(quote.quote_id, quote.book_id, quote.book_name, quote.quote) for quote in quotes]
    insert_data(db, 'books', books_data)
    insert_data(db, 'quotes', quotes_data)

def make_update_db(db):
    create_tables(db)
    quotes_files = sorted([xfile for xfile in os.listdir(os.curdir) if xfile.endswith('.md')])
    for md_file_name in quotes_files:
        books, quotes = read_md_file(md_file_name)
        add_data_to_db(db, books, quotes)