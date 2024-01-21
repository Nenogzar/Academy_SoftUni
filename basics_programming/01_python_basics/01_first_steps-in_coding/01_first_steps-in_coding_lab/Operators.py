a = input("въведете стойност за 'а' ",)
b = input("въведете стойност за 'b' ",)
concat = a + b              # Долепване
sum1 = int(a) + int(b)      # Сбор
result = int(a) - int(b)    # Разлика
umno = int(a) * int(b)      # произведение
delene = int(a) / int(b)    # деление
delcelo = int(a) // int(b)  # целочислено делене
product = int(a) % int(b)   # остатък от целочислено делене if = 0 then Четно Else Нечетно


print("Сбора от a и b e:  ", sum1)
print("Слепване на  a и b e:  ", concat)
print("Разликата от a и b e:  ", result)
print("произведение от a и b e:  ", umno)
print("деление от a и b e:  ", delene)
print("целочислено делене от a и b e:  ", delcelo)
print("остатък от целочислено делене от a и b e:  ", product)

chetnoa = int(a) % 2
if chetnoa == 0:
    print("Числото", a, "е четно")
else:
    print("Числото", a, "е нечетно")

chetnob = int(b) % 2
if chetnob == 0:
    print("Числото", b, "е четно")
else:
    print("Числото", b, "е нечетно")
