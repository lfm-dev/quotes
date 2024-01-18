import os
from rich.table import Table
from rich.console import Console
from rich.markdown import Markdown

def print_books_table(books):
    table = Table(show_header=True, header_style='bold green')
    table.add_column('ID', justify='left')
    table.add_column('Name', justify='left')
    table.add_column('Author', justify='left')
    table.add_column('Quotes', justify='left')

    for book in books:
        table.add_row(book.book_id, book.book_name, book.author, str(book.n_quotes))

    console = Console()
    console.print(table)

def print_quotes_markdown(quotes):
    quotes_markdown = Markdown(f'# {quotes[0].book_name}\n{(os.linesep).join([f"* {quote.quote}" for quote in quotes])}')
    console = Console()
    console.print(quotes_markdown)