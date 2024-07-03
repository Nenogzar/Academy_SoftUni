check1 = ['Learn', 'quiz', 'practice', 'contribute']
check2 = check1
check3 = check1[:]

check2[0] = "Code"
check3[1] = "Mcq"

counter = 0

for c in (check1, check2, check3):
    if c[0] == "Code":
        counter += 1
    if c[1] == "Mcq":
        counter += 10

print(counter)