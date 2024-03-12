#!/usr/bin/python3
import os
from components.get_books import get_books
from components.get_authors import get_authors
from components.get_tags import get_tags
from components.filter_books import filter_books
from components.print_entries import print_books_table, print_quotes_markdown, print_authors_table, print_tags_table
from components.get_args import get_args

QUOTES_PATH = '/path/to/your/quotes/folder'

def main():
    os.chdir(QUOTES_PATH)

    args, parser = get_args()
    books = get_books()

    if args.show_books:
        query = args.show_books
        filtered_books = filter_books(books, query)

        if len(filtered_books) == 1: # if only one book was found, print quotes
            print_quotes_markdown(filtered_books[0])
        elif len(filtered_books) > 1:
            print_books_table(filtered_books)
        else:
            print('No books found.')

    elif args.show_quotes:
        book_id = args.show_quotes
        book = books.get(book_id)
        if book:
            print_quotes_markdown(book)
        else:
            print('Book not found.')

    elif args.show_authors:
        authors = get_authors(books)
        print_authors_table(authors)

    elif args.show_tags:
        tags = get_tags(books)
        print_tags_table(tags)

    else:
        parser.print_help()

if __name__ == '__main__':
    main()
