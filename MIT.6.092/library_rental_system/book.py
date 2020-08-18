class Book:
    def __init__(self, title, borrowed=False):
        self.title = title
        self.borrowed = borrowed

    
    def get_title(self):
        return self.title


    def is_borrowed(self):
        return self.borrowed


    def borrow(self):
        if not self.borrowed:
            self.borrowed = True


    def __return__(self):
        self.borrowed = False
