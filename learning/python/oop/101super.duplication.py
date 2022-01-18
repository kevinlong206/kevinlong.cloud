class Book:
    def __init__(self, title, publisher, pages):
        self.title = title
        self.publisher = publisher
        self.pages = pages

class EBook(Book):
    # BAD PRACTICE, redundant !
    def __init__(self, title, publisher, pages, format_):
        self.title = title
        self.publisher = publisher
        self.page = pages
        self.format_ = format
