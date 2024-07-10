"""
1. Дефиниция:

Статичните методи са функции, дефинирани вътре в клас, които не са свързани с конкретна инстанция на класа.
Не приемат нито self, нито cls като първи параметър.
Създават се с декоратора @staticmethod.

2. Декларация:

Декларират се с декоратора @staticmethod преди дефиницията на метода.
"""

class MyClass:
    @staticmethod
    def static_method():
        pass
"""
3.Нямат достъп до инстанционни или класови атрибути:
Статичните методи нямат достъп до атрибутите и методите на инстанцията (self) или на класа (cls).
"""


class NewClass:
    attribute = "class attribute"

    @staticmethod
    def static_method():
        return "static method called"


"""
4. Извикване:
Могат да се извикват както чрез инстанции на класа, така и директно чрез самия клас.
"""

# Извикване чрез класа
print(NewClass.static_method())  # static method called

# Извикване чрез инстанция на класа
instance = NewClass()
print(instance.static_method())  # static method called

"""
5. Употреба:
Използват се за операции, които са свързани с класа, но не се нуждаят от достъп до атрибути на инстанцията или класа.
Подходящи са за помощни функции, които логически принадлежат на класа, 
    но не изискват използване на данни от инстанцията или класа.

"""
class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(5, 3))  # 8

"""
6. Могат да бъдат извиквани извън класа:
Понеже нямат нужда от инстанция на класа, статичните методи могат да бъдат извиквани независимо от контекста на класа.
"""

class Utils:
    @staticmethod
    def is_even(number):
        return number % 2 == 0

print(Utils.is_even(4))  # True
print(Utils.is_even(5))  # False

"""
7. Подходящи за функционално програмиране:
Статичните методи могат да се използват за прилагане на принципи от функционалното програмиране вътре в обектно-ориентирани класове.
"""

class Converter:
    @staticmethod
    def to_fahrenheit(celsius):
        return celsius * 9/5 + 32

    @staticmethod
    def to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

print(Converter.to_fahrenheit(0))  # 32.0
print(Converter.to_celsius(32))    # 0.0


"""
8. Използване на декоратори и други функции:
Могат да бъдат декорирани с други декоратори или да се използват като помощни функции вътре в класа.
"""

class Example:
    @staticmethod
    def static_method():
        print("Static method")

    @staticmethod
    def decorated_static_method():
        Example.static_method()
        print("Decorated static method")

Example.decorated_static_method()
# Static method
# Decorated static method


"""
Тези характеристики правят статичните методи подходящи за случаи, 
    когато трябва да се дефинират функции вътре в клас, 
    които не зависят от състоянието на инстанцията или класа.
"""