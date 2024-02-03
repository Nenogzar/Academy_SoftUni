""""""" random.randint() """""""""""""
# Функцията random.randint() приема два аргумента: долната граница и горната граница на диапазона.
# В този случай долната граница е 1, а горната граница е 100.
# Това означава, че функцията може да генерира всяко число от 1 до 100, включително.

num_randint = random.randint(1, 100)

print("random.randint() - ", num_randint)

# output:
# 23
# 47
# 89

""""""" random.random() """""""""""""

# Функция за генериране на случайни float
# Ето как работи функцията random.random():
# Тя използва псевдослучайна функция, за да генерира произволно число.
# 1. Числото се преобразува в плаваща запетая с точност 32 бита.
# 2. Числото се връща като резултат от функцията.
# 3. Ето как изглежда кодът за генериране на случайно число с плаваща запетая:

#import random

num_random = pythonProject.Function.random()

print("random.random() - ", num_random)

# output:
# 0.456378923456789
# 0.897654321098765
# 0.123456789012345


""""""" random.uniform() """""""""""""

# функцията random.uniform(), за да генерирате случайни числа с плаваща запетая в даден диапазон.

# Функцията random.uniform() приема два аргумента: долната граница и горната граница на диапазона.
# В този случай долната граница е 0, а горната граница е 1.
# Това означава, че функцията може да генерира всяко число от 0 до 1, включително.

#import random

num_uniform = random.uniform(0, 1)

print("random.uniform() - ", num_uniform)

# output:
# 0.456378923456789
# 0.897654321098765
# 0.123456789012345


""""""" random.choice() """""""""""""

# функция за генериране на случайни низове в Python.
# Тя се нарича random.choice() и приема един аргумент: списък от низове.
# Функцията random.choice() избира произволен елемент от списъка и го връща като резултат.

#import random

strings = ["Hello, world!", "This is a string.", "I am a random string."]

random_choice = random.choice(strings)

print("random.choice() - ", random_choice)

# Можете да използвате тази функция, за да генерирате случайни низове за различни цели,
# като например генериране на случайни имена за потребители или генериране на случайни пароли.

# output:
# Hello, world!
# This is a string.
# I am a random string.


""""""" random.sample() """""""""""""

# функцията random.sample(), за да генерирате случайен подсписък от низове.
# Функцията random.sample() приема два аргумента: списък от низове и размер на подсписъка.
# В този случай списъкът от низове е strings и размерът на подсписъка е 2.
# Това означава, че функцията ще генерира случайен подсписък от два елемента от списъка strings.

#import random

strings = ["Hello, world!", "This is a string.", "I am a random string."]

random_sample = random.sample(strings, 2)

print(random_sample)

# Този код ще генерира случайен подсписък от два елемента от списъка strings.
# output:

# ["Hello, world!", "This is a string."]
# ["I am a random string.", "Hello, world!"]
# ["This is a string.", "I am a random string."]

