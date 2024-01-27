all_numbers = input().split()
count_of_numbers_to_remove = int(input())
only_big_numbers = []
numbers_as_integers = []

for number in all_numbers:
    numbers_as_integers.append(int(number))

for _ in range(count_of_numbers_to_remove):
    min_number = min(numbers_as_integers)
    numbers_as_integers.remove(min_number)

only_big_numbers = numbers_as_integers
print(', '.join(map(str, only_big_numbers)))