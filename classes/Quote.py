class Quote:
    def __init__(self, quote_id, book_id, quote):
        self.quote_id = quote_id
        self.book_id = book_id
        self.quote = quote.rstrip()

    def __repr__(self):
        return f'({self.quote_id}) {self.quote}'