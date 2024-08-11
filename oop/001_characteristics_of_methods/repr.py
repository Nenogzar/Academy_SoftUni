class MyClass:
    def __repr__(self):
        return "MyClass(value=42)"


"""
1. Цел:
Методът __repr__ предоставя официално, недвусмислено представяне на обекта, 
което е предназначено за разработчици и често се използва за дебъгване.
2. Извикване:
Автоматично се извиква, когато обектът се предаде на функцията repr() или 
когато обектът се покаже в интерактивната конзола.
"""


class MyClass1:
    def __repr__(self):
        return "MyClass1()"


obj = MyClass1()
print(repr(obj))  # MyClass()

"""
3. Връщаща стойност:
Трябва да връща стринг (str), който представлява обекта по начин, 
който би трябвало да позволи възстановяване на обекта чрез eval().
"""
class MyClass2:
    def __repr__(self):
        return "MyClass2(value=42)"

val = MyClass2()
print(val.__repr__())   # MyClass2(value=42)

"""
4. Официално и точно представяне:
Стрингът, върнат от __repr__, трябва да бъде официално представяне на обекта, 
което предоставя достатъчно информация за неговото създаване и състояние.
"""

class Person:
    """

    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age})"

person = Person("Ivan", 35)
print(repr(person))           # Person(name='Ivan', age=35)

"""
5. Полезен за дебъгване:
Предназначен е да предоставя информация, която е полезна за дебъгване и разработка, 
като помага на разработчиците да виждат състоянието на обектите.
"""

class Point:
    """

    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

p = Point(2, 3)
print(repr(p))  # Point(x=2, y=3)


"""
6. Възможност за използване с eval():
Желателно е стрингът, върнат от __repr__, 
да може да бъде използван с eval() за възстановяване на обекта, ако е възможно.
"""

class Rectangle:
    """

    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f"{self.width} + {self.height}"

r = Rectangle(4, 5)
r_repr = repr(r)
print(r_repr)  # 4 + 5
r_new = eval(r_repr)
print(r_new)  # 9

"""
7. Взаимодействие с други методи:
Може да съществува заедно с __str__, като __repr__ предоставя по-формално представяне, 
докато __str__ предоставя по-човешко четимо представяне.
"""

class Car:
    """

    """
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"{self.make} {self.model}"

    def __repr__(self):
        return f"Car(make={self.make!r}, model={self.model!r})"

car = Car("Toyota", "Corolla")
print(str(car))  # Toyota Corolla
print(repr(car))  # Car(make='Toyota', model='Corolla')

"""
8. Пример за сложни обекти:
Може да бъде използван за сложни обекти и структури от данни 
за предоставяне на ясна и изчерпателна информация за тяхното състояние.
"""

class Matrix:
    """

    """
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"Matrix ={self.data}"

m = Matrix([[1, 2], [3, 4]])
print(repr(m))  # Matrix =[[1, 2], [3, 4]]


# Използване на __repr__:

"""
1. Дефиниране на __repr__ метод:
Създайте клас и дефинирайте метода __repr__ за предоставяне на официално представяне.
"""

class User:
    """

    """
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return f"User {self.username} whit  email: {self.email!r})"

user = User("John_Doe", "john@example.com")
print(repr(user))  # User John_Doe whit  email: 'john@example.com')

"""
2. Използване в списъци и колекции:
Когато обектите са част от списъци или други колекции, __repr__ осигурява полезна информация при отпечатването им.
"""

users = [User("john_doe", "john@example.com"), User("Hana_Banana", "Hana@example.com")]
print(users)
# [User john_doe whit  email: 'john@example.com'), User Hana_Banana whit  email: 'Hana@example.com')]


"""
3. Дебъгване и логиране:
Използвайте __repr__ за логиране на състоянието на обекти по време на дебъгване и диагностика на проблеми.
"""

import logging

logging.basicConfig(level=logging.DEBUG)

class Order:
    """

    """
    def __init__(self, order_id: int, product: str, quantity: int):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity

    def __repr__(self):
        return f"Order(order_id={self.order_id}, product={self.product!r}, quantity={self.quantity})"

order = Order(1, "Laptop", 2)
logging.debug(repr(order))
# DEBUG:root:Order(order_id=1, product='Laptop', quantity=2)


"""
Тези характеристики и примери подчертават значението на метода __repr__ за предоставяне на официално 
и полезно представяне на обектите, което е особено полезно за дебъгване и логиране.
"""
