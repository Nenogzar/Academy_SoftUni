""" Iterating Over Sorted Keys """

incomes = {"apple": 5600.00, "orange": 3500.00, "banana": 5000.00}

for fruit in sorted(incomes):
    print(fruit, "->", incomes[fruit])
    #   apple -> 5600.0
    #   banana -> 5000.0
    #   orange -> 3500.0

""" Looping Through Sorted Values """
for fruit, income in sorted(incomes.items(), key=lambda item: item[1]):
    print(fruit, "->", income)
    #   orange -> 3500.0
    #   banana -> 5000.0
    #   apple -> 5600.0
""" sorted order without considering the keys """
for income in sorted(incomes.values()):
    print(income)
    # 3500.0
    # 5000.0
    # 5600.0

""" Sorting a Dictionary With a Comprehension"""

incomes = {"apple": 5600.00, "orange": 3500.00, "banana": 5000.00}

sort_key={fruit: incomes[fruit] for fruit in sorted(incomes)}
print(sort_key)  # {'apple': 5600.0, 'banana': 5000.0, 'orange': 3500.0}


sort_value = {
    fruit: income
    for fruit, income in
    sorted(incomes.items(), key=lambda item: item[1])
}
print(sort_value) #{'orange': 3500.0, 'banana': 5000.0, 'apple': 5600.0}

""" Iterating Through a Dictionary in Reverse-Sorted Order """
for fruit in sorted(incomes, reverse=True):
    print(fruit, "->", incomes[fruit])
    # orange -> 3500.0
    # banana -> 5000.0
    # apple -> 5600.0

""" Traversing a Dictionary in Reverse Order """
numbers = {"one": 1, "two": 2, "three": 3, "four": 4}

for key, value in reversed(numbers.items()):
    print(key, "->", value)
    # four -> 4
    # three -> 3
    # two -> 2
    # one -> 1

