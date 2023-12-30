import argparse

def get_args():
    parser = argparse.ArgumentParser(prog='quotes', description='Manage your book quotes')
    parser.add_argument('-makedb', action='store_true', dest='makedb', help='Make (or update) sqlite3 db')
    parser.add_argument('-b', '-books', metavar='', dest='books', help='Search books by name or author ("all" to show all books)')
    parser.add_argument('-q', '-quotes', metavar='', dest='quotes', help='Show all quotes of a book by book ID')
    args = parser.parse_args()
    return args, parser