import os
from classes.Table import BooksTable, QuotesTable
from components.print_table import print_entries
from components.make_update_db import make_update_db
from components.utils import get_args
from components.api import get_books, get_quotes

#TODO installation script
QUOTES_PATH = '/path/to/your/quotes/folder'

def main():
    os.chdir(QUOTES_PATH)
    books_table = BooksTable()
    quotes_table = QuotesTable()

    args, parser = get_args()
    if args.makedb: # make (or update) sqlite3 db
        make_update_db(books_table, quotes_table)
    elif args.books: # search books
        books = get_books(books_table, query=args.books)
        print_entries(books, books_table)
    elif args.quotes: # show quotes
        quotes = get_quotes(quotes_table, query=args.quotes)
        print_entries(quotes, quotes_table)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()