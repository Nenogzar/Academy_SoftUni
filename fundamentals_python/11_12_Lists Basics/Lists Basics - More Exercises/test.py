# list1 = [1, 222, 333, 444, "b", "a", "g", 23, 24, 25, 26, 5]
# list2 = [1, 22, 32, 43, 24, 25, 27, 28, 5]
#
# common_elements = list(set(list1) & set(list2))
#
# print("Common elements:", common_elements)

#####################################
new_list =[]
list3 = ["apple", "banana", "orange"]
# for n in range(len(list3)):
#     print(list3[n])
#     n += 1

# i = 0
# while i < len(list3):
#     print(list3[i])
#     i += 1
############################
# for x in list3:
#     if "n" in x:
#         new_list.append(x)
# print(new_list)

### whit comprehension

# new_list = [x for x in list3 if "n" in x]
# print(new_list)
""" """
for n in list3:
    if n != "apple":
        new_list.append(n)
# [new_list.append(n) for n in list3 if n != "apple"]
print(new_list)
""" """
num_list = []
for x in range(1, 11):
    num_list.append(x)
# [num_list.append(x) for x in range(1, 11)]
print(num_list)

list4 = []
for l in num_list:
    if l < 6:
        list4.append(l)
# [list4.append(l) for l in num_list if l < 6]
print(list4)


