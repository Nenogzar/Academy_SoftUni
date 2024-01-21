nlist = [1, 2, 3, 4]

total = 0  # Инициализирайте променлива за сумата
count = len(nlist)  # Брой на числата в списъка

for num in nlist:
    total += num  # Добавете числото към сумата

# Изчислете средно аритметичното
average = total / count

print(f"The total value on the number i the list is: {total:.2f}")
print(f"The average value in the list is: {average:.2f}")




