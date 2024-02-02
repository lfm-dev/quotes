#!/usr/bin/python3
import os
from classes.Table import BooksTable, QuotesTable
from components.print_entries import print_books_table, print_quotes_markdown
from components.make_update_db import make_update_db
from components.get_args import get_args

#TODO add book tags support
QUOTES_PATH = '/path/to/your/quotes/folder'

def main():
    os.chdir(QUOTES_PATH)

    books_table = BooksTable()
    quotes_table = QuotesTable()

    args, parser = get_args()

    if args.make_update_db:
        make_update_db(books_table, quotes_table)

    elif args.show_books:
        book_name_author = args.show_books
        books = books_table.get_books(query=book_name_author)
        if len(books) == 1: # if only one book was found, print quotes
            quotes = quotes_table.get_quotes_by_bookid(book_id=books[0].book_id)
            book_name, author = books_table.get_book_name_author(book_id=books[0].book_id)
            print_quotes_markdown(quotes, book_name, author)
        else:
            print_books_table(books)

    elif args.show_quotes:
        book_id = args.show_quotes
        quotes = quotes_table.get_quotes_by_bookid(book_id=book_id)
        book_name, author = books_table.get_book_name_author(book_id=quotes[0].book_id)
        print_quotes_markdown(quotes, book_name, author)

    else:
        parser.print_help()

if __name__ == '__main__':
    main()
