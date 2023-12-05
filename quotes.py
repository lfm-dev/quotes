import os
from classes.classes import Entry
from print_table import print_table

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

def main():
    quotes_path = '/path/to/your/quotes/folder'
    os.chdir(quotes_path)

    quotes_files = sorted([xfile for xfile in os.listdir(os.curdir) if xfile.endswith('.md')])
    for md_file_name in quotes_files:
        entries = read_md_file(md_file_name)
        print_table(entries)

if __name__ == '__main__':
    main()