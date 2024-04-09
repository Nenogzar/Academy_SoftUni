numbers = {"one": 1, "two": 2, "three": 3, "four": 4}

small_numbers = {}

for key, value in numbers.items():
    if value <= 2:
        small_numbers[key] = value

print(small_numbers) # {'one': 1, 'two': 2}

########################################################
fruits = {"apple": 1, "orange": 2, "banana": 3}
non_citrus = {}

for key in fruits.keys() - {"orange"}:
    non_citrus[key] = fruits[key]

print(non_citrus) # {'apple': 1, 'banana': 3}

########################################################

new_fruits = {key: value for key, value in fruits.items() if value <= 2}

print(new_fruits) # {'apple': 1, 'orange': 2}


