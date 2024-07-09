"""
1 Дефиниция:

Обикновени методи, които се дефинират вътре в клас и първият им параметър е винаги self.
self е референция към текущата инстанция на класа, което позволява достъп до атрибутите и другите методи на инстанцията.
Декларация:

2 Декларират се като нормални функции вътре в класа, като първият параметър задължително е self.
"""


class MyClass:
    def instance_method(self):
        pass


"""
3. Достъп до атрибути:
Чрез self методът има достъп до атрибутите на инстанцията.
"""


class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof!"


"""
4.Извикване:
Извикват се чрез инстанция на класа.
Например, ако dog е инстанция на класа Dog, тогава dog.bark() извиква метода bark.
"""

dog = Dog("Rex")
print(dog.bark())  # Rex says woof!


"""
5. Модификация на атрибути:
Могат да променят атрибутите на инстанцията чрез self.

"""


class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1


counter = Counter()
counter.increment()
print(counter.count)  # 1


"""
6. Използване на други методи:
Могат да извикват други методи на инстанцията чрез self.
"""


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def describe(self):
        return f"Circle with radius {self.radius}, area {self.area()}, and perimeter {self.perimeter()}"

"""
7. Обхват:

Обикновените методи са достъпни само за инстанциите на класа и не могат да бъдат извикани директно чрез името на класа (освен ако не се използва инстанция).
Употреба:

Използват се за работа с данни и поведение, специфични за инстанцията на класа.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


person = Person("Alice", 30)
print(person.greet())  # Hello, my name is Alice and I am 30 years old.

"""

"""