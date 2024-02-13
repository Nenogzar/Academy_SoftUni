# Median
list1 = [12, 16 ,20, 12, 30, 25, 23, 24, 20, 21]
list1.sort()
print(list1)

len_list= len(list1)


if len_list % 2 == 0:
    print(f"len_list is event -> {len_list = }")
    m1 = list1 [len_list // 2]
    m2 = list1 [len_list // 2 - 1]
    median = (m1 + m2) /2
else:
    print(f"len_list is odd -> {len_list = }")
    median = list1[(len_list + 1) // 2 - 1]
print(f"{median = }")


# Mode
#list2 = [12, 16 ,20, 12, 30, 25, 23, 24, 20, 21]
frequency = {}
for i in list1:
    frequency.setdefault(i, 0)
    frequency[i]+=1

frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i
print(f"{mode = }")