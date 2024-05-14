import random

unique_numbers = set()
while len(unique_numbers) < 190:
    unique_numbers.add(random.randint(1, 1000))

random_numbers = list(unique_numbers)
sorted_random_numbers = sorted(random_numbers)
print(f"{random_numbers = }")
print(f"{sorted_random_numbers = }")
searching_number = int(input("Enter a number to search between 1 and 1000: "))

def linear_search(data_list, value):

    for i in range(len(data_list)):
        if data_list[i] == value:
            return i
    return "Value not found"
    # OR
    # return next((i for i in range(len(data_list)) if data_list[i] == value), "Value not found")

def binary_search(data_list, value):
    low = 0
    high = len(data_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if data_list[mid] == value:
            return mid
        elif data_list[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return "Value not found"

# Линейно търсене за индекса на числото в несортирания списък
linear_index = linear_search(random_numbers, searching_number)

# Сортиране на списъка за да можем да използваме двоично търсене
random_numbers.sort()

# Двоично търсене за индекса на числото в сортирания списък
binary_index = binary_search(random_numbers, searching_number)

print("Searching for value:", searching_number)
print("Index of value in sorted list:", binary_index)
print("Index of value in unsorted list:", linear_index)
