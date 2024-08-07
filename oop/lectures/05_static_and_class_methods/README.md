<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>

<body style="background-color: #0d1117; color: white; align-items: center; height: 100vh; margin: 0;">

<a href="https://github.com/Nenogzar/Academy_SoftUni/tree/main/oop">Back to Python OOP</a>

|№|<a href="https://github.com/Nenogzar/Academy_SoftUni/tree/main/oop/lectures/05_static_and_class_methods/lab">Lab</a>|<a href="https://github.com/Nenogzar/Academy_SoftUni/tree/main/oop/lectures/05_static_and_class_methods/exercise">Exercise</a>|
|-|-|-|
|1|<a href="https://github.com/Nenogzar/Academy_SoftUni/blob/main/oop/lectures/05_static_and_class_methods/lab/1_calculator.py">Calculator</a>|<a href="https://github.com/Nenogzar/Academy_SoftUni/blob/main/oop/lectures/05_static_and_class_methods/exercise/01_photo_album.py">Photo Album </a>| 
|2|<a href="https://github.com/Nenogzar/Academy_SoftUni/blob/main/oop/lectures/05_static_and_class_methods/lab/2_shop.py">Shop</a>|<a href="https://github.com/Nenogzar/Academy_SoftUni/blob/main/oop/lectures/05_static_and_class_methods/exercise/02_movie_world/02_movie_world.py">Movie World</a>|
|3|<a href="https://github.com/Nenogzar/Academy_SoftUni/blob/main/oop/lectures/05_static_and_class_methods/lab/3_integer.py">Integer</a>|<a href="https://github.com/Nenogzar/Academy_SoftUni/blob/main/oop/lectures/05_static_and_class_methods/exercise/03_document_management/03_document_management.py">Document Management</a>|
|4|<a href="https://github.com/Nenogzar/Academy_SoftUni/blob/main/oop/lectures/05_static_and_class_methods/lab/4_hotel_rooms.py">Hotel rooms</a>|<a href="https://github.com/Nenogzar/Academy_SoftUni/blob/main/oop/lectures/05_static_and_class_methods/exercise/04_gym/04_gym.py">Gym</a>|



> # ClassMethod

1. Дефиниция:

Класовите методи са функции, дефинирани вътре в клас, които имат достъп до самия клас и неговите атрибути.
Приемат cls като първи параметър, който представлява самия клас.

2. Декорация:

Декларират се с декоратора @classmethod преди дефиницията на метода.

```py
class MyClass:
    @classmethod
    def class_method(cls):
        pass
```

3. Достъп до класови атрибути:
Чрез cls методът има достъп до атрибутите и другите методи на класа.


```py
class MyClass:
    class_attribute = "class attribute"

    @classmethod
    def class_method(cls):
        return cls.class_attribute
```

4. Извикване:
Могат да се извикват както чрез инстанции на класа, така и директно чрез самия клас.

```py

# Извикване чрез класа
print(MyClass.class_method())  # class attribute

# Извикване чрез инстанция на класа
instance = MyClass()
print(instance.class_method())  # class attribute

```

5. Употреба:
Използват се за операции, които са свързани с класа и изискват достъп до класови атрибути или методи.
Подходящи са за създаване на фабрични методи, които създават нови инстанции на класа.


```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2024 - birth_year
        return cls(name, age)


person = Person.from_birth_year("Alice", 1990)
print(person.name, person.age)  # Alice 34
```

6. Модификация на класови атрибути:
Могат да променят атрибутите на класа чрез cls.

```py
class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1


Counter.increment()
print(Counter.count)  # 1
```


7. Използване на други методи на класа:
Могат да извикват други методи на класа чрез cls.

```py
class Circle:
    pi = 3.14

    @classmethod
    def area(cls, radius):
        return cls.pi * radius ** 2

    @classmethod
    def perimeter(cls, radius):
        return 2 * cls.pi * radius
```

8. Съвместимост със субкласове:
Когато се наследяват, класовите методи работят правилно със субкласовете, като използват коректния клас чрез cls.

```py
class Animal:
    @classmethod
    def create(cls):
        return cls()

class Dog(Animal):
    pass

dog = Dog.create()
print(isinstance(dog, Dog))  # True
```

Тези характеристики правят класовите методи полезни за операции, 
които са свързани с класа като цяло, а не с конкретни инстанции на класа.
</body>
