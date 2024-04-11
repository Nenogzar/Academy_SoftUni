""" The collections module from the standard library provides
    a specialized container type called ChainMap.
    It’s a dictionary-like class that you can use to create a single,
    updateable view out of multiple existing dictionaries.
    The resulting object will logically appear and behave as a single dictionary."""

from collections import ChainMap

fruits = {"apple": 0.40, "orange": 0.35}
vegetables = {"pepper": 0.20, "onion": 0.55}

catalog = ChainMap(fruits, vegetables)
print(catalog)
# ChainMap({'apple': 0.4, 'orange': 0.35}, {'pepper': 0.2, 'onion': 0.55})

for product, price in catalog.items():
    print(product, "->", price)
    # pepper -> 0.2
    # onion -> 0.55
    # apple -> 0.4
    # orange -> 0.35

""" When using ChainMap to iterate over multiple dictionaries in one go, 
    you must keep in mind that if you have duplicate keys, 
    then you’ll only be able to access the first instance of them. """

from collections import ChainMap

for_adoption = {"dogs": 10, "cats": 7, "pythons": 3}
vet_treatment = {"dogs": 4, "cats": 3, "turtles": 1}
pets = ChainMap(for_adoption, vet_treatment)

for pet, count in pets.items():
    print(pet, "=>", count)
    # dogs => 10
    # cats => 7
    # turtles => 1
    # pythons => 3
