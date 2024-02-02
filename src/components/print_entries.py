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

    for n_book, book in enumerate(books):
        end_section = True if n_book == len(books)-1 else book.year_read != books[n_book+1].year_read # line between books read in different years
        table.add_row(book.book_id, book.book_name, book.author, str(book.n_quotes), end_section=end_section)

    console = Console()
    console.print(table)

def print_quotes_markdown(quotes, book_name, author):
    quotes_markdown = Markdown(f'# {book_name} ({author})\n{(os.linesep).join([f"* {quote.quote}" for quote in quotes])}')
    console = Console()
    console.print(quotes_markdown)