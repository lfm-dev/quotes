class Author:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.tags = []

    def __repr__(self):
        return f'{self.name} {len(self.books)}'
