from rich.table import Table
from rich.console import Console

def make_table_books(table, books):
    table.add_column('ID', justify='left')
    table.add_column('Name', justify='left')
    table.add_column('Author', justify='left')
    table.add_column('Quotes', justify='left')

    for book in books:
        table.add_row(book.id_, book.book_name, book.author, str(book.n_quotes))
    return table

def make_table_quotes(): pass

def print_table(entries):
    table = Table(show_header=True, header_style='bold green')
    table = make_table_books(table, entries)
    console = Console()
    console.print(table)