import os
from rich.table import Table
from rich.console import Console
from rich.markdown import Markdown

def print_authors_table(authors):
    table = Table(show_header=True, header_style='bold green')
    table.add_column('Name', justify='left')
    table.add_column('Books', justify='center')
    table.add_column('Tags', justify='center')

    for author in authors:
        author_tags = (' ').join(sorted(author.tags)) if author.tags else '---'
        table.add_row(author.name, str(len(author.books)), author_tags, end_section=True)

    console = Console()
    console.print(table)

def print_tags_table(tags):
    sorted_tags = sorted(list(tags.keys()))
    table = Table(show_header=True, header_style='bold green')
    table.add_column('Tag', justify='left')
    table.add_column('Books', justify='center')

    for tag in sorted_tags:
        table.add_row(tag, str(tags[tag]))

    console = Console()
    console.print(table)

def print_books_table(books):
    table = Table(show_header=True, header_style='bold green')
    table.add_column('ID', justify='left')
    table.add_column('F', justify='center')
    table.add_column('Name', justify='left')
    table.add_column('Author', justify='left')
    table.add_column('Tags', justify='center')

    for n_book, book in enumerate(books):
        end_section = True if n_book == len(books)-1 else book.reading_year != books[n_book+1].reading_year # line between books read in different years
        book_tags = (' ').join(book.tags) if book.tags else '---'
        is_favorite = '*' if book.is_favorite else ''
        table.add_row(book.book_id, is_favorite, book.book_name, book.author, book_tags, end_section=end_section)

    console = Console()
    console.print(table)

def print_book_quotes_markdown(book):
    quotes_markdown = Markdown(f'# {book.book_name} ({book.author})\n{(os.linesep).join([f"* {quote}" for quote in book.quotes])}')
    console = Console()
    console.print(quotes_markdown)

def print_quotes_markdown(quotes):
    quotes_markdown = Markdown(f'{(os.linesep).join([f"* {quote.quote} ({quote.book_name}, {quote.author})" for quote in quotes])}')
    console = Console()
    console.print(quotes_markdown)
