import os
import argparse
from classes.Book import Book
from classes.Quote import Quote
from classes.DB import DB
from print_table import print_table

def add_data_to_db(db, books, quotes):
    books_data = [(book.id_, book.book_name, book.author, book.n_quotes) for book in books]
    quotes_data = [(f'{n}-{quote.book_id}', quote.book_id, quote.quote) for n, quote in enumerate(quotes)]
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
            if line.startswith('#'):
                id_, book_name, author = get_book_data(line)
                quotes[id_] = []
                book = Book(id_, book_name, author)
                books.append(book)
            elif line.startswith('*'):
                quotes[id_].append('')
                quotes[id_][-1] += line.lstrip('* ')
            else:
                quotes[id_][-1] += line
    return books, quotes

def add_n_quotes_to_books(books, quotes):
    for book in books:
        book.n_quotes = len(quotes[book.id_])

def create_tables(db):
    db.create_table('books', 'book_id TEXT PRIMARY KEY', 'book_name TEXT', 'author TEXT', 'n_quotes INTEGER')
    db.create_table('quotes', 'quote_id TEXT PRIMARY KEY', 'book_id TEXT', 'quote TEXT')

def make_quotes(quotes):
    quotes = [Quote(book_id, quote) for book_id in quotes for quote in quotes[book_id]]
    return quotes

def make_update_db(db):
    create_tables(db)
    quotes_files = sorted([xfile for xfile in os.listdir(os.curdir) if xfile.endswith('.md')])
    for md_file_name in quotes_files:
        books, quotes = read_md_file(md_file_name)
        add_n_quotes_to_books(books, quotes)
        quotes = make_quotes(quotes)
        add_data_to_db(db, books, quotes)

def get_args():
    parser = argparse.ArgumentParser(prog='quotes', description='Manage your book quotes')
    parser.add_argument('-makedb', action='store_true', dest='makedb', help='Make (or update) sqlite3 db')
    parser.add_argument('-b', '-books', metavar='', dest='books', help='Search books by name or author ("all" to show all books)')
    parser.add_argument('-q', '-quotes', metavar='', dest='quotes', help='Show all quotes of a book by book ID')
    args = parser.parse_args()
    return args, parser

def main():
    quotes_path = '/path/to/your/quotes/folder'
    os.chdir(quotes_path)
    db = DB('book_quotes.db')

    args, parser = get_args()
    if args.makedb: # make (or update) sqlite3 db
        make_update_db(db)
    elif args.books: # search books
        book_list = db.get_books_data(args.books)
        books = [Book(id_ = entry[0], book_name = entry[1], author = entry[2], n_quotes = entry[3]) for entry in book_list]
        print_table(books, 'books')
    elif args.quotes: # show quotes
        quotes = db.get_book_quotes(args.quotes)
        print_table(quotes, 'quotes')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()