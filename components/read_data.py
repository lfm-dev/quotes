from classes.Quote import Quote
from classes.Book import Book

def make_quotes(quotes):
    quotes = [Quote(book_id, quote) for book_id in quotes for quote in quotes[book_id]]
    return quotes

def read_md_file(md_file_name):
    quotes = {}
    books = []
    with open(md_file_name) as file_handle:
        for line in file_handle:
            if not line.strip():
                continue
            if line.startswith('#'):
                id_, book_name, author = get_book_data(line)
                quotes[id_] = []
                book = Book(id_, book_name, author)
                books.append(book)
            elif line.startswith('*'):
                book.n_quotes += 1
                quotes[id_].append('')
                quotes[id_][-1] += line.lstrip('* ')
            else:
                quotes[id_][-1] += line
    quotes = [Quote(book_id, quote) for book_id in quotes for quote in quotes[book_id]]
    return books, quotes

def get_book_data(line):
    return line[1:].strip().split('/')