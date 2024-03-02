#!/usr/bin/python3
import os
from components.get_quotes import get_book_quotes
from components.print_entries import print_books_table, print_quotes_markdown
from components.get_args import get_args

#TODO add book tags support
#TODO add authors table
QUOTES_PATH = '/path/to/your/quotes/folder'

def main():
    os.chdir(QUOTES_PATH)

    args, parser = get_args()
    books = get_book_quotes()

    if args.show_books:
        book_name_author = args.show_books
        filtered_books = []
        for _, book in books.items():
            if book_name_author.casefold() in book.book_name.casefold() or book_name_author.casefold() in book.author.casefold() or book_name_author == 'all':
                filtered_books.append(book)

        if len(filtered_books) == 1: # if only one book was found, print quotes
            print_quotes_markdown(filtered_books[0])
        elif len(filtered_books) > 1:
            print_books_table(filtered_books)

    elif args.show_quotes:
        book_id = args.show_quotes
        book = books.get(book_id)
        if book:
            print_quotes_markdown(book)

    else:
        parser.print_help()

if __name__ == '__main__':
    main()
