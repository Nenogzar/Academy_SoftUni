lst = [1, 2, 3, 4, 5, 9, 6]

# max and min
max_number = max(lst)
min_number = min(lst)
print(f" In list {lst} the max nomber is: {max_number} and the min number is: {min_number}")
sum_number = sum(lst)
print(f"{sum_number = }")

# list comprehension
squarred_number = [x**2 for x in lst]
print(f"{squarred_number = }")

# list Filter

even_numbers = list(filter(lambda x: x % 2 ==0, lst))
print(f"{even_numbers = }")

# map function

double_number = list(map(lambda  x: x * 2, lst))
print(f"{double_number = }")

# Check is All elements in a List are True

all_true = all(lst)
print("yes" if all_true else "no")

# Count occurrences of an Emenet in a List
element = 2
count_element = lst.count(element)
print(f"{count_element = }")

# STRING
# reverse a string

me_str = "Clouding"
reversed_str = me_str[::-1]
print(f"{reversed_str = }")

# read a file into a list of lines
lines = [line.strip() for line in open('file.txt')]
print(lines)