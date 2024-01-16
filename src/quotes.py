import os
from classes.DB import DB
from components.print_table import print_entries
from components.make_update_db import make_update_db
from components.utils import get_args
from components.api import retrieve_data

#TODO installation script
QUOTES_PATH = '/path/to/your/quotes/folder'

def main():
    os.chdir(QUOTES_PATH)
    db = DB('book_quotes.db')

    args, parser = get_args()
    if args.makedb: # make (or update) sqlite3 db
        make_update_db(db)
    elif args.books: # search books
        books = retrieve_data(db, 'books', query=args.books)
        print_entries(books, 'books')
    elif args.quotes: # show quotes
        quotes = retrieve_data(db, 'quotes', query=args.quotes)
        print_entries(quotes, 'quotes')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()