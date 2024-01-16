import os
from rich.table import Table
from rich.console import Console
from rich.markdown import Markdown

def make_table_books(books):
    table = Table(show_header=True, header_style='bold green')
    table.add_column('ID', justify='left')
    table.add_column('Name', justify='left')
    table.add_column('Author', justify='left')
    table.add_column('Quotes', justify='left')

    for book in books:
        table.add_row(book.book_id, book.book_name, book.author, str(book.n_quotes))
    return table

def make_markdown_quotes(quotes):
    quotes_markdown = Markdown(f'# {quotes[0].book_name}\n{(os.linesep).join(["* " + quote.quote for quote in quotes])}')
    return quotes_markdown

def print_entries(entries, table):
    if table.value == 'books':
        entries = make_table_books(entries)
    elif table.value == 'quotes':
        entries = make_markdown_quotes(entries)
    console = Console()
    console.print(entries)