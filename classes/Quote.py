class Quote:
    def __init__(self, book_id, quote):
        self.book_id = book_id
        self.quote = quote.rstrip()

    def __repr__(self):
        return self.quote