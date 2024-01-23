head = input()
body = input()
tail = input()
text = [tail, body, head]
print(text)

###################################*-FROM**zahariev-webbersof*-*####################################
my_list = []

for _ in range(3):
    data = input()
    my_list.append(data)
my_list[0], my_list[2] = my_list[2], my_list[0]
print(my_list)

############################################*-*[::1]*-*#############################################
my_list1 = []

for _ in range(3):
    data = input()
    my_list1.append(data)
new_list = my_list1[::-1]
print(new_list)
###########################################*-*revers[]*-*###########################################
my_list2 = []

for _ in range(3):
    data = input()
    my_list2.append(data)
    new_list2 = my_list2.reverse()
print(new_list2)
