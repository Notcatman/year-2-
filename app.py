class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author 
        self.year = year

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        for n in self.books:
            if n.title == book.title and n.author == book.author and n.year == book.year:
                print(f'The book "{book.title}" is already in library')
                return
        self.books.append(book)
        print(f'Book "{book.title}" was added.')


    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f'book "{book.title}" was removed.')

    def list_books(self):
        print("book list:")
        for book in self.books:
            print(f"{book.title} by {book.author} ({book.year})")


library = Library()
book1 = Book("It", "Stephen King", 1986)
book2 = Book("Adventures of Huckleberry Finn", "Mark Twain", 1884)
book3 = Book("The Master and Margarita", "Mikhail Bulgakov", 1928)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.list_books()
library.remove_book('It')
library.list_books()