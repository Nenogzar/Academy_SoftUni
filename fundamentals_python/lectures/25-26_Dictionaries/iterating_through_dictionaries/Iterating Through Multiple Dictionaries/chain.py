""" The itertools module provides the chain() function,
    which can take multiple iterable objects as arguments and
    make an iterator that yields elements from all of them.
    To do its job, chain() starts yielding items from the first iterable until exhaustion,
    then the function yields items from the next iterable,
    and so on until all the input iterable objects are exhausted."""

from itertools import chain

for_adoption = {"dogs": 10, "cats": 7, "pythons": 3}
vet_treatment = {"dogs": 4, "cats": 3, "turtles": 1}
pets = chain(for_adoption.items(), vet_treatment.items())


for pet, count in pets:
    print(pet, "->", count)
    # dogs -> 10
    # cats -> 7
    # pythons -> 3
    # dogs -> 4
    # cats -> 3
    # turtles -> 1


""" Note that unlike ChainMap, 
    the chain() function gives you access to all the keys from your input dictionaries, 
    even the duplicated ones."""