class MyClass:
    def __str__(self):
        return "This is a MyClass object"


obj = MyClass()
print(obj)  # This is a MyClass object

"""
1. Цел:
Методът __str__ предоставя неформално, лесно четимо представяне на обекта, 
което е предназначено за хора, а не за машини.

2. Извикване:
Автоматично се извиква, когато обектът се предаде на функцията print() или str(), 
както и когато обектът се използва в контекст, изискващ стринг представяне (например във форматни стрингове).

3. Връщаща стойност:
Трябва да връща стринг (str), който представлява обекта.
"""


class MyClass1:
    def __str__(self):
        return "String representation of MyClass1"


"""
4. Човешко-четим формат:
Стрингът, върнат от __str__, трябва да бъде лесен за четене и разбиране от хора. 
Той обикновено съдържа полезна информация за състоянието на обекта.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"


person = Person("Ivan", 35)
print(person)  # Person(name=Ivan, age=35)

"""
5. Промяна на поведението на print():
Позволява дефиниране на поведението на обекта при извикване на print(), 
така че да предостави смислена информация.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"


p = Point(2, 3)
print(p)  # Point(2, 3)

"""
6. Съвместимост с други методи:
Може да бъде използван заедно с други методи за предоставяне на различни нива на детайлност в представянето на обекта.
"""


class Car:
    def __init__(self, *data):
        [self.make,
         self.model] = data

    def __str__(self):
        return f"{self.make} {self.model}"

    def __repr__(self):
        return f"Car(make={self.make!r}, model={self.model!r})"


car = Car("Toyota", "Corolla")
print(str(car))  # Toyota Corolla
print(repr(car))  # Car(make='Toyota', model='Corolla')

"""
7. Дефиниция в базовите класове:
Може да се дефинира в базовите класове и да бъде наследяван от под-класовете, които могат да го пренаписват при нужда.
"""


class Base:
    def __str__(self):
        return "Base class"


class Derived(Base):
    def __str__(self):
        return "Derived class"


b = Base()
d = Derived()
print(b)  # Base class
print(d)  # Derived class

"""
8. Лесно тестване и дебъгване:
Предоставянето на смислено стринг представяне чрез __str__ улеснява тестването и дебъгването на обектите, 
тъй като осигурява полезна информация за състоянието на обекта.
"""


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product(name={self.name}, price={self.price})"


product = Product("Laptop", 1200)
print(product)  # Product(name=Laptop, price=1200)

"""
9. Не замества __repr__:
__str__ и __repr__ могат да съществуват едновременно в един и същ клас, 
като __repr__ е по-формален и предназначен за разработчици, 
докато __str__ е за крайни потребители.
"""


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r})"


lord = Book("Lord", "J.R")

print(lord.__str__())  # Book: Lord by J.R
print(lord.__repr__())  # Book(title='Lord', author='J.R')

"""
Тези характеристики правят метода __str__ важен за предоставяне на лесно четимо и 
смислено представяне на обектите, което улеснява тяхното използване и разбиране.
"""
