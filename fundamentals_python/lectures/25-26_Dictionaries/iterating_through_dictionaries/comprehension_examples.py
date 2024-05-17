categories = ["color", "fruit", "pet"]
objects = ["blue", "apple", "dog"]

likes = {key: value for key, value in zip(categories, objects)}
print(likes) # {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

""" or """
likes1 = dict(zip(categories, objects))
print(likes1) # {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

###################################################################
numbers = {"one": 1, "two": 2, "three": 3, "four": 4}

small_dict = {key: value for key, value in numbers.items() if value <= 2}
print(small_dict) # {'one': 1, 'two': 2}

""" Sorting a Dictionary """

incomes = {"apple": 5600.00, "orange": 3500.00, "banana": 5000.00}

sort_incomes={fruit: incomes[fruit] for fruit in sorted(incomes)}
print(sort_incomes)  # {'apple': 5600.0, 'banana': 5000.0, 'orange': 3500.0}