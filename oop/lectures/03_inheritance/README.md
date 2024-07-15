<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>

<body style="background-color: #0d1117; color: white; align-items: center; height: 100vh; margin: 0;">


## <a href="https://github.com/Nenogzar/Academy_SoftUni/tree/main/oop">Back to Python OOP</a>
</body>


> inheritance

Наследяването (Inheritance) е една от основните концепции в Обектно-ориентираното програмиране (OOP). Тя позволява създаването на нови класове, които наследяват свойства и методи от вече съществуващи класове. Това помага за повторната употреба на код, намаляване на дублирането и подобряване на организацията на кода. 

### Основни концепции на наследяването
1. Базов клас (Base class): Това е класът, от който се наследяват свойства и методи. Нарича се още супер клас (superclass) или родителски клас (parent class).
2. Производен клас (Derived class): Това е класът, който наследява свойствата и методите от базовия клас. Нарича се още подклас (subclass) или дъщерен клас (child class).

Пример:

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


```

Използването на наследяване в Python трябва да се основава на ясни йерархии и нуждата от повторна употреба на код. Важно е да следвате принципите на доброто проектиране, като принципа на единната отговорност и принципа на подмяна на Лисков, за да създадете устойчиви и добре организирани системи.
