class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page
    def __str__(self):
        return f"{self.author} - {self.title}"

class Library:

    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))



    def get_books(self, title):
        try:
            book = [book for book in self.books if book.title == title][0]
            return book
        except IndexError:
            return f"Sorry, {title} doesn't exist"


    def remove_book(self, title):
        for b in self.books:
            if b.title == title:
                self.books.remove(b)






library = Library()
for num in range(1,6):
    b = Book(f"Title {num}", f"Author {num}")
    library.add_book(b.title, b.author)

print(library.get_books("Title 1"))
print(library.get_books("Title 2"))
print(library.get_books("Title 3"))
print(library.get_books("Title 4"))
print(library.get_books("Title 5"))
print(library.get_books("Title 6"))
print(library.get_books("Title 7"))

