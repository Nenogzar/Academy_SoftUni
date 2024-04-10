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


""" Filtering Items in a Dictionary: filter() """

fruits = {"apple": 0.40, "orange": 0.35, "banana": 0.25}

def has_low_price(item, price=0.4):
    return item[1] < price


filtered_dict = dict(filter(has_low_price, fruits.items()))
print(filtered_dict)