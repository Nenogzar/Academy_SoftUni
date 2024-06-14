def append_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list

def extend_to_list(value, my_list=[]):
    my_list.extend(value)
    return my_list


result_app = append_to_list([1])
result_ex = extend_to_list([1])
print(f"{result_app}")


result_app1 = append_to_list([2])
result_ex1 = extend_to_list([2])
print(f"{result_app1}")


result_app2 = append_to_list([3])
result_ex2 = extend_to_list([3])
print(f"{result_app2}")