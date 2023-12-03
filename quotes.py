import os
from rich.table import Table
from rich.console import Console

class Entry:
    def __init__(self, id_, name, author):
        self.id_ = id_
        self.name = name
        self.author = author
        self.quotes = []
        self.n_quotes = 0
        self.tags = []
        self.reading_date = self.get_reading_date()

    def add_quote(self, quote):
        self.quotes.append(quote)
        self.n_quotes += 1

    def add_tags(self, line):
        self.tags = line.strip()[1:-1].split(',')
    
    def get_reading_date(self):
        return '20' + self.id_[1:self.id_.find('-')] # this will work until the year 2100

    def __repr__(self):
        return f'{self.id_} {self.name} {self. author} {self.n_quotes}'

def get_reading_date(file_name):
    return file_name[file_name.find('-')+1:file_name.find('.', file_name.find('-'))]

def get_entry_data(line):
    return line[1:].strip().split('/')

def read_md_file(md_file_name):
    entries = []
    quote = ''
    file_handle = open(md_file_name)

    for line in file_handle:
        if not line.strip():
            continue
        elif line.startswith('#'):
            if quote: # last quote for previous entry
                entry.add_quote(quote)
                quote = ''
            id_, name, author = get_entry_data(line)
            entry = Entry(id_, name, author)
            entries.append(entry)
        elif line.startswith('['):
            entry.add_tags(line)
        elif line.startswith('*'):
            if quote:
                entry.add_quote(quote)
                quote = ''
            quote = line[1:].lstrip()
        else:
            quote += line
    entry.add_quote(quote) # last quote of file

    file_handle.close()

    return entries

def make_table_entries(table, entries):
    table.add_column('ID', justify='left')
    table.add_column('Name', justify='left')
    table.add_column('Author', justify='left')
    table.add_column('Quotes', justify='left')

    for entry in entries:
        table.add_row(entry.id_, entry.name, entry.author, str(entry.n_quotes))
    return table

def make_table_quotes(): pass

def print_table(entries):
    table = Table(show_header=True, header_style='bold green')
    table = make_table_entries(table, entries)
    console = Console()
    console.print(table)

def main():
    quotes_path = '/path/to/your/quotes/folder'
    os.chdir(quotes_path)

    quotes_files = sorted([xfile for xfile in os.listdir(os.curdir) if xfile.endswith('.md')])
    for md_file_name in quotes_files:
        entries = read_md_file(md_file_name)
        print_table(entries)

if __name__ == '__main__':
    main()