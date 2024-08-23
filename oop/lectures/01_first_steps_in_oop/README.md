<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>

<body style="background-color: #0d1117; color: white; align-items: center; height: 100vh; margin: 0;">

Object-Oriented Programming (OOP) is a fundamental concept in software development that revolves around the concept of classes and objects.

Learning OOP helps us create efficient, modular, and maintainable code.

In this article, we will explore core OOP concepts using easy to understand code examples.
<div id="badges" align="center">
<img src="https://github.com/Nenogzar/Academy_SoftUni/blob/main/oop/image/oop.jpg" alt="Nenogzar_Python" height="450"  >
</div>


<details> <summary>1. Classes and Objects</summary>
    
> A class is a blueprint or template that defines the properties and behavior of an object. An Object is an instances of a class, created using the class definition.

Here's an example of a class definition in Python:
```py
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


    def start_engine(self):
        print(f"The {self.make} {self.model}'s engine is starting")
```

In this example, the Car class is a blueprint that defines the properties of a car.

```py
toyota_car = Car("Toyota", "Camry", 2022)
toyota_car.start_engine()

chevrolet_car = Car("Chevrolet", "Tahoe", 2023)
chevrolet_car.start_engine()
```
We create two objects, toyota_car and chevrolet_car which are instances of the Car class. Both car objects can invoke start_engine() method using their own values for the make, model and year properties.


</details>  
<details> <summary>2. Encapsulation</summary>

> Encapsulation is the concept of hiding the implementation details of an object from the outside world and only exposing the necessary information through public methods.

Encapsulation helps protect the object's internal state from external interference and misuse.

In Python, you can achieve encapsulation using private attributes and methods, denoted by a double underscore prefix (__).


```py
class BankAccount:
    def __init__(self, account_id, balance):
        self.__acount_id = account_id
        self.__balance = balance
        
    def deposit(self, amount):
        self.__balance += amount
        
    def withdrow(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        print("Insufficient funds")
        
    def get_balance(self):
        return self.__balance
```

In this example, the __account_number and __balance attributes are private, meaning it can't be accessed directly from outside the class. We interact with it through the deposit, withdraw, and get_balance methods.

</details>  
<details> <summary>3. Inheritance</summary>
    
> Inheritance is a mechanism that allows a class to inherit properties and methods from another class, called the superclass or parent class.

The class that inherits is called the subclass or child class.

The child class inherits all the fields and methods of the parent class and can also add new fields and methods or override the ones inherited from the parent class.

Inheritance promotes code reuse and helps create a hierarchical structure.

Let’s say we have a parent Vehicle class with a method named honk().

```py
# Devine a parent class called "Vehicle"
class Vehicle:
    def __init__(self, color):
        self.color = color

    def cyty(self):
        print("Sofia")


# Define a child class called "Car" that inherits from Vehicle
class Car(Vehicle):
    def __init__(self, color, speed):
        super().__init__(color)
        self.speed = speed

    def acceleration(self):
        self.speed += 10


# create an object /instance/ of the Car class

my_car = Car("blue", 60)
my_car.cyty()  # Output: Sofia
```

The Car class inherits the color attribute and the honk method from the Vehicle class promoting code reuse. The Car class also adds its own attributes and methods, such as speed and accelerate.

</details>  
<details> <summary>4. Polymorphism</summary>
    
>Polymorphism is the ability of an object to take on multiple forms.

It enables you to write generic code that can work with objects of multiple types, as long as they share a common interface.

A common way to achieve polymorphism is method overriding.

Method overriding is when a subclass provides a specific implementation of a method that is already defined in its parent class.

For example, let’s say we have an interface Document which defines a method show().


```py
class Document:
    def show(self):
        raise NotImplementedError("Sublass nust implement abstract method")

class Pdf(Document):
    def show(self):
        return "Show PDF content"

class Word(Document):
    def show(self):
        return "Show Word content"


try:
    doc = [Pdf(), Word(), Document()]
    for d in doc:
        print(d.show())
except NotImplementedError as e:
    print(e)

# OUTPUT:
# Show PDF content
# Show Word content
# Sublass nust implement abstract method
```

Each subclass (Pdf, Word) of Document implement the show method differently (method overriding), but the interface remains consistent giving the ability to iterate over both the classes using a single for loop.

</details>  
<details> <summary>5. Abstraction</summary>

> Abstraction is the concept of showing only the necessary information to the outside world while hiding unnecessary details.

Abstraction helps to simplify complex systems and focus on the essential features.
In Python, you can achieve abstraction using abstract base classes (ABC) and abstract methods.
Let’s say we have an abstract base class called Shape. The Shape class is marked as an abstract class by inheriting from the ABC class (Abstract Base Class).
Inside the Shape class, we define an abstract method called area() using the @abstractmethod decorator.

```py
from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, heigh):
        self.width = width
        self.heigh = heigh

    def area(self):
        return self.width * self.heigh

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius** 2
```

The Rectangle and Circle classes inherit from the Shape class.

They provide their own implementations of the area() method specific to their shapes. Note that the implementation details are hidden from the outside world, and only the interface defined by the abstract class is exposed.


</details> 




## <a href="https://github.com/Nenogzar/Academy_SoftUni/tree/main/oop">Back to Python OOP</a>
</body>
