#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Колекции: типове данни, които съхраняват повече от една стойност
# Типове колекции: списъци, кортежи, речници и др.
# Types of collections: lists, tuples, dictionaries, etc.
# Една колекция има две основни свойства: наредба и изменчивост
# A collection has two main properties: order and mutability
# Наредба: дали може да се подреди или не
# изменчивост: дали може да се променя или не

# Оператор за членство - Membership operator (in): проверява дали елемент принадлежи на колекция
#
# "n" in "самолет"  --> True
# 2 in [1,3,4]  --> False
#
# ВСЯКА КОЛЕКЦИЯ Е ITERABLE /Повтаряема/ (може да се изброи)

# Основно свойство на Python: НИЗОВЕТЕ СА КОЛЕКЦИИ

# Вградени функции на Python:
# a) Общи (приложими към всякакъв тип данни):
#   print(), del(), int(), bool(), float(), str(), input(), help(),...
#
# b) За колекции:
#   len(), sum(), max(),  min()
#
# c) Специфични за всеки ТИП ДАННИ
# променлива.функция()
# Пример: превръщане на думата "здравей" в главни букви: "здравей".upper() --> "ЗДРАВЕЙ"

# Lists
# Те са КОЛЕКЦИИ С НАРЕДБА и ИЗМЕНЧИВОСТ
# They are ORDERED and MUTABLE collections
list = []
print(f"Празен list: {list}")

list = [1, 3, "Здравей", 25.2, True]
print(f"list: {list}")

# Достъп до елементите
print(f"1-ви елемент: {list[0]}")
print(f"3-ти елемент: {list[2]}")
print(f"Последен елемент: {list[-1]}")
print(f"Предпоследен елемент: {list[-2]}")

# Брой на елементите:
print(f"Общ брой на елементите: {len(list)}")

# Промяна на елементите
list[0] = "Първи"
list[-1] = "Последен"
print(f"Променен list: {list}")

# Изтриване на елементи
del(list[-2])
print(f"Предпоследен елемент изтрит: {list}")

# Изтриване на списъка:
# del(list)
# print(list) # вдига грешка, списъкът е изтрит

# Добавяне на елементи: със специфични функции
# Добавяне на елемент в края на списъка
list.append(1000)
print(list)

# Вмъкване на "втори" между "Първи" и 3
list.insert(1, "втори")
print(list)

# Изчистване на list
list.clear()
print(f"Празен list: {list}")

# Скрипт, който изчислява средния успех, най-високата и най-ниската оценка от list с оценки/grades/
grades = [5, 8, 9, 10, 4, 3, 5, 7, 8, 9, 10, 10, 10, 8, 7, 9]
print(f"Average: {sum(grades) / len(grades):.2f}")
print(f"Highest grade: {max(grades)}")
print(f"Lowest grade: {min(grades)}")

# If the lists are homogenous, they can be sorted
# Ако списъците са хомогенни, те могат да бъдат сортирани
names = ["Alan", "Zoilo", "Abel", "Marta", "Carina"]
print(names)
names.sort()
print(f"Names sorted alphabetically: {names}")
names.sort(reverse=True)
print(f"Names sorted alphabetically in reverse: {names}")

print("\n\n\n")

# Strings as collections:
# Strings are ORDERED and IMMUTABLE collections
# Низовете са ПОДРЕДЕНИ и НЕИЗМЕНЯЕМИ колекции
# "hello"[0]  --> returns "h"
# "hello"[0] = "C"  --> ERROR, you cannot modify a string