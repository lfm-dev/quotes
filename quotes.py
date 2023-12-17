import os
import argparse
from classes.classes import Book
from classes.classes import DB
from print_table import print_table

def add_data_to_db(db, books):
    books_data = [(book.id_, book.book_name, book.author, book.n_quotes) for book in books]
    quotes_data = [(f'{n}-{book.id_}', book.id_, quote) for book in books for n, quote in enumerate(book.quotes)]
    db.insert_data('books', books_data)
    db.insert_data('quotes', quotes_data)

def get_book_data(line):
    return line[1:].strip().split('/')

def read_md_file(md_file_name):
    quotes = {}
    books = []
    with open(md_file_name) as file_handle:
        for line in file_handle:
            if not line.strip():
                continue
            elif line.startswith('#'):
                id_, book_name, author = get_book_data(line)
                quotes[book_name] = []
                book = Book(id_, book_name, author)
                books.append(book)
            elif line.startswith('*'):
                quotes[book_name].append('')
                quote_number = len(quotes[book_name])-1
                quotes[book_name][quote_number] += line.lstrip('* ')
            else:
                quotes[book_name][quote_number] += line
    return books, quotes

def add_quotes_to_books(books, quotes):
    for book in books:
        for quote in quotes[book.book_name]:
            book.add_quote(quote.strip()) # remove last \n

def create_tables(db):
    db.create_table('books', 'book_id TEXT PRIMARY KEY', 'book_name TEXT', 'author TEXT', 'n_quotes INTEGER')
    db.create_table('quotes', 'quote_id TEXT PRIMARY KEY', 'book_id TEXT', 'quote TEXT')

def make_update_db(db):
    create_tables(db)
    quotes_files = sorted([xfile for xfile in os.listdir(os.curdir) if xfile.endswith('.md')])
    for md_file_name in quotes_files:
        books, quotes = read_md_file(md_file_name)
        add_quotes_to_books(books, quotes)
        add_data_to_db(db, books)

def get_args():
    parser = argparse.ArgumentParser(prog='quotes', description='Manage your book quotes')
    parser.add_argument('-makedb', action='store_true', dest='makedb', help='Make (or update) sqlite3 db')
    parser.add_argument('-b', '-books', metavar='', dest='books', help='Search books by name or author ("all" to show all books)')
    args = parser.parse_args()
    return args

def main():
    quotes_path = '/path/to/your/quotes/folder'
    os.chdir(quotes_path)
    db = DB('book_quotes.db')

    args = get_args()
    if args.makedb: # make (or update) sqlite3 db
        make_update_db(db)
    elif args.books: # search books
        book_list = db.get_book_data(args.books)
        books = [Book(id_ = entry[0], book_name = entry[1], author = entry[2], n_quotes = entry[3]) for entry in book_list]
        print_table(books)

if __name__ == '__main__':
    main()