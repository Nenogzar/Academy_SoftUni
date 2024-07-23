from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 2:
            raise ValueError("The len of name must be more 2 char")
        self.__name = value

    @abstractmethod
    def go_to_work(self):
        pass

    # @abstractmethod
    # def eat(self):
    #     pass

    def info(self):
        return self.go_to_work(), self.name


class Student(Person):

    def go_to_work(self):
        return "Go to the Library"

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value[0] != "a":
            raise ValueError("The name must be start whit \"a\" ")
        self.__name = value

class Actor(Person):

    def go_to_work(self):
        return "Go to the theater"


class Miner(Person):

    def go_to_work(self):
        return "Go to mine"


m = Miner("Pesho")
print(", ".join(el for el in m.info()))

st = Student("angel")
print(", ".join(el for el in st.info()))

""" 
Всеки клас който наследява класа е длъжен да има определен метод!
Абстрактния клас никога не може да създава обекти от самия себаси!!!
ТОЕСТ Абстрактния КЛАС трябва да наследява ABC:
    from abc import ABC, abstractmethod 
        и да има поне един абстрактен метод
Той служи като шаблон за това какво трябва да правят другите методи!!!

Всеки един клас който наследява абстрактния КЛАС 
    е длъжен да имплементира абстрактния метод
Това означава че насилваме полиморфизма в наследниците.
Абстрактния метод няма никаква имплементация - pass

"""
