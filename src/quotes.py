import os
from classes.Table import BooksTable, QuotesTable
from components.print_entries import print_books_table, print_quotes_markdown
from components.make_update_db import make_update_db
from components.get_args import get_args

#TODO installation script
QUOTES_PATH = '/path/to/your/quotes/folder'

def main():
    os.chdir(QUOTES_PATH)

    books_table = BooksTable()
    quotes_table = QuotesTable()

    args, parser = get_args()

    if args.makedb:
        make_update_db(books_table, quotes_table)

    elif args.books:
        books = books_table.get_books(query=args.books) # query: book_name or author
        print_books_table(books)

    elif args.quotes:
        quotes = quotes_table.get_quotes_by_bookid(query=args.quotes) # query: book_id
        book_name, author = books_table.get_book_name_author(book_id=quotes[0].book_id)
        print_quotes_markdown(quotes, book_name, author)

    else:
        parser.print_help()

if __name__ == '__main__':
    main()