def hit(book, query):
    if query == book.book_id:
        return True
    if query in book.book_name.casefold().split():
        return True
    if query in book.author.casefold().split():
        return True
    if query in book.tags:
        return True
    if query == book.reading_year:
        return True
    return False

def filter_books(books, query):
    '''
    filter books by book name, author or tag
    '''
    if not query: # print all books
        filtered_books = list(books.values())
    else:
        filtered_books = []
        for book in books.values():
            if hit(book, query):
                filtered_books.append(book)
    return filtered_books
