def filter_books(books, query):
    '''
    filter books by book name, author or tag
    '''
    filtered_books = []
    for _, book in books.items():
        if query.casefold() in book.book_name.casefold() or query.casefold() in book.author.casefold() or query.casefold() in book.tags or not query:
            filtered_books.append(book)
    return filtered_books
