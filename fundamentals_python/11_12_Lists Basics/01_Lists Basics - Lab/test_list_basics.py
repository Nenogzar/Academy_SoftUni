n = int(input())

for _ in range(n):
    line = input()

    name_start = line.index('@')
    print("name_start ", name_start)
    name_end = line.index('|', name_start)
    print("name_end ", name_end)
    age_start = line.index('#', name_end)
    print("age_start ", age_start)
    age_end = line.index('*', age_start)
    print("age_end ", age_end)

    if name_start != -1 and name_end != -1 and age_start != -1 and age_end != -1:
        name = line[name_start + 1:name_end]
        age = line[age_start + 1:age_end]
        print(f"{name} is {age} years old.")

"""""""""
input
1
Here is a name @George| and an age #18*