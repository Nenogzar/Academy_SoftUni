points = int(input())
bonus_count = 0

if points <= 100:
    bonus_count = 5
elif 100 < points <= 1000:
    bonus_count = 0.20 * points
else:
    bonus_count = 0.10 * points

if points % 2 == 0:
    bonus_count += 1
if points % 10 == 5:
    bonus_count += 2

print(bonus_count)
print(bonus_count + points)

