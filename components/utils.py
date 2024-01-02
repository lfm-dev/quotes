import argparse
from classes.Book import Book
from classes.Quote import Quote

def get_args():
    parser = argparse.ArgumentParser(prog='quotes', description='Manage your book quotes')
    parser.add_argument('-makedb', action='store_true', dest='makedb', help='Make (or update) sqlite3 db')
    parser.add_argument('-b', '-books', metavar='', dest='books', help='Search books by name or author ("all" to show all books)')
    parser.add_argument('-q', '-quotes', metavar='', dest='quotes', help='Show all quotes of a book by book ID')
    args = parser.parse_args()
    return args, parser

def make_books(books):
    return [Book(book_id = book[0], book_name = book[1], author = book[2], n_quotes = book[3]) for book in books]

def make_quotes(quotes):
    return [Quote(quote_id = quote[0], book_id = quote[1], book_name = quote[2], quote = quote[3]) for quote in quotes]
