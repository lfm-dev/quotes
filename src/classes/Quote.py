class Quote:
    def __init__(self, quote_id, book_id, book_name, quote):
        self.quote_id = quote_id
        self.book_id = book_id
        self.book_name = book_name
        self.quote = quote.rstrip()

    def get_data(self):
        return (self.quote_id, self.book_id, self.book_name, self.quote)

    def __repr__(self):
        return f'({self.quote_id}) {self.quote}'