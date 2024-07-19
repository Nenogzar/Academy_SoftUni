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


> Class and Static Methods

1. Methods and Decorators
2. Static Methods
3. Class Methods

> ### Static Methods

▪ It knows nothing about the class or instance it is called on

▪ It cannot modify object state or class state

▪ It could be put outside the class, but it is inside the class where it is applicable

▪ To turn a method into a static, we add a line with @staticmethod in front of the method header 

Example: Static Methods

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
> ▪ Often helps to avoid accidental modifications that go against the original design
> ▪ Communicates and enforces developer intent about the class design
> ▪ It is much easier to test since it is completely independent from the rest of the class




</body>
