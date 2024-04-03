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
    book_list = list(books.values())

    if not query: # print all books
        filtered_books = book_list
    elif query == 'favs':
        filtered_books = [book for book in book_list if book.is_favorite]
    else:
        filtered_books = [book for book in book_list if hit(book, query)]

    return filtered_books
