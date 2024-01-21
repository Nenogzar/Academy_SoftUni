depozit = float(input())
srok_depozit = int(input())
lihva = float(input())

total = depozit + srok_depozit * ((depozit*(lihva/100))/12)
print(total)
