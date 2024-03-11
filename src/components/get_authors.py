from classes.Author import Author

def get_authors(books):
    authors = {}
    for book in books.values():
        if book.author in authors:
            authors[book.author].books.append(book)
        else:
            author = Author(book.author)
            author.books.append(book)
            authors[book.author] = author

    authors = list(authors.values())
    authors.sort(key = lambda x: x.name)

    return authors
