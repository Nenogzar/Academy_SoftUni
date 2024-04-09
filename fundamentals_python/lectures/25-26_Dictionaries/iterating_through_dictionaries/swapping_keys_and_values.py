numbers = {"one": 1, "two": 2, "three": 3, "four": 4}
swapped = {}

for key, value in numbers.items():
    swapped[value] = key

print(swapped) # {1: 'one', 2: 'two', 3: 'three', 4: 'four'}

##########################################################################
new_swapped_dict = dict(zip(numbers.values(), numbers.keys()))

print(new_swapped_dict) # {1: 'one', 2: 'two', 3: 'three', 4: 'four'}

##########################################################################
new_swapped_dict1 = {value: key for key, value in numbers.items()}

print(new_swapped_dict1) # {1: 'one', 2: 'two', 3: 'three', 4: 'four'}

##########################################################################