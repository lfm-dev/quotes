from classes.Author import Author

def get_authors(books):
    authors = {}
    for book in books:
        if book.author not in authors:
            authors[book.author] = Author(book.author)

        authors[book.author].books.append(book)
        authors[book.author].tags = list(set(authors[book.author].tags + book.tags))

    authors = list(authors.values())
    authors.sort(key = lambda x: x.name)

    return authors
