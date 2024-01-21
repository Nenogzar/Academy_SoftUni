# Write a program that receives two numbers (factor and count).
# It should create a list with a length of the given count that contains only integer numbers,
# which are multiples of the given factor.
# The numbers should be only positive, and they should be arranged in ascending order,
# starting from the value of the factor.

# x = int(input())
# y = int(input())
# new_list=[]
# for n in range(x, x*y+1, x):
#     new_list.append(n)

x, y = int(input()), int(input())
new_list = [n for n in range(x, x*y+1, x)]
print(new_list)

########################  From CEO #################################

# numner_one = int(input())
# numner_two = int(input())
#
# print([x * numner_one for x in range(1, numner_two + 1)])



# numner_one = int(input())
# numner_two = int(input())
#
# print_text = list()
#
# for number in range(1, numner_two + 1):
#     print_text.append(number * numner_one)
#
# print(print_text)


