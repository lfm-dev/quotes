def filter_books(books, query):
    '''
    filter books by book name, author or tag
    '''
    filtered_books = []
    for book in books.values():
        if query in book.book_name.casefold() or query in book.author.casefold() or query in book.tags or not query:
            filtered_books.append(book)
    return filtered_books
