import os
from classes.classes import Entry
from classes.classes import DB
from print_table import print_table

def add_data_to_db(db, entries):
    books_data = [(entry.id_, entry.book_name, entry.author, entry.n_quotes) for entry in entries]
    quotes_data = [(entry.id_, quote) for entry in entries for quote in entry.quotes]
    db.insert_data('books', books_data)
    db.insert_data('quotes', quotes_data)

def get_entry_data(line):
    return line[1:].strip().split('/')

def read_md_file(md_file_name):
    quotes = {}
    entries = []
    with open(md_file_name) as file_handle:
        for line in file_handle:
            if not line.strip():
                continue
            elif line.startswith('#'):
                id_, book_name, author = get_entry_data(line)
                quotes[book_name] = []
                entry = Entry(id_, book_name, author)
                entries.append(entry)
            elif line.startswith('*'):
                quotes[book_name].append('')
                quote_number = len(quotes[book_name])-1
                quotes[book_name][quote_number] += line.lstrip('* ')
            else:
                quotes[book_name][quote_number] += line
    return entries, quotes

def add_quotes_to_entries(entries, quotes):
    for entry in entries:
        for quote in quotes[entry.book_name]:
            entry.add_quote(quote.strip()) # remove last \n

def create_tables(db):
    db.create_table('books', 'book_id TEXT PRIMARY KEY', 'book_name TEXT', 'author TEXT', 'n_quotes INTEGER')
    db.create_table('quotes', 'book_id TEXT', 'quote TEXT')

def main():
    quotes_path = '/path/to/your/quotes/folder'
    os.chdir(quotes_path)

    db = DB('book_quotes.db')
    create_tables(db)

    quotes_files = sorted([xfile for xfile in os.listdir(os.curdir) if xfile.endswith('.md')])
    for md_file_name in quotes_files:
        entries, quotes = read_md_file(md_file_name)
        add_quotes_to_entries(entries, quotes)
        add_data_to_db(db, entries)
        print_table(entries)

if __name__ == '__main__':
    main()