list1 = [12, 16 ,20, 12, 30, 25, 23, 24, 20]
list1.sort()
print(list1)

len_list= len(list1)
print(len_list)

if len_list % 2 == 0:
    m1 = list1 [len_list // 2]
    m2 = list1 [len_list // 2 - 1]
    median = (m1 + m2) /2
else:
    median = list1[(len_list + 1) // 2 - 1]
print(median)