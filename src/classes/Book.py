class Book:
    def __init__(self, book_id, book_name, author, n_quotes = 0):
        self.book_id = book_id
        self.book_name = book_name
        self.author = author
        self.year_read = self.get_year_read()
        self.n_quotes = n_quotes

    def get_data(self):
        return (self.book_id, self.book_name, self.author, self.n_quotes)

    def get_year_read(self):
        return int(self.book_id.split('-')[0])

    def __repr__(self):
        return f'{self.book_id} {self.book_name} {self. author} {self.n_quotes}'