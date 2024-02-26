import os
import sys
from classes.Quote import Quote
from classes.Book import Book

def read_md_file(md_file_name):
    quotes = {}
    books = {}
    year = md_file_name.split('.')[0][-2:] # md name: year.md, get only last two digits
    with open(md_file_name, encoding="utf-8") as file_handle:
        book_number = 0
        for line in file_handle:
            if not line.strip():
                continue
            if line.startswith('#'):
                book_number += 1
                book_id = f'{year}-{book_number}'
                book_name, author = get_book_name_author(line, md_file_name)
                book = Book(book_id, book_name, author)
                books[book.book_id] = book
                quotes[book_id] = []
            elif line.startswith('*'): # new quote starts
                book.n_quotes += 1
                quotes[book_id].append(line.lstrip('* '))
            else:
                quotes[book_id][-1] += line

    books = [book for book_id, book in books.items() if book.n_quotes > 0]
    quotes = [Quote(f'{n}-{book_id}', book_id, quote) for book_id, quote_list in quotes.items() for n, quote in enumerate(quote_list) if quote_list]

    return books, quotes

def get_book_name_author(line, file_name):
    try:
        book_name, author = line.strip('#\n').split('/')
    except ValueError:
        print(f'Wrong format in book header -> {line.strip()} in {file_name}')
        print('The format should be book_name/author')
        print('Correct format and run -makedb again')
        sys.exit(1)
    return book_name, author

def make_update_db(books_table, quotes_table):
    quotes_files = sorted([xfile for xfile in os.listdir(os.curdir) if xfile.endswith('.md')])
    for md_file_name in quotes_files:
        books, quotes = read_md_file(md_file_name)
        if books and quotes:
            books_table.add_books(books)
            quotes_table.add_quotes(quotes)
