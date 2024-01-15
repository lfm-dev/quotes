class Book:
    def __init__(self, book_id, book_name, author, n_quotes = 0):
        #TODO make auto book_id
        self.book_id = book_id
        self.book_name = book_name
        self.author = author
        self.n_quotes = n_quotes

    def get_data(self):
        return (self.book_id, self.book_name, self.author, self.n_quotes)

    def __repr__(self):
        return f'{self.book_id} {self.book_name} {self. author} {self.n_quotes}'