import os
from classes.Quote import Quote
from classes.Book import Book

def read_md_file(md_file_name):
    quotes = {}
    books = []
    with open(md_file_name) as file_handle:
        for line in file_handle:
            if not line.strip():
                continue
            if line.startswith('#'):
                book_id, book_name, author = get_book_data(line)
                quotes[book_id] = []
                book = Book(book_id, book_name, author)
                books.append(book)
            elif line.startswith('*'):
                book.n_quotes += 1
                quotes[book_id].append('')
                quotes[book_id][-1] += line.lstrip('* ')
            else:
                quotes[book_id][-1] += line
    quotes = [Quote(f'{n}-{book_id}', book_id, quote) for book_id in quotes for n, quote in enumerate(quotes[book_id])]
    return books, quotes

def get_book_data(line):
    return line[1:].strip().split('/')

def create_tables(db):
    db.create_table('books', 'book_id TEXT PRIMARY KEY', 'book_name TEXT', 'author TEXT', 'n_quotes INTEGER')
    db.create_table('quotes', 'quote_id TEXT PRIMARY KEY', 'book_id TEXT', 'quote TEXT')

def add_data_to_db(db, books, quotes):
    books_data = [(book.book_id, book.book_name, book.author, book.n_quotes) for book in books]
    quotes_data = [(quote.quote_id, quote.book_id, quote.quote) for quote in quotes]
    db.insert_data('books', books_data)
    db.insert_data('quotes', quotes_data)

def main(db):
    create_tables(db)
    quotes_files = sorted([xfile for xfile in os.listdir(os.curdir) if xfile.endswith('.md')])
    for md_file_name in quotes_files:
        books, quotes = read_md_file(md_file_name)
        add_data_to_db(db, books, quotes)