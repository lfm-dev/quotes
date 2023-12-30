import os
from classes.Book import Book
from classes.DB import DB
from components.print_table import print_table
from components.DB_management import make_update_db
from components.args_parser import get_args

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