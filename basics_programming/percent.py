n = float(input("`Number is: "))
procent=int(input("%: "))
f = n
f1 = n
r = n

procent_int = float (procent / 100)
print(f"1: десетичен процент {procent_int}")
procent_invert = float(1 - procent_int)
print (f"2: procent_invert {procent_invert}")

g = n - (n * procent_int)
print(f"3: приспадане на процента: {n} - ({n} * {procent_int}) = {g}")

f *= procent_invert
print(f"4: приспадане на процента: {n} *= {procent_invert} = {f}")

f1 = n + (n * procent_int)
print(f"5: Добавяне на процент:  {n} + {n} n->{n}* {procent_int}) = {f1}")

r -= procent_invert
r1 = n - f
r2 = n - f1
print(f"6: {n} -= {n} * {procent_int} = {r:.2f}")
print(f"7: {r2}")
