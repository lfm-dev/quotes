import os
import sys
from classes.Book import Book

def read_md_file(md_file_name):
    books = []
    year = md_file_name.split('.')[0] # md name: year.md
    with open(md_file_name, encoding="utf-8") as file_handle:
        book_number = 0
        for line in file_handle:
            if not line.strip():
                continue
            if line.startswith('#'):
                book_number += 1
                book_id = f'{year[-2:]}-{book_number}'
                book_name, author, is_favorite = get_book_name_author(line, md_file_name)
                books.append(Book(book_id, book_name, author, year, is_favorite))
            elif line.startswith('[') and line.strip().endswith(']'):
                if len(line.strip()) == 2: # line = []
                    continue
                books[-1].tags = line.lower().strip('[]\n').split(',')
            elif line.startswith('*'): # new quote starts
                books[-1].quotes.append(line.lstrip('* '))
            else:
                books[-1].quotes[-1] +=  '\n  ' + line # newline in markdown
    return books

def get_book_name_author(line, file_name):
    is_favorite = line.strip().endswith('*')
    try:
        book_name, author = line.strip('*#\n').split('/')
    except ValueError:
        print(f'Wrong format in book header -> {line.strip()} in {file_name}')
        print('The format should be book_name/author')
        print('Correct format and run -makedb again')
        sys.exit(1)
    return book_name, author, is_favorite

def get_books():
    quotes_files = sorted([xfile for xfile in os.listdir(os.curdir) if xfile.endswith('.md')])
    books = []
    for md_file_name in quotes_files:
        books += read_md_file(md_file_name)
    return books
