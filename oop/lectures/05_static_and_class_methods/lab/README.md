<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>

<body style="background-color: #0d1117; color: white; align-items: center; height: 100vh; margin: 0;">

    
|<a href="https://github.com/Nenogzar/Academy_SoftUni/tree/main/oop">Back to Python OOP</a>|<a href="https://github.com/Nenogzar/Academy_SoftUni/tree/main/oop/lectures/05_static_and_class_methods/lab">Lab</a>|<a href="https://github.com/Nenogzar/Academy_SoftUni/tree/main/oop/lectures/05_static_and_class_methods/exercise">Exercise</a>|
|-|-|-|


> # Class and Static Methods

1. Methods and Decorators
2. Static Methods
3. Class Methods

> ### Static Methods

> ▪ It knows nothing about the class or instance it is called on

> ▪ It cannot modify object state or class state

> ▪ It could be put outside the class, but it is inside the class where it is applicable

> ▪ To turn a method into a static, we add a line with @staticmethod in front of the method header 

### Example: 👈 Static Methods

To call a static method, we could use both the instance or the class


```py
class Person:
    def __init__(self, name):
        self.name = name

    @staticmethod        
        def is_adult(age):    # It does not take a self parameter
        return age >= 18

print(Person.is_adult(5)) # False
girl = Person("Amy")
print(girl.is_adult(20)) # True

```

### Benefits

> ▪ Shows that a particular method is independent of everything else around it
> 
> ▪ Often helps to avoid accidental modifications that go against the original design
> 
> ▪ Communicates and enforces developer intent about the class design
> 
> ▪ It is much easier to test since it is completely independent from the rest of the class

### Problem: 👈 Calculator

> ▪ Follow the instructions in the lab document and create a class called Calculator with the following static methods

> ▪ add(*args)

> ▪ multiply(*args)

> ▪ divide(*args)

> ▪ subtract(*args)


Skeleton: Calculator

```py
class Calculator:
    @staticmethod
        def add(*args):
        pass

    @staticmethod
        def multiply(*args):
        pass

    @staticmethod
        def divide(*args):
        pass

    @staticmethod
        def subtract(*args):
        pass
```

> # Class Methods

> ▪ It is bound to the class and not the object of the class
> 
> ▪ It can modify a class state that would apply across all the instances of the class
> 
> ▪ To turn a method into a class method, we add a line with @classmethod in front of the method header

### Example:👈 Class Methods

▪ We generally use class method to create factory methods

```py
class Pizza:
    def __init__(self, ingredients):
    self.ingredients = ingredients
                                    # We could create different pizzas easily
    @classmethod                
    def pepperoni(cls):
        return cls(["tomato sauce", "parmesan", "pepperoni"])

    @classmethod
    def quattro_formaggi(cls):
        return cls(["mozzarella", "gorgonzola", "fontina", "parmigiano"])

first_pizza = Pizza.peperoni()
second_pizza = Pizza.quattro_formaggi()
```

### Benefits

> ▪ Simply provide a shortcut for creating new instance objects
> ▪ Ensures correct instance creation of the derived class
> ▪ You could easily follow the Don't Repeat Yourself (DRY) principle using class methods


### Problem:👈 Shop

▪ Follow the instructions in the lab document and create a class called Shop with the following methods

    ▪ small_shop(name: str, type: str)
    
    ▪ add_item(item_name: str)
    
    ▪ remove_item(item_name: str, amount: int)
    
    ▪ __repr__()

Skeleton: Shop

class Shop:
    def __init__(self, name, type, capacity):
        pass
        
    @classmethod
        def small_shop(cls, name, type):
        pass
        
    def add_item(self, item_name):
        pass
    
    def remove_item(self, item_name, count):
        pass
    
    def __repr__(self):
        pass
</body>
