""" 1 """
# largest = max(int(input()), int(input()), int(input()))
# print(largest)

""" 2 """
# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
# if n1 >= n2 and n1 >= n3:
#     large = n1
# elif n2 >= n1 and n2 >= n3:
#     large = n2
# else:
#     large = n3
# print(large)

""" 3 """
num_list = []
for _ in range(3):
    num_list.append(int(input()))
    max_num=max(num_list)
print(max_num)

