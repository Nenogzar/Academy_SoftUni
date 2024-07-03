# ******* First Steps in OOP - Exercise ******* #

# *******  02_hero  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Compete/Index/1935


Create a class called Hero. Upon initialization, it should receive a name (string) and health (number). Create two additional methods:
•	defend(damage) - reduce the given damage from the hero's health:
    o   	if the health becomes 0 or less, set it to 0 and return "{name} was defeated"
•	heal(amount) - increase the health of the hero with the given amount
Examples


Test Code:

hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))

Output:

None
None
Peter was defeated


"""


##########: variant 1 :##########

class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def defend(self, damage):
        current_health = self.health - damage
        if current_health <= 0:
            self.health = 0
            return f"{self.name} was defeated"
        else:
            self.health = current_health
            return None

    def heal(self, amount):
        self.health += amount


hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))
##########: variant 2 :##########


##########: variant 3 solution SoftUni :##########
