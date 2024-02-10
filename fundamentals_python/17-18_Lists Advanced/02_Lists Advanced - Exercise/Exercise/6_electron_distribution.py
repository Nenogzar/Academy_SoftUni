num = int(input())
shells = []
count = 1

while num > 0:
    fill_shells = min(2 * count ** 2, num)
    shells.append(fill_shells)
    num -= fill_shells
    count += 1

print(shells)
