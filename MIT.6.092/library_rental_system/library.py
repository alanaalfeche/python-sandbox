from book import Book


class Library:
    def __init__(self, name, hours, address, books):
        self.name = name
        self.hours = hours
        self.address = address
        self.books = books

    
    def get_name(self):
        return self.__str__(self.name)


    def get_library_hours(self):
        return self.__str__(self.hours)


    def get_address(self):
        return self.__str__(self.address)


    def get_books(self):
        available_books = []
        for book in self.books:
            if not book.is_borrowed():
                available_books.append(book.title)

        return self.__str__(available_books)


    def get_book(self, title):
        for book in self.books:
            if book.title == title:
                return book


    def add_book(self, title):
        new_book = Book(title)
        self.books.append(new_book)


    def borrow_book(self, title):
        book = self.get_book(title)
        book.borrow()


    def return_book(self, title):
        book = self.get_book(title)
        book.__return__()

    
    def is_borrowed(self, title):
        book = self.get_book(title)
        return self.__str__(book.is_borrowed())


    def __str__(self, entry):
        print(entry)