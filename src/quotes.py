#!/usr/bin/python3
import os
from components.get_settings import SETTINGS
from components.get_books import get_books
from components.get_authors import get_authors
from components.get_all_tags import get_tags
from components.filter_books import filter_books
from components.filter_quotes import filter_quotes
from components.print_entries import print_books_table, print_book_quotes_markdown, print_authors_table, print_tags_table, print_quotes_markdown
from components.get_args import get_args

#TODO README.md

def main():
    os.chdir(SETTINGS['quotes_path'])

    args, parser = get_args()
    books = get_books()

    if args.show_books:
        query = args.show_books.strip().casefold()
        filtered_books = filter_books(books, query)

        if len(filtered_books) == 1: # if only one book was found, print quotes
            print_book_quotes_markdown(filtered_books[0])
        elif len(filtered_books) > 1:
            print_books_table(filtered_books)
        else:
            print('No books found.')

    elif args.show_quotes:
        query = args.show_quotes
        quotes = filter_quotes(books, query)
        if quotes:
            print_quotes_markdown(quotes)
        else:
            print('Quotes not found.')

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
