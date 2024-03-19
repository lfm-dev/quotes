def filter_books(books, query):
    '''
    filter books by book name, author or tag
    '''
    filtered_books = []
    for book in books.values():
        if not query:
            filtered_books = list(books.values())
        elif query in book.book_name.casefold() or query in book.author.casefold() or query in book.tags:
            filtered_books.append(book)
    return filtered_books
