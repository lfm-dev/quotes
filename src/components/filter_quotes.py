from classes.Quote import Quote

def filter_quotes(books, query):
    quotes = []
    for book in books.values():
        for quote in book.quotes:
            if query in quote:
                quote = Quote(book.book_name, book.author, quote)
                quotes.append(quote)
    return quotes
