def show (num_list = [0,1,2]):
    for k in range (len(num_list)):
        num_list[k] += 1
    print(num_list, id(num_list))

show()
show()
show()


def f(my_list=[]):
    my_list.append('###')
    return my_list, id(my_list)

print(f())
print(f())
print(f())

""" As a workaround, consider using a default argument value 
that signals no argument has been specified. 
Most any value would work, but None is a common choice. 
When the sentinel value indicates no argument is given, 
create a new empty list inside the function """

def f1(my_list=None):
    if my_list is None:
        my_list =[]
    my_list.append('###')
    return my_list, id(my_list)

print(f1())
print(f1())
print(f1())