from rich.table import Table
from rich.console import Console

def make_table_entries(table, entries):
    table.add_column('ID', justify='left')
    table.add_column('Name', justify='left')
    table.add_column('Author', justify='left')
    table.add_column('Quotes', justify='left')

    for entry in entries:
        table.add_row(entry.id_, entry.book_name, entry.author, str(entry.n_quotes))
    return table

def make_table_quotes(): pass

def print_table(entries):
    table = Table(show_header=True, header_style='bold green')
    table = make_table_entries(table, entries)
    console = Console()
    console.print(table)