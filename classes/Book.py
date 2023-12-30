class Book:
    def __init__(self, id_, book_name, author, n_quotes = 0):
        self.id_ = id_
        self.book_name = book_name
        self.author = author
        self.n_quotes = n_quotes

    def __repr__(self):
        return f'{self.id_} {self.book_name} {self. author} {self.n_quotes}'