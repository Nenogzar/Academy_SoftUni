number = int(input())
counter = 0
for num_1 in range(0, number+1):
    for num_2 in range(0, number+1):
        for num_3 in range(0, number + 1):
            multiplication = num_1+num_2+ num_3
            if multiplication == number:
                counter += 1
print(counter)

