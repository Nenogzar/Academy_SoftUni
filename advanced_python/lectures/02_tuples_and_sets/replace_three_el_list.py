""" unpack tuple to 2 elements """
tup = (1,2,3,4,5)
x, *y = tup
print(f"x: {x}, y: {y}")

"""swap elements of two tuples"""
tup1 = (1, 2)
tup2 = (3, 4)
tup1, tup2 = tup2, tup1
print(f"tup1: {tup1}, tup2: {tup2}")

"""Sort the nested tuple by the second element"""

my_tuple = ((1, 44), (2, 33), (3, 22), (4, 11))
sort_nest = tuple(sorted(my_tuple, key=lambda x: x[1]))
print(f"sort_nest: {sort_nest}")

"""Modify the given tuple as per the expected output"""
given_tuple = (1, 2, [3, 4], 5)
given_tuple[2][0] = 6
print(f"given_tuple: {given_tuple}")

"""Count the number of occurrences of item 4 from the tuple"""

count_tuple = (1, 2, 3, 4, 5, 4)
count_4 = count_tuple.count(4)
print(f"count_tuple: {count_tuple}, count_4: {count_4}")

"""Replace the first 3 elemnts of the list whit elements of the tuple"""

tup = (1, 2, 3)
lst = [10, 20, 30, 4, 5, 6]

for i, v in enumerate(tup):
    lst[i] = v

print(lst)

"""Write the program to find the second-largest element from the tuple"""
t = (1,5,8,7,6,3,4)
max_t = max(t)
length = len(t)
second_max = 0
for num in range(length):
    if second_max < t[num] < max_t:
        second_max = t[num]
print(second_max)

"""Write a program to check if a tuple contains duplicates."""

tup = (1, 2, 3, 4, 5, 1,2)

for i in tup:
    if tup.count(i) > 1:
        print("Tuple contains duplicates")
        break
    else:
        print("Tuple contains no duplicates")