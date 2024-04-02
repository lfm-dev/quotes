import argparse

def get_args():
    parser = argparse.ArgumentParser(prog='quotes', description='Manage your book quotes')
    parser.add_argument('-b', '-books', metavar='', dest='show_books', nargs='?', const=' ', help='search books by name, author, tag, reading year or favorites (favs) (-b shows all books)')
    parser.add_argument('-q', '-quotes', metavar='', dest='show_quotes', help='show all quotes of a book by book ID')
    parser.add_argument('-a', '-authors', action='store_true', dest='show_authors', help='show authors table')
    parser.add_argument('-t', '-tags', action='store_true', dest='show_tags', help='show tags table')
    args = parser.parse_args()
    return args, parser
