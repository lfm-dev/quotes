class Book:
    def __init__(self, book_id, book_name, author, reading_year):
        self.book_id = book_id
        self.book_name = book_name
        self.author = author
        self.reading_year = reading_year
        self.quotes = []
        self.tags = []

    def __repr__(self):
        return f'{self.book_id} {self.book_name} {self. author}'
