<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>

<body style="background-color: #0d1117; color: white; align-items: center; height: 100vh; margin: 0;">


|<a href="https://github.com/Nenogzar/Academy_SoftUni/tree/main/oop">Back to Python OOP</a>|<a href="https://github.com/Nenogzar/Academy_SoftUni/tree/main/oop/lectures/03_inheritance/lab">Lecture</a>|<a href="https://github.com/Nenogzar/Academy_SoftUni/tree/main/oop/lectures/03_inheritance/exercise">Exercise</a>|
|-|-|-|


> inheritance

Наследяването (Inheritance) е една от основните концепции в Обектно-ориентираното програмиране (OOP). Тя позволява създаването на нови класове, които наследяват свойства и методи от вече съществуващи класове. Това помага за повторната употреба на код, намаляване на дублирането и подобряване на организацията на кода. 

### Основни концепции на наследяването
1. Базов клас (Base class): Това е класът, от който се наследяват свойства и методи. Нарича се още супер клас (superclass) или родителски клас (parent class).
2. Производен клас (Derived class): Това е класът, който наследява свойствата и методите от базовия клас. Нарича се още подклас (subclass) или дъщерен клас (child class).



Използването на наследяване в Python трябва да се основава на ясни йерархии и нуждата от повторна употреба на код. Важно е да следвате принципите на доброто проектиране, като принципа на единната отговорност и принципа на подмяна на Лисков, за да създадете устойчиви и добре организирани системи.

1. В Python наследяването се постига чрез дефиниране на нови класове, които наследяват съществуващи.

Ето един основен пример за наследяване в Python:

```py


# Базов клас (родителски клас)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


# Подклас (наследник)
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


# Друг подклас (наследник)
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


# Създаваме обекти от подкласовете
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Използваме методите на подкласовете
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!

```

В този пример:
Animal е базовият клас.
Dog и Cat са подкласове, които наследяват от Animal.
Методът speak е дефиниран в базовия клас, но е презаписан (overridden) в подкласовете.


2. Разширяване на функционалността
Можете също така да добавяте нови методи и атрибути в подкласовете:

```py
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{self.name} says Woof!"

    def fetch(self):
        return f"{self.name} is fetching the ball!"


dog = Dog("Buddy", "Golden Retriever")
print(dog.speak())  # Output: Buddy says Woof!
print(dog.fetch())  # Output: Buddy is fetching the ball!
```



Тук използваме функцията super() за да извикаме __init__ метода на базовия клас и да инициализираме атрибута name.

3. Полиморфизъм
Полиморфизмът е друга важна концепция в OOP, която позволява на методите да работят с обекти от различни класове, 
стига тези класове да имат този метод:
```py

animals = [Dog("Buddy", "Golden Retriever"), Cat("Whiskers")]

for animal in animals:
    print(animal.speak())

# Buddy says Woof!
# Whiskers says Meow!

```


4. Наследяване на няколко класа (Multiple Inheritance)
Python поддържа и наследяване от няколко базови класа. Това е малко по-сложно, но ето един основен пример:
```py
class Walker:
    def walk(self):
        return "Walking"


class Swimmer:
    def swim(self):
        return "Swimming"


class Amphibian(Walker, Swimmer):
    pass


frog = Amphibian()
print(frog.walk())  # Walking
print(frog.swim())  # Swimming

```
В този пример, Amphibian класът наследява методите и на Walker, и на Swimmer.

Наследяването в Python е мощен инструмент за повторна употреба на код и организиране на обекти в йерархии. 
Основните концепции включват базови класове, подкласове, полиморфизъм и, ако е необходимо, множествено наследяване.


Няколко условия и принципи, които трябва да имате предвид при използването на наследяване:

1. Йерархия и абстракция
    Йерархична структура: 
        Наследяването е подходящо, когато има ясно изразена йерархична структура. 
        Например, когато имате общ базов клас и няколко специфични подкласове, 
            които добавят или променят функционалността.
            
    Абстрактни концепции: 
        Използвайте наследяване, за да създадете абстрактни базови класове, 
        които дефинират общи интерфейси и поведения, които могат да бъдат споделени между подкласовете.
        
2. Повторна употреба на код
    Повторна употреба на код: 
        Ако имате код, който се повтаря в няколко класа, 
        можете да го поставите в базов клас и да го наследите, 
        за да избегнете дублиране на код.
        
3. Принципи на добрата проектика

    Принцип на единната отговорност: 
    Всеки клас трябва да има единствена отговорност. 
    Избягвайте да създавате класове, които имат множество несвързани функционалности.
    
    Принцип на отвореност и затвореност: 
        Класовете трябва да бъдат отворени за разширяване, но затворени за модификация. 
        Това означава, че трябва да можете да добавяте нова функционалност чрез наследяване и полиморфизъм, 
        без да променяте съществуващия код.
        
    Принцип на подмяна на Лисков: 
        Подкласовете трябва да могат да заместят базовия клас, 
        без да нарушават функционалността на програмата. 
        Това означава, че подкласовете трябва да спазват условията, зададени от базовия клас.
        
4. Подходящо използване на super()

    Използване на super(): 
        Когато презаписвате методи в подкласовете, 
        използвайте функцията super() за да извикате методите на базовия клас, ако е необходимо. 
        Това осигурява правилна инициализация и поведение.
        
5. Избягвайте множественото наследяване, ако е възможно

    Множествено наследяване: 
        Множественото наследяване може да доведе до сложно и труднo за проследяване зависимости. 
        Използвайте го внимателно и обмислено, като предпочитате композиция пред наследяване, когато е възможно.
        
Пример:
Ето един пример, който показва правилното използване на наследяване:


```py
# Базов клас
class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass


# Подкласове
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Създаване на обекти и използване на полиморфизъм
shapes = [Circle("Red", 5), Rectangle("Blue", 3, 4)]

for shape in shapes:
    print(f"A {shape.color} shape with area: {shape.area()}")

# A Red shape with area: 78.5
# A Blue shape with area: 12

```
Използването на наследяване в Python трябва да се основава на ясни йерархии и нуждата от повторна употреба на код. 
Важно е да следвате принципите на добрата практика, 
като принципа на единната отговорност и принципа на подмяна на Лисков, 
за да създадете устойчиви и добре организирани системи.



</body>

