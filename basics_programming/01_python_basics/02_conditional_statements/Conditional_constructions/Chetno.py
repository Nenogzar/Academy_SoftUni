a=int(input('Въведете стойност: '))

chetnoa = int(a) % 2
if chetnoa == 0:
    print(f"Числото {a} е четно - even")
else:
    print("Числото", a, "е нечетно - odd")