import os
from classes.DB import DB
from components.print_table import print_table
from components.make_update_db import make_update_db
from components.utils import get_args, make_books, make_quotes
from components.api import retrieve_data

def main():
    quotes_path = '/path/to/your/quotes/folder'
    os.chdir(quotes_path)
    db = DB('book_quotes.db')

    args, parser = get_args()
    if args.makedb: # make (or update) sqlite3 db
        make_update_db(db)
    elif args.books: # search books
        books = retrieve_data(db, 'books', query=args.books)
        if books:
            books = make_books(books)
            print_table(books, 'books')
    elif args.quotes: # show quotes
        quotes = retrieve_data(db, 'quotes', query=args.quotes)
        if quotes:
            quotes = make_quotes(quotes)
            print_table(quotes, 'quotes')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()