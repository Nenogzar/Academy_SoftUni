
x = [1, 2, 3, 4, 5, 6]
list1 = list(x)
#[1, 2, 3, 4, 5, 6]

text = 'a b c d e'
text_list = list(text)
# ['a', ' ', 'b', ' ', 'c', ' ', 'd', ' ', 'e']
text_list1 = text.split(" ")
# ['a', 'b', 'c', 'd', 'e']

num = input(" въведи стойности разделени със запетая ").split(', ')   # Сплит към списък
# input:    1, 2, 3, 4, 5, 3
# output:   ['1', '2', '3', '4', '5', '3']

#############################################*-map()-*##############################################
num_list = list(map(int, input("въведи стойности разделени със запетая ").split(', ')))

# map(function, iterable, [iterable1, iterable2, .....]])

#############################################*-join()-*#############################################
str_list = ['a', 'b', 'c']
join_list = ("-".join(str_list))
# a-b-c

############################################*-[index]-*#############################################
my_list = ['a', 'b', 'c']
print("index [0] ->", my_list[0])           # a
print("index [-1] ->", my_list[-1])         # c
print("reversed list ->", my_list[::-1])    # ['c', 'b', 'a']
print("index [:1] ->", my_list[:1])         # ['a']
print("index [1:] ->", my_list[1:])         # ['b', 'c']


list = [x for x in range(2, 11)]
print(list[::2])
# [2, 4, 6, 8, 10]

############################################*-*pop()*-*#############################################
new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
popped_list = new_list.pop(3)
# 4

odd_list = [x for x in range(1, 11) if x % 2 != 0]
even_list = [x for x in range(1, 11) if x % 2 == 0]
# [1, 3, 5, 7, 9])
# [2, 4, 6, 8, 10]



