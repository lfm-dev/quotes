import os
from rich.table import Table
from rich.console import Console
from rich.markdown import Markdown

def print_authors_table(authors):
    table = Table(show_header=True, header_style='bold green')
    table.add_column('Name', justify='left')
    table.add_column('Books', justify='center')

    for author in authors:
        table.add_row(author.name, str(len(author.books)), end_section=True)

    console = Console()
    console.print(table)

def print_books_table(books):
    table = Table(show_header=True, header_style='bold green')
    table.add_column('ID', justify='left')
    table.add_column('Name', justify='left')
    table.add_column('Author', justify='left')
    table.add_column('Quotes', justify='center')
    table.add_column('Tags', justify='center')

    for n_book, book in enumerate(books):
        end_section = True if n_book == len(books)-1 else book.year_read != books[n_book+1].year_read # line between books read in different years
        book_tags = (" ").join(book.tags) if book.tags else "---"
        table.add_row(book.book_id, book.book_name, book.author, str(len(book.quotes)), book_tags, end_section=end_section)

    console = Console()
    console.print(table)

def print_quotes_markdown(book):
    quotes_markdown = Markdown(f'# {book.book_name} ({book.author})\n{(os.linesep).join([f"* {quote}" for quote in book.quotes])}')
    console = Console()
    console.print(quotes_markdown)
