from abc import ABC, abstractmethod

class Author:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

class Book:
    def __init__(self, title: str, author: Author):
        self.title = title
        self.author = author

class BaseFormatter(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        return book.title


class PaperFormater(BaseFormatter):
    def format(self, book: Book) -> str:
        return book.title[:2]


class InstagramFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return book.title[:5]


class TwitterFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return book.title[:12]


class Printer:
    def get_book(self, book: Book, formatter: BaseFormatter) -> Book:
        formatted_book = formatter.format(book)
        return formatted_book


au = Author('Ivan', 'Vazov')
book1 = Book('Mamino detence', au)

p = Printer()
print(p.get_book(book1, PaperFormater()))
print(p.get_book(book1, InstagramFormatter()))
print(p.get_book(book1, TwitterFormatter()))
print(au)