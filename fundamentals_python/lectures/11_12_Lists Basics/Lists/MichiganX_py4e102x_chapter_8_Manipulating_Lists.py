a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(f"{a} + {b} = {c}")
print()

t = [9, 41, 12, 3, 74, 15]
print(f"{t = }")
# списъка е: [9, 41, 12, 3, 74, 15]

print("t[1:3] ->", t[1:3])
# от 2ри до 3ти - [1:3] -> [41, 12]

print("t[:4] ->", t[:4])
# от начало до 4ти - [:4] -> [9, 41, 12, 3]

print("t[3:] ->", t[3:])
# от 3ти до края [3:] -> [3, 74, 15]

print("t[:] ->", t[:])
# от начало до край [:] -> [9, 41, 12, 3, 74, 15]

print("t[::-1]", t[::-1])

####### 3.1.3. Lists¶  https://docs.python.org/3/tutorial/introduction.html#lists ########
cubes = [1, 8, 27, 65, 125]
print(f"{cubes = }")

cubes[3] = 64               # За разлика от низовете, които са неизменни, списъците са променлив тип,
                            # т.е. възможно е да се променя тяхното съдържание:
print("cubes[3] = 64 ->", cubes)

cubes.append(7 ** 3)        # Можете също така да добавяте нови елементи в края на списъка,
                            # като използвате метода list.append() (ще видим повече за методите по-късно):

print("cubes.append(7 ** 3)->", cubes)
#[1, 8, 27, 64, 125]

# Присвояването на срезове също е възможно и това може дори да промени размера на списъка или да го изчисти изцяло:

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(f"{letters = }")
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']

letters[2:5] = ['C', 'D', 'E']  # replace some values
print("letters[2:5] = ['C', 'D', 'E'] -> ", letters)
# ['a', 'b', 'C', 'D', 'E', 'f', 'g']

# clear the list by replacing all the elements with an empty list
letters[:] = []
print("letters[:] = [] -> ", letters)
# []

# The built-in function len() also applies to lists:
letters = ['a', 'b', 'c', 'd']

print("len(letters) ->", len(letters))
# 4

# Възможно е да се влагат списъци (създаване на списъци, съдържащи други списъци), например:
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
# [['a', 'b', 'c'], [1, 2, 3]]

# Разбира се, можем да използваме Python за по-сложни задачи от събирането на две и две.
# Например, можем да напишем начална под-последователност на редицата на Фибоначи, както следва:

# l, m = 0, 1
# while l < 10:
#     print(l, end=", ")
#     l, m = m, l+m

# 0, 1, 1, 2, 3, 5, 8,

"""""или :"""""
l, m = 0, 1     # начални стойности на реда
upper_limit = int(input("Въведете горната граница на редицата на Фибоначи: "))

fibonacci_sequence_l = []    # Дефинира списъка съхраняващ стойностите
fibonacci_sequence_m = []
fibonacci_sequence =[]
fibonacci_sequence_nested = []
while l < upper_limit:
    fibonacci_sequence_l.append(l)
    fibonacci_sequence_m.append(m)
    l, m = m, l + m
    fibonacci_sequence = fibonacci_sequence_l + fibonacci_sequence_m    # +
    fibonacci_sequence_nested = [fibonacci_sequence_l, fibonacci_sequence_m]    # nested lists

# Използвайте join, за да обедините елементите в низ със запетаи и изпечатайте го
print(', '.join(map(str, fibonacci_sequence_l)))
print(', '.join(map(str, fibonacci_sequence_m)))
print(', '.join(map(str, fibonacci_sequence)))
print(', '.join(map(str, fibonacci_sequence_nested)))

""""" - Method append() - """""""""

stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)

#Output
#['book', 99]
stuff.append('cookie')
print(stuff)
#Output
#['book', 99, 'cookie']


""""" - Is Sommething is a List?- """""""""

some =[1, 9, 21, 10, 16]
if 9 in some:
    print("True")
else:
    print("False")
# output True

if 15 in some:
    print("True")
else:
    print("False")
# output False

if 20 not in some:
    print("True")
else:
    print("False")
# output True

""""" - Lists are in Order """""""""
friends = ['Joseph', "Glenn", 'Sally']
print(friends[1])
# output: Glenn

friends.sort()
# output: ["Glenn", 'Joseph', 'Sally']
print(friends)
print(friends[1])
# output: Joseph


""""" Built-in Functions and Lists """""""""
nums = [3, 41, 12, 9, 74, 15]
len_nums = len(nums)
# output: 6

max_nums = max(nums)
# output: 74

min_nums = min(nums)
# output: 3

sum_nums = sum(nums)
# output: 154

average_nums = (sum_nums / len_nums)
print(average_nums)
# output: 25.6


""""" - average - """""
# total = 0
# count = 0
# while True:
#     inp = input(('Enter a number: '))
#     if inp == "done ": break
#     value = float(inp)
#     total += value
#     count += 1
#
# everage = total / count
# print('Average: ', average)

num_list = list()                       # дефиниране на списък
while True:
    inp = input('Enter the number: ')   # променлива за аргумент
    if inp == 'done': break             # условие за спиране на записите в списъка
        #break
    value = float(inp)
    num_list.append(value)              # добавяне в списъка
    total = sum(num_list)               # total += value
    count = len(num_list)               # count += 1
    if total == 0:
        break
    else:
        average = total / count                 # пресмятане
print('Average:', average)


""""" - PART 3 - """""
""""" - String in Lists - """""
# Split

# Split разделя низ на части и създава списък от низове.
# Мислим за това като за думи.
# Можем да имаме достъп до конкретна дума или да преминем през всички думи.

abc = " whit three words"
split_list = abc.split()
print(split_list)
# output: ['whit', 'three', 'words']
#
print(len(split_list))
# output: 3

print(split_list[0])
# output: whit

for w in split_list:
    print(w, end=' ')
print()
# output:   whit three words

# Split - lot of spaces

line = 'A lot         of     spaces'
etc = line.split()              # Премахва празните полета
print('line:', etc)
# output: ['A', 'lot', 'of', 'spaces']

line1 = 'first;second;third'
etc1 = line1.split()            # списъка е с ; и ги разчита като един аргумент
print('line1:', etc1)
# output: ['first;second;third']

etc2 = line1.split(';')         # премахва ; и прави отделни аргументи
print('line2:', etc2)
# output: ['first', 'second', 'third']

