from classes.Quote import Quote

def filter_quotes(books, query):
    quotes = []
    for book in books:
        for quote in book.quotes:
            if query in quote:
                quotes.append(Quote(book.book_name, book.author, quote))
    return quotes
