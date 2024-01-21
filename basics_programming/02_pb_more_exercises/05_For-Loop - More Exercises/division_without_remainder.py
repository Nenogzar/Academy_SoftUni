numbers = int(input())
dev_2 = 0
dev_3 = 0
dev_4 = 0


for num in range(numbers):
    number = int(input())
    if number % 2 == 0:
        dev_2 += 1
        if number % 3 == 0:
            dev_3 += 1
        elif number % 4 == 0:
            dev_4 += 1
    elif number % 3 == 0:
        dev_3 += 1
    elif number % 4 == 0:
        dev_4 += 1

print(f"{dev_2/numbers*100:.2f}%")
print(f"{dev_3/numbers*100:.2f}%")
print(f"{dev_4/numbers*100:.2f}%")


