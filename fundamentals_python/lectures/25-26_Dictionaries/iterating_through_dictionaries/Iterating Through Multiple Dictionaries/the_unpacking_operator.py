""" This feature allows you to iterate through multiple dictionaries in one go: """

fruits = {"apple": 0.40, "orange": 0.35}
vegetables = {"pepper": 0.20, "onion": 0.55}

for product, price in {**fruits, **vegetables}.items():
    print(product, "->", price)
    # apple -> 0.4
    # orange -> 0.35
    # pepper -> 0.2
    # onion -> 0.55

""" It’s important to note that if the dictionaries that you’re merging have repeated or duplicate keys, 
    then the values of the rightmost dictionary will prevail"""

for_adoption = {"dogs": 10, "cats": 7, "pythons": 3}
vet_treatment = {"dogs": 4, "cats": 3, "turtles": 1}

for pet, count in {**for_adoption, **vet_treatment}.items():
    print(pet, "->", count)
    # dogs -> 4
    # cats -> 3
    # pythons -> 3
    # turtles -> 1