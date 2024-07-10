"""
1 . Цел:
Методът __next__ се използва за дефиниране на итератор в клас. Той връща следващия елемент от итерацията.

2. Извикване:
Автоматично се извиква при използване на функцията next() върху обект-итератор.
"""

iterator = iter([1, 2, 3])
print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3

"""
3. Връщаща стойност:
Методът трябва да връща следващия елемент от последователността.
Ако няма повече елементи за връщане, трябва да повдигне изключението StopIteration.
"""


class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            return StopIteration
        else:
            self.current += 1
            return self.current - 1


counter = Counter(1, 3)
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3
print(next(counter))  # StopIteration

"""
4. Свързан с __iter__:
За да бъде клас итератор, трябва да дефинира и метода __iter__, който връща самия итератор (обикновено self).
"""


class IterableCounter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            return "StopIteration"

        else:
            self.current += 1
            return self.current - 1


counters = IterableCounter(1, 3)
print(f"counter: {next(counters)}")
print(f"counter: {next(counters)}")
print(f"counter: {next(counters)}")
print(f"counter: {next(counters)}")

"""
5.Пример за създаване на собствен итератор:
Създаването на итератор включва дефиниране на клас с методите __iter__ и __next__.
"""


class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


rev = Reverse('spam')
for char in rev:
    print(*char, end=" ")  # m a p s


"""
6. Съвместимост с цикли:
Обекти с дефинирани __iter__ и __next__ методи могат да бъдат използвани в for цикли
и други контексти, изискващи итерация.
"""

"""
counter = IterableCounter(1, 3)
for num in counter:
    print(num)  # 1 2 3
"""
print()
"""
7.Поддържане на състояние:
Итераторът обикновено поддържа вътрешно състояние,
което позволява проследяване на позицията в последователността.
"""


class Fibonacci:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a


fib = Fibonacci()

print([next(fib) for _ in range(10)])  # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

"""
ИЗПОЛЗВАНЕ на __next__:
1. Дефиниране на клас с __next__:
Създайте клас, който имплементира метода __next__ за връщане на следващия елемент от итерацията.

"""


class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


my_iter = MyIterator(1, 4)
print(next(my_iter))  # 1
print(next(my_iter))  # 2
print(next(my_iter))  # 3
print(next(my_iter))  # StopIteration

"""
2. Използване на __next__ в цикли:
Класовете, имплементиращи __next__, могат лесно да бъдат използвани в цикли.
"""
my_iter = MyIterator(1, 4)
for num in my_iter:
    print(*num, end="")  # 1 2 3

"""
3. Използване на __next__ с генератори:
Вместо да дефинирате клас с __next__, можете да използвате генератори, които автоматично поддържат итерация и състояние.
"""

def my_generator(start, end):
    current = start
    while current < end:
        yield current
        current += 1

gen = my_generator(1, 4)
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
print(next(gen))  # StopIteration

"""
Методът __next__ е основен за създаването на персонализирани итератори в Python 
и предоставя мощен начин за контролиране на итерационния процес.
"""
