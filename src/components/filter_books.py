def filter_by_author_book_name(books, book_name_author):
    filtered_books = []
    for _, book in books.items():
        if book_name_author.casefold() in book.book_name.casefold() or book_name_author.casefold() in book.author.casefold() or book_name_author == 'all':
            filtered_books.append(book)
    return filtered_books
