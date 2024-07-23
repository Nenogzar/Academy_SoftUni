# ******* Polymorphism and Abstraction - Lab ******* #

# *******  03_playing  ******* #

# *******  TASK CONDITION  ******* #
"""
https://judge.softuni.org/Contests/Practice/Index/1942
Create a function called start_playing which will receive an instance and will return its play() method.

Submit only the start_playing function in the judge system
"""


##########: SOLUTION :##########

class Guitar:
    def play(self):
        return "Playing the guitar"


class Children:
    def play(self):
        return "Children are playing"


def start_playing(player):
    return player.play()


guitar = Guitar()
print(start_playing(guitar))

children = Children()
print(start_playing(children))

