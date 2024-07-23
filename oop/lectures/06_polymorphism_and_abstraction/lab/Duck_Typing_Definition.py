"""Duck Typing е концепция в Python и други динамични програмни езици,
    която се основава на идеята, че
        типът или класът на обект не е важен за определена операция,
            стига обектът да поддържа необходимите методи и свойства.

Името "Duck Typing" идва от израза:
"If it looks like a duck,
    swims like a duck,
        and quacks like a duck,
    then it probably is a duck"
    (Ако изглежда като патица, плува като патица и квака като патица,
        огава вероятно е патица).
    В контекста на програмирането това означава,
        че ако даден обект има необходимите методи и поведение,
            може да се третира като определен тип,
                независимо от неговата действителна класа.


"""
class Duck:
    def quack(self):
        print("Quack")

    def swim(self):
        print("Swim")


class Person:
    def quack(self):
        print("I'm quacking like a duck")

    def swim(self):
        print("I'm swimming like a duck")


def in_the_pond(duck):
    duck.quack()
    duck.swim()


# Тук използваме функцията in_the_pond с обекти от различни класове,
# които имат необходимите методи quack и swim.
duck = Duck()
person = Person()

in_the_pond(duck)   # Quack, Swim
in_the_pond(person) # I'm quacking like a duck, I'm swimming like a duck
