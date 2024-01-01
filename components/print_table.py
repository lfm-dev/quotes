from rich.table import Table
from rich.console import Console

def make_table_books(table, books):
    table.add_column('ID', justify='left')
    table.add_column('Name', justify='left')
    table.add_column('Author', justify='left')
    table.add_column('Quotes', justify='left')

    for book in books:
        table.add_row(book.book_id, book.book_name, book.author, str(book.n_quotes))
    return table

def make_table_quotes(table, quotes):
    table.add_column('Quotes', justify='left')

    for quote in quotes:
        table.add_row(quote.quote, end_section=True)
    return table

def print_table(entries, table_type):
    table = Table(show_header=True, header_style='bold green')
    if table_type == 'books':
        table = make_table_books(table, entries)
    elif table_type == 'quotes':
        table = make_table_quotes(table, entries)
    console = Console()
    console.print(table)