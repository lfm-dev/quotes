def get_tags(books):
    tags = {}
    for book in books:
        for tag in book.tags:
            if tag in tags:
                tags[tag] += 1
            else:
                tags[tag] = 1
    return tags
