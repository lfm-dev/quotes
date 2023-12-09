class Entry:
    def __init__(self, id_, book_name, author):
        self.id_ = id_
        self.book_name = book_name
        self.author = author
        self.quotes = []
        self.n_quotes = 0
        self.tags = []
        self.reading_date = self.get_reading_date()

    def add_quote(self, quote):
        self.quotes.append(quote)
        self.n_quotes += 1

    def add_tags(self, line):
        self.tags = line.strip()[1:-1].split(',')

    def get_reading_date(self):
        return '20' + self.id_[1:self.id_.find('-')] # this will work until the year 2100

    def __repr__(self):
        return f'{self.id_} {self.book_name} {self. author} {self.n_quotes}'
