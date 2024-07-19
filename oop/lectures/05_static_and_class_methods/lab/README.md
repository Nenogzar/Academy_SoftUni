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

    def change_name(self, new_name):
        self.name = new_name

    @staticmethod
    def is_adult(age):
        return age >= 18

person = Person("Name")
print(person.name)        # Name
person.change_name("New name")
print(person.name)        # Ne name
print(person.is_adult(20))    # True
print(person.is_adult(17))    # False

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
whi can add more ingredients to pizza:
```py
     @classmethod
        def quattro_formaggi(cls, additional_ingredients = []):
            all_ingredient = ["mozzarella", "gorgonzola", "fontina", "parmigiano"] + additional_ingredients
            return cls(all_ingredient)

first_pizza = Pizza.pepperoni()
second_pizza = Pizza.quattro_formaggi(["banana"])


print(second_pizza.ingredients)
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
```py
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
```

### Problem:👈 Integer

▪ Follow the instructions in the lab document and create a class called Integer with the following methods

▪ from_float(value)

▪ from_roman(value)

▪ from_string(value)

Skeleton: Integer

```py
class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        pass

    @classmethod
    def from_roman(cls, value):
        pass

    @classmethod
    def from_string(cls, value):
        pass

```


> # Overriding Using Class Methods



```py
class Person:
    min_age = 0
    max_age = 150

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def __validate_age(value):
        if value < Person.min_age or \
        value > Person.max_age:
        raise ValueError()

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value
```

```py
class Employee(Person):
    min_age = 16
    max_age = 150
    def __init__(self, name, age):
    self.name = name
    self.age = age

@staticmethod
def __validate_age(value):
    if value < Employee.min_age or \
    value > Employee.max_age:
    raise ValueError()

@property
def age(self):
    return self.__age

@age.setter
def age(self, value):
    self.__validate_age(value)
    self.__age = value

```

> ▪ If the methods do not rely on state and they are the same, they could be optimized using @classmethod

```py
class Person:
    min_age = 0
    max_age = 150

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def __validate_age(cls, value):
        raise ValueError(f'{value} must be between '
                        f'{cls.min_age} and {cls.max_age}')
# __validate_age() takes the class attributes of class Person


    @property
        def age(self):
        return self.__age
    @age.setter
        def age(self, value):
        self.__validate_age(value)
        self.__age = value

class Employee(Person):
    min_age = 16
    # __validate_age() takes the class attribute min_age of class Employee

    def __init__(self, name, age, salary):
        super().__init__(name, age) # when checking the age of the Employee
        self.salary = salary
```


> ### Summary

> ▪ A static method is a method that knows nothing about the class or instance it is called on

> ▪ A class method, on the other hand, is bound to the class and not the object of the class

</body>
