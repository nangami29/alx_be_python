class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title}, {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size= file_size

    def __str__(self):
        return f"{self.title}, {self.author}, {self.file_size}"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count= page_count

    def __str__(self):
        return f"{self.title}, {self.author}, {self.page_count}"


class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        if isinstance(book, Book):  # Check if it's a Book or subclass
            self.books.append(book)
        elif isinstance(book, EBook):
            self.books.append(book)
        else :
            self.books.append(book)
    

    def list_books(self):
        
        print (f"Book:{self.title} by {self.author}" )
        print (f"Ebook: {self.title} by {self.author}, File Size: {self.file_size}")
        print (f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}")