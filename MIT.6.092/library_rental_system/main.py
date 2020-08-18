from book import Book
from library import Library

book = Book('The Da Vinci Code')
book.get_title()    # The Da Vinci Code
book.is_borrowed()  # False
book.borrow()       # Success
book.is_borrowed()  # True
book.__return__()   # Success
book.is_borrowed()  # False


library = Library('NPL', '9 AM to 5 PM', '10 Main St.', [])
library.get_name()
library.get_library_hours()
library.get_address()
library.add_book('The Da Vinci Code')
library.add_book('Le Petit Prince')
library.add_book('A Tale of Two Cities')
library.add_book('The Lord of the Rings')
library.get_books()
library.borrow_book('The Da Vinci Code')
library.get_books()
library.is_borrowed('The Da Vinci Code')
library.return_book('The Da Vinci Code')
library.get_books()
