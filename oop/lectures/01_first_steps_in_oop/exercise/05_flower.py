# ******* First Steps in OOP - Exercise ******* #

# *******  05_flower  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Compete/Index/1935https://judge.softuni.org/Contests/Compete/Index/1935


Create a class called Flower. Upon initialization,
    the class should receive a name (string) and a water_requirements (number).

    The flower should also have an instance attribute called is_happy (False by default).

    Add two additional methods to the class:
-	water(quantity)
    - it will water the flower. Each time check if the quantity is greater than or equal to the required.
        If it is - the flower becomes happy (set is_happy to True).

-	status()
    - it should return "{name} is happy" if the flower is happy,
        otherwise it should return
        "{name} is not happy"

Submit only the class in the judge system.

Examples

Test Code:

flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())

Output:

Lilly is not happy
Lilly is not happy
Lilly is happy



"""


##########: variant 1 :##########


class Flower:
    def __init__(self, name: str, water: int, is_happy=False):
        self.name = name
        self.water_requirements = water
        self.is_happy = is_happy

    def water(self, quantity):
        if quantity >= self.water_requirements:
            self.is_happy = True

    def status(self):
        return (f"{self.name} is happy") if self.is_happy else (f"{self.name} is not happy")
        # OR 
        # return f"{self.name} is {'' if self.is_happy else 'not '}happy"
        # OR 
        # if self.is_happy:
        #     return f"{self.name} is happy"
        #
        # return f"{self.name} is not happy"


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())

##########: variant 2 :##########

class Flower:
    def __init__(self, name,water_requirements):
        self.name = name
        self.water_requirements = int(water_requirements)
        self.is_happy = False

    def water(self, quantity):
        if quantity >= self.water_requirements:
            self.is_happy = True

    def status(self):
        if self.is_happy:
            return f"{self.name} is happy"
        return f"{self.name} is not happy"





"""
Как е по правилно да се иницилизира:

 def __init__(self, name: str, water: int, is_happy=False):
        self.name = name
        self.water_requirements = water
        self.is_happy = is_happy

или  :

def __init__(self, name,water_requirements):
        self.name = name
        self.water_requirements = int(water_requirements)
        self.is_happy = False


питам за self.is_happy


Изборът между двете варианта зависи от това какво искате да бъде стойността на is_happy, 
    когато не е зададена при инициализация на обекта.

1. Вариант с подразбираща се стойност в аргумента на метода __init__:

def __init__(self, name: str, water: int, is_happy=False):
    self.name = name
    self.water_requirements = water
    self.is_happy = is_happy



В този случай, ако при създаването на обект не се предостави стойност за is_happy, 
    то тя автоматично ще бъде зададена на False.


2. Вариант с фиксирано зададена стойност:

def __init__(self, name, water_requirements):
    self.name = name
    self.water_requirements = int(water_requirements)
    self.is_happy = False
    
Тук is_happy винаги ще бъде зададена на False, 
дори и ако при създаването на обект бъде подадена друга стойност за is_happy.


Кой вариант да избера?
    
Ако искате гъвкавост и да може потребителите на вашия клас да решат дали искат да предоставят стойност за is_happy 
при инициализацията, използвайте първия вариант с подразбираща се стойност. 
Това позволява на потребителите на вашия код да използват класа с различни конфигурации, 
включително и без задаване на is_happy.

Ако искате ясна и предвидима стойност за is_happy и не предвиждате различни сценарии без нея, 
може да използвате втория вариант с фиксирано зададена стойност False. 
Това прави вашия код по-прозрачен и предсказуем, но ще ограничи гъвкавостта при използване на класа.

Заключение
И двата варианта са валидни и зависят от специфичните нужди и предпочитания на вашето приложение. 

Ако вие или потребителите на вашия код биха могли да се възползват от гъвкавостта на подразбиращата се стойност 
за is_happy, използвайте първия вариант. 

Ако предпочитате по-ясна и предвидима логика за инициализацията, изберете втория вариант.






"""
